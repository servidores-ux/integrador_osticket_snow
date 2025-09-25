from psql import PSQL
class System:
    def __init__(self):
        pass
    def obtener_agentes(self):
        psql = PSQL()
        query = "SELECT * FROM email_addresses"
        agentes = psql.execute_query(query)
        return agentes
    