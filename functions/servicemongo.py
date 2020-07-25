def service_mongo(client):
    stdin, stodout, stderr = client.exec_command('systemctl status mongodb.service')
    resultado = stodout.read().decode()
    return resultado