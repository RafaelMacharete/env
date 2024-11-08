import sqlite3
import pandas as pd

class Ecommerce():
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
                    self.menu_create()
                case '2':
                    self.read()
                case '3':
                    print("Update")
                case '4':
                    self.delete()
                case '5':
                    break
                case _:
                    print("Escolha uma opção correta")

    def create(self,
               titulo,
               preco,
               descricao,
               image,
               cat,
               classif,
               exibir
               ):
        cursor = self.conn.cursor()
        cursor.execute('''
               INSERT INTO api_produto(
               tituloProduto,
               preco,
               descricao,
               imgProduto,
               catProduto,
               classProduto,
               exibirHome)
               VALUES(?,?,?,?,?,?,?)''',
               (titulo,
                preco,
                descricao,
                image,
                cat,
                classif,
                exibir))
        self.conn.commit()
        print('Produto criado com sucesso...')
    
    def menu_create(self):
        print('\n'
              '[1]-Titulo\n'
              '[2]-Preco\n'
              '[3]-Descricao\n'
              '[4]-Imagem\n'
              '[5]-Categoria\n'
              '[6]-Classificação\n'
              '[7]-Exibir\n'
              )

        titulo = input('Titulo: ')
        preco = float(input('Preço: '))
        descricao = input('Descrição: ')
        img = input('Imagem: ')
        cat = input('Categoria: ')
        classif = input('Classificação :')
        exibir = input('Exibir: ')
        self.create(titulo,
               preco,
               descricao,
               img,
               cat,
               classif,
               exibir)
        
    def read(self):
        print('\n'
              '[1]-Lista todos os produtos\n'
              '[2]-Listar por ID\n'
              '[3]-Listar por Título\n'
              )
        op = int(input("Escolha a opção:"))
        match op:
            case 1:
                df = pd.read_sql_query("SELECT * FROM api_produto", self.conn)
                return print(df)
            case 2:
                valor = int(input('ID: '))
                query = f"SELECT * FROM api_produto WHERE id = {valor}"
                df = pd.read_sql_query(query, self.conn)
                return print(df)
            case 3:
                valor = input("Título: ")
                query = f"SELECT * FROM api_produto WHERE tituloProduto = {valor}"
                df = pd.read_sql_query(query, self.conn)
                return print(df)
            case _:
                print('Escolha uma opção válida...')

    def delete(self):
        print('\n'
              '[1]-Apagar todos os produtos\n'
              '[2]-Apagar por ID\n'
              '[3]-Apagar por Título\n'
              )
        op = int(input("Escolha a opção:"))
        match op:
            case 1:
                valor = int(input('Exibir Home: '))
                df = pd.read_sql_query(f"DELETE FROM api_produto WHERE exibirHome = {valor}", self.conn)
                return print(df)
            case 2:
                valor = int(input('ID: '))
                query = f"SELECT * FROM api_produto WHERE id = {valor}"
                df = pd.read_sql_query(query, self.conn)
                return print(df)
            case 3:
                valor = input("Título: ")
                query = f"SELECT * FROM api_produto WHERE tituloProduto = {valor}"
                df = pd.read_sql_query(query, self.conn)
                return print(df)
            case _:
                print('Escolha uma opção válida...')
home = Ecommerce()