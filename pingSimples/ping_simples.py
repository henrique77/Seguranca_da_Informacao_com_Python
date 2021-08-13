import os #Importar o modulo ou biblioteca OS
            #(Intrega os programas e recursos do S.O

print('#' * 60)

ip_ou_host = input("Digite o Ip ou host a ser verificado: ")
print('-' * 60)
#-w 10 --tempo em segundo que o ping sera executado
os.system('ping -w 10 {}'.format(ip_ou_host))

print('-' * 60)