def screenfetch(session):
    session.exec_command('screenfetch')
    resultado = session.recv(1024).decode()
    return resultado