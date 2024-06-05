from models.actor import Actor
from models.book import Book
from os import system

a = Actor(1, "test")

actors = [a]

def menu():
    opcao = None
    while opcao != 0:
        system('clear')
        print("1. Cadastrar X")
        print("2. Listar X")
        print("0. Sair")
        opcao = int(input())

        if opcao == 2:
            list_actors()

def list_actors():
    for actor in actors:
        print(actor.__str__())
    input(". . . continuar")

menu()
