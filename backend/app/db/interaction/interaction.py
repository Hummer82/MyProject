import os
import sys
sys.path.append(os.getcwd())
sys.path.append("C:\\Users\\user\\Documents\\GitHub\\MyProject\\backend\\app\\api")
sys.path.append("C:\\Users\\user\\Documents\\GitHub\\MyProject\\backend\\app\\db")
# print(os.getcwd())
# print(sys.path)
from utils import config_parser
from client.client import MySQLConnection
from models.models import User
from models.models import Base
from exceptions import UserNotFoundException

class DbInteraction:
    
    def __init__(self, host, port, user, password, db_name, rebuild_db=False):
        self.mysql_connection = MySQLConnection(
            host=host,
            user=user,
            port=port,
            password=password,
            db_name=db_name,
            rebuild_db=rebuild_db
        )
        
        self.engine = self.mysql_connection.engine
        
        if rebuild_db:
            self.create_table_me('users')
            self.create_table_me('musical_compositions')
    
    def create_table_me(self, table_name: str):
        if not self.engines.dialect.has_table(self.engine, table_name):
            Base.metadata.tables[table_name].create(self.engine)
        else:
            self.mysql_connection.execute_query(f'DROP TABLE IF EXISTS {table_name}')
            Base.metadata.tables[table_name].create(self.engine)

    def add_user_info(self, username, email, password):
        user = User(
            username=username,
            password=password,
            email=email
        )
        self.mysql_connection.session.add(user)
        return True

    def get_user_info(self, username):
        user = self.mysql_connection.session.query(User).filter_by(username=username).first()
        if user:
            self.mysql_connection.session.expire_all()
            return {'username': user.username, 'email': user.email, 'password': user.password}
        else:
            raise UserNotFoundException('User not found!')

if __name__=='__main__':
    
    config = config_parser('C:\\Users\\user\\Documents\\GitHub\\MyProject\\backend\\app\\api\\config.txt')
    
    db = DbInteraction(
        host=config['MYSQL_HOST'],
        port=int(config['MYSQL_PORT']),
        user=config['MYSQL_USER'],
        password=config['MYSQL_PASSWORD'],
        db_name=config['MYSQL_DB_NAME'],
        rebuild_db=True
    )