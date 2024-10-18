import pandas as pd
import os
import sqlite3

conn = sqlite3.connect('db.sqlite3')

caminho_atual = os.getcwd()
caminho_final = caminho_atual.replace('\\', '/')

data_frame = pd.read_csv(caminho_final+'/data/ferramentas.csv')

data_frame.columns =['tituloProduto','preco','descricao',
                     'imgProduto','catProduto',
                     'classProduto','exibirHome']

data_frame.to_sql('api_produto', conn, if_exists='append', index=False)

conn.close()

print('Dados inseridos com sucesso!!')