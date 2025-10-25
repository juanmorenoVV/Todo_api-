from psycopg2.pool import ThreadedConnectionPool
from config import settings
from contextlib import contextmanager
import logging
logger = logging.getLogger(__name__)



class DataBaseConnection:
    def __init__(self, settings):
        self.db_user = settings.DB_USER
        self.db_password = settings.DB_PASSWORD 
        self.db_port = settings.DB_PORT
        self.db_host = settings.DB_HOST
        self.db_name = settings.DB_NAME
        self.pool = None


        try:
            self.pool = ThreadedConnectionPool(
                minconn=1,
                maxconn=5,
                user = self.db_user,
                password = self.db_password,
                port = self.db_port,
                host = self.db_host,
                dbname = self.db_name
            )
        
        except Exception as error:
            logger.info(f"An error ocurred in the pool {error}")
            raise

    

    @contextmanager
    def get_connection(self):
        conn = None

        try:
            conn = self.pool.getconn()
        
            yield conn
            logger.info("Connection succes")            
        except Exception as error:
            logger.error(f"An error ocurred during the yield {error}")
            raise

        finally:
            if conn:
                self.pool.putconn(conn)

    def close_pool(self):
        
        try:
            if self.pool:
                self.pool.closeall()
            logger.info("Connection pool closed")

        except Exception as error:
            logger.error(f"An error ocurred during close pools connections {error}")



if __name__ == '__main__':

    connection_proof = DataBaseConnection(settings)

    with connection_proof.get_connection() as conn:
        
        cur = conn.cursor()
        cur.execute('SELECT 1')
        print(cur.fetchone())
        cur.close()
    connection_proof.close_pool()



# ssh url for repo https://github.com/juanmorenoVV/Todo_api-.git