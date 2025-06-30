import mysql.connector


def get_connection():
    try:
        connection = mysql.connector.connect(
            user="guest",
            password="ctu-relational",
            host="relational.fel.cvut.cz",
            port=3306,
            database="classicmodels"
        )

        return connection

    except mysql.connector.Error as e:
        pass