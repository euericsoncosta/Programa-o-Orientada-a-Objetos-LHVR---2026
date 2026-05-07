import sqlite3
from modelo import Livro

#  inserir, buscar_todos, atualizar e deletar


class LivroDAO:
    def __init__(self, db_name = "Biblioteca.db"):
        self.db_name = db_name
        self._criar_taabela_se_nao_existir()

    def _criar_taabela_se_nao_existir(self):
        with sqlite3.connect(self.db_name) as conexao:
            cursor = conexao.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS livros (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT NOT NULL,
                    autor TEXT NOT NULL,
                    ano_publicacao INTEGER NOT NULL,
                    genero TEXT NOT NULL
                )
            ''')
            conexao.commit()

    def _inserir(self, livro):
        with sqlite3.connect(self.db_name) as conexao:
            cursor = conexao.cursor()
            cursor.execute('''
                INSERT INTO livros (titulo, autor, ano_publicacao, genero)
                VALUES (?, ?, ?, ?)
            ''', (livro.titulo, livro.autor, livro.ano_publicacao, livro.genero))
            conexao.commit()
            print("Livro inserido com sucesso!")

    def buscar_todos(self):
        with sqlite3.connect(self.db_name) as conexao:
            cursor = conexao.cursor()
            cursor.execute('SELECT * FROM livros')
            linhas = cursor.fetchall()
            livros = []
            for linha in linhas:
                livro = Livro(id=linha[0], titlo=linha[1], autor=linha[2], ano_publicacao=linha[3], genero=linha[4])
                livros.append(livro)
            return livros
        
    def atualizar(self, livro):
        with sqlite3.connect(self.db_name) as conexao:
            cursor = conexao.cursor()
            cursor.execute('''
                UPDATE livros
                SET titulo = ?, autor = ?, ano_publicacao = ?, genero = ?
                WHERE id = ?
            ''', (livro.titulo, livro.autor, livro.ano_publicacao, livro.genero, livro.id))
            conexao.commit()
            print("Livro atualizado com sucesso!")

    def deletar(self, livro_id):
        with sqlite3.connect(self.db_name) as conexao:
            cursor = conexao.cursor()
            cursor.execute('DELETE FROM livros WHERE id = ?', (livro_id,))
            conexao.commit()
            print("Livro deletado com sucesso!")