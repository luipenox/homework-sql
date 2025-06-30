import mariadb
import sys


def get_connection():
    try:
        connection = mariadb.connect(
            user="guest",
            password="ctu-relational",
            host="relational.fel.cvut.cz",
            port=3306,
            database="classicmodels"
        )

        return connection

    except mariadb.Error as e:
        pass