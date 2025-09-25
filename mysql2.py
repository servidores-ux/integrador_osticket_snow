import os
import mysql.connector
class MYSQL:
    def __init__(self):
        self._mysql_host = os.getenv("IP_OSTICKET")
        self._mysql_port = os.getenv("PORT_OSTICKET")
        self._mysql_user = os.getenv("USER_OSTICKET")
        self._mysql_password = os.getenv("PASS_OSTICKET")
        self._mysql_dbname = os.getenv("DB_OSTICKET")

    def connect(self):
        import mysql.connector
        conn = mysql.connector.connect(
            host=self._mysql_host,
            port=self._mysql_port,
            user=self._mysql_user,
            password=self._mysql_password,
            database=self._mysql_dbname
        )
        return conn