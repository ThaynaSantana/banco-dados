# Exercício 1: Criar um Banco de Dados e Tabela
# Crie um banco de dados SQLite chamado "exercicio.db" e dentro dele crie uma tabela chamada "alunos" com os campos "id" (inteiro, chave primária) e "nome" (texto).
import sqlite3
conexao = sqlite3.connect('exercicio')
cursor = conexao.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS alunos(
               id INTENGER PRIMARY KEY,
               nome TEXT
    );
''')

# Exercício 2: Inserir Dados
# Escreva um programa Python para inserir três registros na tabela "alunos" com os seguintes dados: (1, "João"), (2, "Maria"), (3, "Pedro").
cursor.execute('''
    INSERT INTO alunos(id,nome) VALUES(1, "João")
    INSERT INTO alunos(id,nome) VALUES(2, "Maria")
    INSERT INTO alunos(id,nome) VALUES(3, "Pedro");
''')
# Exercício 3: Consulta Simples
# Escreva uma consulta SQL para selecionar todos os registros da tabela "alunos".
cursor.execute('''
    SELECT * FROM alunos;
''')
# Exercício 4: Consulta com Condição
# Escreva uma consulta SQL para selecionar o nome do aluno com id = 2.
cursor.execute('''
    SELECT nome FROM alunos WHERE id=2;
''')
# Exercício 5: Atualização de Dados
# Escreva um programa Python para atualizar o nome do aluno com id = 3 para "Carlos".
cursor.execute('''
    UPDATE alunos SET nome="Carlos" WHERE id=3;
''')
# Exercício 6: Exclusão de Dados
# Escreva um programa Python para excluir o aluno com id = 1 da tabela.
cursor.execute('''
    DELETE FROM alunos WHERE id=1
''')
# Exercício 7: Consulta com Junção de Tabelas
# Crie outra tabela chamada "notas" com os campos "aluno_id" (inteiro, chave estrangeira referenciando id da tabela "alunos") e "nota" (inteiro).
cursor.execute('''
    CREATE TABLE notas(
               aluno_id INTENGER FOREIGN KEY REFERENCES alunos (id) NOT NULL,
               nota INTENGER
    );
''')
# Insira algumas notas para os alunos existentes na tabela "alunos".
cursor.execute('''
    INSERT INTO notas(aluno_id,nota) VALUES(1, 5)
    INSERT INTO notas(aluno_id,nota) VALUES(2, 7)
    INSERT INTO notas(aluno_id,nota) VALUES(3, 8)
''')
# Escreva uma consulta SQL para selecionar o nome do aluno e sua nota correspondente.
cursor.execute('''
    SELECT * FROM alunos
''')
# Exercício 8: Transações
# Escreva um programa Python que realize uma transação para inserir um novo aluno e sua nota correspondente na tabela "alunos" e "notas". Garanta que a transação seja realizada com sucesso ou revertida em caso de falha.
cursor.execute('''
    BEGIN
               
    COMMIT
''')
# Exercício 9: Consulta com Funções Agregadas
# Escreva uma consulta SQL para calcular a média das notas dos alunos.

print('nao sei :(')

# Exercício 10: Desafio de Desempenho
# Crie uma tabela com uma grande quantidade de dados (por exemplo, 100.000 registros). Realize consultas de seleção e atualização para medir o desempenho da sua implementação.

print('não sei :(')