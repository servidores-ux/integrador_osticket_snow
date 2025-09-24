import os
import psycopg2 
class PSQL:
    def __init(self):
        self._pg_host = os.getenv("PG_HOST")
        self._pg_port = int(os.getenv("PG_PORT", 5432))
        self._pg_user = os.getenv("PG_USER")
        self._pg_password = os.getenv("PG_PASSWORD")
        self._pg_dbname = os.getenv("PG_DBNAME")
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