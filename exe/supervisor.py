import psutil, os

if __name__ == '__main__':
    while True:
        encontrado = 0
        for proc in psutil.process_iter():
            if proc.name().lower() == 'agenda.exe':
                encontrado = 1
        if encontrado == 1:
            pass
        else:
            os.system('Agenda.exe')