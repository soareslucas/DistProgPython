import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    
    i = 1
    
    while True:
        
        print('Aceitando nova conexao');
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            
            
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                
                temp = str(data.decode()).replace("'", "")     
                temp = temp.split("/")
                
                nome = temp[0]                
                cargo = temp[1]                
                salario = temp[2]
                
                print(nome)
                print(cargo)
                print(salario)
                
                if cargo == "operador":
                    salario = int(salario,10)
                    salarioNovo =  1.2*salario 
                else:
                    salario = int(salario)
                    salarioNovo =  1.18*salario 
                
                text = nome.encode() + b"/"+ str(salarioNovo).encode() 
                
                conn.sendall(text)
                
        i = i +1;        