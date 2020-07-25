def show_potgres(client):
    stdin, stodout, stderr = client.exec_command('systemctl status postgresql.service')
    resultado = stodout.read().decode()
    return resultado