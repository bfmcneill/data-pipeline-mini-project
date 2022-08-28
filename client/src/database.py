import os

import mysql.connector


def get_mysql_cnxn():
    return mysql.connector.connect(
        user=os.getenv('DATABASE_USER'),
        password=os.getenv('DATABASE_PASSWORD'),
        host=os.getenv('DATABASE_HOST'),
        database=os.getenv('DATABASE_NAME')
    )
