# Questão 12:

class aluno:
    def __init__(self, nome, nota_1, nota_2):
        self.nome = nome
        self.nota_1 = nota_1
        self.nota_2 = nota_2

    def calcula_media(self):
        return (self.nota_1 + self.nota_2) / 2

    def mostra_dados(self):
        print('\nNome: {}'.format(self.nome))
        print('Primeira nota: {}'.format(self.nota_1))
        print('Segunda nota: {}'.format(self.nota_2))
        print('Média: {:.1f}'.format(self.calcula_media()))

    def resultado(self):
        if self.calcula_media() >= 6.0:
            print('\n{} está aprovado(a)'.format(self.nome))
        else:
            print('\n{} está reprovado(a)'.format(self.nome))

aluno_1 = aluno('Fulano', 6.0, 9.0)
aluno_2 = aluno('Cicrano', 3.0, 4.5)

print('Dados do primeiro aluno(a):')
aluno_1.mostra_dados()
aluno_1.resultado()

print('')
print('')
print('')

print('\nDados do segundo aluno(a):')
aluno_2.mostra_dados()
aluno_2.resultado()
