'''
Created on 22 de abr de 2019

@author: lsrodrigues
'''


import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

# text = input("Insira sua mensagem:");


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
    nome = input("Insira o nome do funcionario:").encode()    
    cargo = input("Insira o cargo do funcionario:").encode()    
    salario = input("Insira o salario do funcionario:").encode()    
    text = nome + "/".encode() +cargo +"/".encode() + salario
        
    s.connect((HOST, PORT))
    s.sendall(text)
    
    data = s.recv(1024)
    temp = str(data.decode()).replace("'", "")
    temp = temp.split("/") 

print('Nome: '+temp[0])
print('Novo Salario: '+temp[1])
