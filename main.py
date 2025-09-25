from dotenv import load_dotenv
import os
from system import System

load_dotenv()


def main():
    system = System()

    system.verificar_sincronizacion()


    return
    departamentos = system.obtener_departamentos()
    for dept in departamentos:
        print("Departamento:", dept[1])
        ayudantes = system.obtener_ayudantes(dept[0])
        for ayudante in ayudantes:
            print("  Ayudante:", ayudante[4])
            print("  Email:", ayudante[5])

        

    pass
if __name__=="__main__":
    main()
