def show_potgres(session):
    session.exec_command('systemctl status postgresql.service')
    resultado = session.recv(1024).decode()
    return resultado