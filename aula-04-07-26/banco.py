import sqlite3
from classe import Aluno

class AlunoDAO:
    def __init__(self, nome_banco = "banco_aluno.db"):
        self.nome_banco = nome_banco
        self._criar_tabela_se_nao_existe()

    def _conectar(self):
        return sqlite3.connect(self.nome_banco)

    def _criar_tabela_se_nao_existe(self):
        with self._conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute(
                '''
                CREATE TABLE IF NOT EXISTS alunos(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    idade INTEGER NOT NULL,
                    curso TEXT NOT NULL
                )
                '''
            )
            conexao.commit()
    
    def inserir(self, aluno):
        with self._conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute('''
                INSERT INTO alunos(nome, idade, curso)
                VALUES(?, ?, ?)
            ''', (aluno.nome, aluno.idade, aluno.curso)
            )
            conexao.commit()
            print(f"[OK] Aluno(a) '{aluno.nome}' inserido com  sucesso")
    
    def buscar_todos(self):
        with self._conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute('SELECT id, nome, idade, curso FROM alunos')
            linhas = cursor.fetchall()

            lista_alunos =[]
            for linha in linhas:
                aluno  = Aluno(id_aluno = linha[0], nome = linha[1], idade = linha[2], curso = linha[3])
                lista_alunos.append(aluno)

            return lista_alunos


