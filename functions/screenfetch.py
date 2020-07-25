def screenfetch(client):
    stdin, stodout, stderr = client.exec_command('screenfetch')
    resultado = stodout.read().decode()
    return resultado