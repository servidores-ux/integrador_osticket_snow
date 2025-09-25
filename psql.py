import os
import psycopg2 
class PSQL:
    def __init__(self):
        self._pg_host = os.getenv("IP_SNOW")
        self._pg_port = int(os.getenv("PORT_SNOW", 5432))
        self._pg_user = os.getenv("USER_SNOW")
        self._pg_password = os.getenv("PASS_SNOW")
        self._pg_dbname = os.getenv("DB_SNOW")

    def connect(self):
        """Conectar a la base de datos PostgreSQL"""
        conn = psycopg2.connect(
            host=self._pg_host,
            port=self._pg_port,
            user=self._pg_user,
            password=self._pg_password,
            dbname=self._pg_dbname
        )
        return conn