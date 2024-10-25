import sqlite3

class Eccomerce:
    def __init__(self, db='db.sqlite3'):
        self.conn = sqlite3.connect(db)
        self.menu()

    def menu(self):
        while True:
            print("\n"
                '[1] - Create\n'
                '[2] - Read\n'
                '[3] - Update\n'
                '[4] - Delete\n'
                '[5] - Exit\n'
                )
            op = input("Escolha uma opção: ")

            match op:
                case '1':
                    print("Crate")
                case '2':
                    print("Read")
                case '3':
                    print("Update")
                case '4':
                    print("Delete")
                case '5':
                    break
                case _:
                    print("Escolha uma opção correta")

    def create(self,
               tituloProduto,
               preco,
               descricao,
               imgProduto,
               catProduto,
               classProduto,
               exibirHome,
               ):
        pass

home = Eccomerce()