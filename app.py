from paramiko import SSHClient, AutoAddPolicy, ssh_exception
import pyfiglet 
from preguntas import question
from loading import show_loading

#funciones
from functions.screenfetch import screenfetch
from functions.servicemongo import service_mongo
from functions.servicepostgres import show_potgres

HOST = '192.168.0.28'

USER = 'nelson'

if __name__ == "__main__":
    try:
        
        result = pyfiglet.figlet_format(f'                        HorchataJS') 
        print(result)
        selected = question()
        client = SSHClient()
        # le decimos que nos conectaremos con nuestras propias credenciales
        client.set_missing_host_key_policy(AutoAddPolicy())
        client.connect(HOST,username=USER, password='pa$$w0rd')

        session = client.get_transport().open_session()

        if session.active:
            #Condicionales
            if selected['procesos'][0] == "screenfetch":
                print(screenfetch(session))

            if selected['procesos'][0] == "Verificar el estado de MongoDB":
                print(service_mongo(session))
            
            if selected['procesos'][0] == "Verificar el estado de PostgreSQL":
                print(show_potgres(session))

        client.close()

    except ssh_exception.AuthenticationException:
        print('Autenticación Fallida')
    