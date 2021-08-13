import os
import time

#Abrir como arquivo
with open('hosts.txt') as file:
    dump = file.read()
    dump = dump.splitlines()

    for ip in dump:
        print('Verificando o ip: ', ip)
        print('-' * 60)
        os.system('ping -w 5 {}'.format(ip))
        print('-' * 60)
        time.sleep(5)
