import sqlite3

# ==========================================
# CLASSE DE MODELO (A Entidade)
# ==========================================
class Aluno:
    def __init__(self, nome, idade, curso, id_aluno=None):
        self.id = id_aluno 
        self.nome = nome
        self.idade = idade
        self.curso = curso

    def __str__(self):
        return f"ID: {self.id} | Nome: {self.nome} | Idade: {self.idade} | Curso: {self.curso}"

# ==========================================
# CLASSE DAO (Data Access Object)
# ==========================================
class AlunoDAO:
    def __init__(self, nome_banco="banco_escola.db"):
        self.nome_banco = nome_banco
        self._criar_tabela_se_nao_existe()

    def _conectar(self):
        return sqlite3.connect(self.nome_banco)

    def _criar_tabela_se_nao_existe(self):
        with self._conectar() as conexao:
            cursor = conexao.cursor()#o executar do cursor vai criar a tabela alunos, caso ela ainda não exista. Se já existir, ele ignora.
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS alunos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    idade INTEGER NOT NULL,
                    curso TEXT NOT NULL
                )
            ''')
            conexao.commit()# o commit vai executar a criação da tabela, se ela não existir. Se já existir, não faz nada.

    def inserir(self, aluno):
        with self._conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute('''
                INSERT INTO alunos (nome, idade, curso) 
                VALUES (?, ?, ?)
            ''', (aluno.nome, aluno.idade, aluno.curso))
            aluno.id = cursor.lastrowid
            conexao.commit()
            print(f"\n[OK] Aluno(a) '{aluno.nome}' inserido com sucesso!")

    def buscar_todos(self):
        with self._conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute('SELECT id, nome, idade, curso FROM alunos')
            linhas = cursor.fetchall()# o fetchall() vai pegar todas as linhas retornadas pela consulta SELECT e armazená-las na variável 'linhas'. Cada linha é uma tupla representando um registro da tabela 'alunos'.
            
            lista_alunos = []
            for linha in linhas:
                aluno = Aluno(id_aluno=linha[0], nome=linha[1], idade=linha[2], curso=linha[3])
                lista_alunos.append(aluno)
            return lista_alunos

    def atualizar(self, aluno):
        with self._conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute('''
                UPDATE alunos 
                SET nome = ?, idade = ?, curso = ? 
                WHERE id = ?
            ''', (aluno.nome, aluno.idade, aluno.curso, aluno.id))
            conexao.commit()
            print(f"\n[Atualizado] Dados de '{aluno.nome}' atualizados!")

    def deletar(self, id_aluno):
        with self._conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute('DELETE FROM alunos WHERE id = ?', (id_aluno,))
            conexao.commit()
            print(f"\n[Deletado] Aluno com ID {id_aluno} foi removido.")