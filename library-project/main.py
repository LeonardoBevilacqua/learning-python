from models.actor import Actor
from models.book import Book
from os import system

actors = []
books = []

def menu():
    opcao = None
    while opcao != 0:
        clean_screen()
        print("1. Cadastrar ator")
        print("2. Listar atores")
        print("3. Cadastrar livro")
        print("4. Listar livros")
        print("5. Listar atores e seus livros")
        print("0. Sair")
        opcao = int(input())

        clean_screen()
        match opcao:
            case 1:
                add_actor()
            case 2:
                list_actors()
            case 3:
                add_book()
            case 4:
                list_books()
            case 5:
                list_actors_and_books()

def add_actor():
    name = input("Nome: ")
    actor = Actor(len(actors) + 1, name)
    actors.append(actor)
    input(". . . continuar")

def list_actors():
    for actor in actors:
        print(actor.__str__())
    input(". . . continuar")

def add_book():
    name = input("Nome: ")
    actor_id = int(input("Codigo do ator: "))
    book = Book(len(books) + 1, name, actor_id)
    books.append(book)
    input(". . . continuar")

def list_books():
    for book in books:
        print(book.__str__())
    input(". . . continuar")

def list_actors_and_books():
    for actor in actors:
        print(actor.__str__())
        for book in books:
            if book.actor_id == actor.id:
                print(book.__str__())
        print("===//===")
    input(". . . continuar")

def clean_screen():
    system('clear')

menu()
