'''
Created on 25 de abr de 2019

@author: lsrodrigues
'''

import Pyro4
               
               
@Pyro4.expose
class ExemploPPD(object):
    def get_salario(self, nome, cargo, salario):
        
        if cargo == "operador":
            salario = int(salario,10)
            salarioNovo =  1.2*salario 
        else:
            salario = int(salario)
            salarioNovo =  1.18*salario 
                 
        return "O nome do empregado eh: "+nome + "\n"\
                "o novo salario eh: "+  str(salarioNovo)  
                

daemon = Pyro4.Daemon()                # make a Pyro daemon
ns = Pyro4.locateNS()                  # find the name server


uri = daemon.register(ExemploPPD)   
ns.register("examplo.ppd", uri)

print("Ready.")
daemon.requestLoop()                   # start the event loop of the server to wait for calls