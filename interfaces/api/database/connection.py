from mongoengine import connect
from xaas.config import Config as config


class Connection:
    def __enter__(self):
        self.conn = connect('postsdb', host=config.MONGO_URL, port=config.MONGO_PORT)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
