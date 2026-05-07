from DAO import LivroDAO
from modelo import Livro


def menu_principal():
    print("==="*30)
    print("Bem-vindo à Biblioteca!")
    print("1. Adicionar Livro")
    print("2. Listar Livros")
    print("3. Atualizar Livro")
    print("4. Deletar Livro")
    print("5. Sair")
    print("==="*30)

def main():
    dao = LivroDAO()
    while True:
        menu_principal()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            titulo = input("Título: ")
            autor = input("Autor: ")
            ano_publicacao = int(input("Ano de Publicação: "))
            genero = input("Gênero: ")
            livro = Livro(titlo=titulo, autor=autor, ano_publicacao=ano_publicacao, genero=genero)
            dao._inserir(livro)

        elif escolha == '2':
            livros = dao.buscar_todos()
            for livro in livros:
                print(livro)

        elif escolha == '3':
            id_atualizar = int(input("ID do livro a atualizar: "))
            titulo = input("Novo Título: ")
            autor = input("Novo Autor: ")
            ano_publicacao = int(input("Novo Ano de Publicação: "))
            genero = input("Novo Gênero: ")
            livro_atualizado = Livro(titlo=titulo, autor=autor, ano_publicacao=ano_publicacao, genero=genero, id=id_atualizar)
            dao.atualizar(livro_atualizado) 

        elif escolha == '4':
            id_deletar = int(input("ID do livro a deletar: "))
            dao.deletar(id_deletar)

        elif escolha == '5':
            print("Saindo da Biblioteca. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()