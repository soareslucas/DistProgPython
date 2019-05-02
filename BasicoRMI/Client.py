'''
Created on 25 de abr de 2019

@author: lsrodrigues
'''
import Pyro4

nome = input("Qual seu nome? ").strip()
cargo = input("Qual seu cargo? ").strip()
salario = input("Qual seu salário? ").strip()

'''
greeting_maker = Pyro4.Proxy("PYRONAME:example.greeting")    # use name server object lookup uri shortcut
print(greeting_maker.get_fortune(name))
'''
    
greeting_maker = Pyro4.Proxy("PYRONAME:examplo.ppd")    # use name server object lookup uri shortcut
print(greeting_maker.get_salario(nome, cargo, salario))