# Professor OpenIA
# Considerando o esforço e a abordagem demonstrados nos exercícios apresentados, eu atribuiria uma nota de 8,5. Você demonstrou compreensão dos conceitos básicos de manipulação de banco de dados SQLite e Python, e foi capaz de completar a maioria dos exercícios com sucesso. No entanto, alguns erros foram cometidos, como o esquecimento de adicionar ponto e vírgula em algumas instruções SQL e a omissão dos exercícios 9 e 10. Ainda assim, sua dedicação em aprender e realizar os exercícios é evidente. Continue praticando e explorando mais conceitos para aprimorar suas habilidades!

# Nota: 8,5

# CORREÇÃO!!!

# - Adicionei uma extensão .db ao nome do banco de dados no momento da conexão.
# - No Exercício 2, adicionei ponto e vírgula após cada instrução INSERT INTO.
# - No Exercício 7, corrigi o tipo de dados das colunas aluno_id e nota para INTEGER.
# - Adicionei instruções de BEGIN e COMMIT para a transação no Exercício 8.

import sqlite3

# Exercício 1: Criar um Banco de Dados e Tabela
conexao = sqlite3.connect('exercicio.db')
cursor = conexao.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS alunos(
               id INTEGER PRIMARY KEY,
               nome TEXT
    );
''')

# Exercício 2: Inserir Dados
# cursor.execute('''
#     INSERT INTO alunos(id, nome) VALUES(1, "João");
# ''')
# cursor.execute('''
#     INSERT INTO alunos(id, nome) VALUES(2, "Maria");
# ''')
# cursor.execute('''
#     INSERT INTO alunos(id, nome) VALUES(3, "Pedro");
# ''')

# Depois da minha sugestão de não precisar de TRÊS EXECUTES, ele disse que pode sim, desta forma:
# Exercício 2: Inserir Dados
cursor.execute('''
    INSERT INTO alunos(id, nome) VALUES(1, "João"),
                                      (2, "Maria"),
                                      (3, "Pedro");
''')


# Exercício 3: Consulta Simples
cursor.execute('''
    SELECT * FROM alunos;
''')
print(cursor.fetchall())

# Exercício 4: Consulta com Condição
cursor.execute('''
    SELECT nome FROM alunos WHERE id=2;
''')
print(cursor.fetchone())

# Exercício 5: Atualização de Dados
cursor.execute('''
    UPDATE alunos SET nome="Carlos" WHERE id=3;
''')

# Exercício 6: Exclusão de Dados
cursor.execute('''
    DELETE FROM alunos WHERE id=1;
''')

# Exercício 7: Consulta com Junção de Tabelas
cursor.execute('''
    CREATE TABLE IF NOT EXISTS notas(
               aluno_id INTEGER,
               nota INTEGER
    );
''')
cursor.execute('''
    INSERT INTO notas(aluno_id, nota) VALUES(1, 5);
''')
cursor.execute('''
    INSERT INTO notas(aluno_id, nota) VALUES(2, 7);
''')
cursor.execute('''
    INSERT INTO notas(aluno_id, nota) VALUES(3, 8);
''')
cursor.execute('''
    SELECT alunos.nome, notas.nota FROM alunos JOIN notas ON alunos.id = notas.aluno_id;
''')
print(cursor.fetchall())

# Exercício 8: Transações
cursor.execute('''
    BEGIN;
    INSERT INTO alunos(id, nome) VALUES(4, "Ana");
    INSERT INTO notas(aluno_id, nota) VALUES(4, 9);
    COMMIT;
''')

# Exercício 9: Consulta com Funções Agregadas
# Escreva uma consulta SQL para calcular a média das notas dos alunos.
cursor.execute('''
    SELECT AVG(nota) AS media_notas FROM notas;
''')

# Exercício 10: Desafio de Desempenho
# Crie uma tabela com uma grande quantidade de dados (por exemplo, 100.000 registros). Realize consultas de seleção e atualização para medir o desempenho da sua implementação.
cursor.execute('''
    for i in range(100000):
    cursor.execute('INSERT INTO tabela_exemplo (coluna1, coluna2) VALUES (?, ?)', (valor1, valor2))
''')

# ~ Depois de criar os registros, você pode medir o desempenho de consultas de seleção e atualização utilizando a biblioteca time em Python para medir o tempo decorrido antes e depois da execução das consultas. Por exemplo, para medir o tempo decorrido para uma consulta de seleção:
import time

inicio = time.time()
cursor.execute('SELECT * FROM tabela_exemplo;')
registros = cursor.fetchall()
fim = time.time()

tempo_decorrido = fim - inicio
print("Tempo decorrido:", tempo_decorrido, "segundos")


conexao.close()
