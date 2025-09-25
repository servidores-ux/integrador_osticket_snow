from psql import PSQL
from mysql2 import MYSQL
class System:
    def __init__(self):
        pass
    def obtener_agentes(self):
        psql = PSQL()
        connector = psql.connect()
        query = "SELECT * FROM snowflake_usersnow;"
        cursor = connector.cursor()
        cursor.execute(query)
        resultado = cursor.fetchall()
        return resultado
    def obtener_departamentos(self):
        psql = PSQL()
        connector = psql.connect()
        query = "SELECT * FROM ladeco_team;"
        cursor = connector.cursor()
        cursor.execute(query)
        resultado = cursor.fetchall()
        return resultado

    def obtener_ayudantes(self,id_depto):
        psql = PSQL()
        connector = psql.connect()
        query = """SELECT * FROM  snowflake_usersnow AS a JOIN ladeco_team_users as b ON a.id=b.usersnow_id WHERE b.team_id=%s;"""
        cursor = connector.cursor()
        cursor.execute(query,(id_depto,))
        resultado = cursor.fetchall()
        return resultado
        pass
    
    def os_team(self):
        mysql = MYSQL()
        connector = mysql.connect()
        query = "SELECT * FROM ost_team;"
        cursor = connector.cursor()
        cursor.execute(query)
        resultado = cursor.fetchall()
        return resultado
    def os_staff(self):
        mysql = MYSQL()
        connector = mysql.connect()
        query = "SELECT * FROM ost_staff;"
        cursor = connector.cursor()
        cursor.execute(query)
        resultado = cursor.fetchall()
        return resultado
    def verificar_sincronizacion_por_usuario(self,correo):
        psql = PSQL()
        connector = psql.connect()
        query = "SELECT * FROM snowflake_usersnow WHERE email=%s;"
        cursor = connector.cursor()
        cursor.execute(query,(correo,))
        resultado = cursor.fetchall()
        print(resultado)
        return resultado

    def verificar_sincronizacion(self):
        mysql = MYSQL()
        connector = mysql.connect()
        query = "SELECT * FROM ost_staff;"
        cursor = connector.cursor()
        cursor.execute(query)
        ost_staff = cursor.fetchall()
    
        psql = PSQL()
        connector = psql.connect()
        query = "SELECT * FROM snowflake_usersnow;"
        cursor = connector.cursor()
        cursor.execute(query)
        snowflake_users = cursor.fetchall()
        for user in snowflake_users:
            encontrado = False
            for staff in ost_staff:
            
                if user[5] == staff[8]:  # Comparar por correo electrónico
                    encontrado = True
                    print(f"Usuario sincronizado: {user[4]} - {user[5]}")
                    break
            if not encontrado:
                print(f"Usuario en Snowflake no encontrado en osTicket: {user[4]} - {user[5]}")