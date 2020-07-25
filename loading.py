from progress.bar import Bar
import time

def show_loading():
    #Barra de CARGA
        bar = Bar('Cargando', max=10)
        for i in range(10):
            bar.next()
            time.sleep(0.5)
        bar.finish()