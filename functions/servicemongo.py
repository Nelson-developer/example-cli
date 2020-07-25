def service_mongo(session):
    session.exec_command('systemctl status mongodb.service')
    resultado = session.recv(1024).decode()
    return resultado