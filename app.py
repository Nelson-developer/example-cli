from paramiko import SSHClient, AutoAddPolicy, ssh_exception
import pyfiglet 
from preguntas import question
#funciones
from functions.screenfetch import screenfetch
from functions.servicemongo import service_mongo
from functions.servicepostgres import show_potgres
from dotenv import load_dotenv
import os

HOST = '192.168.0.23'

USER = 'nelson'

if __name__ == "__main__":
    try:
        load_dotenv() # Carga las variables de entorno
        print(os.getenv('contraseña'))
        result = pyfiglet.figlet_format(f'                        HorchataJS') 
        print(result)
        selected = question()
        client = SSHClient()
        # le decimos que nos conectaremos con nuestras propias credenciales
        client.set_missing_host_key_policy(AutoAddPolicy())
        client.connect(HOST,username=USER, password=os.getenv('contraseña'))
            #Condicionales
        if selected['procesos'][0] == "screenfetch":
            print(screenfetch(client))

        if selected['procesos'][0] == "Verificar el estado de MongoDB":
            print(service_mongo(client))
            
        if selected['procesos'][0] == "Verificar el estado de PostgreSQL":
            print(show_potgres(client))

        client.close()

    except ssh_exception.AuthenticationException:
        print('Autenticación Fallida')
    