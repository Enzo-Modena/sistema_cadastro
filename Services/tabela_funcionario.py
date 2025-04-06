# Services/tabela_vendedor.py
import sqlite3

conexao = sqlite3.connect("Empresa.db")

cursor = conexao.cursor()

cursor.execute(
    '''
        CREATE TABLE funcionario (
            codigo INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            tipo TEXT NOT NULL,  -- 'FreeLancer' ou 'Vendedor'
            diasTrabalhados INTEGER,  -- Apenas para FreeLancer
            valorDia REAL,            -- Apenas para FreeLancer
            salarioBase REAL,         -- Apenas para Vendedor
            comissao REAL             -- Apenas para Vendedor
);
    '''
)

cursor.close()
print("Tabela FUNCIONÁRIO criada com sucesso!")