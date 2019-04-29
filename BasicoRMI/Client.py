'''
Created on 25 de abr de 2019

@author: lsrodrigues
'''
import Pyro4

name = input("What is your name? ").strip()
cargo = input("What is your name? ").strip()
salario = input("What is your name? ").strip()

'''
greeting_maker = Pyro4.Proxy("PYRONAME:example.greeting")    # use name server object lookup uri shortcut
print(greeting_maker.get_fortune(name))
'''
    
greeting_maker = Pyro4.Proxy("PYRONAME:example.ppd")    # use name server object lookup uri shortcut
print(greeting_maker.get_salario(name, cargo, salario))