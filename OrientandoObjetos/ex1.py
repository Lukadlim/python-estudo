from ex1Classe import Personagem

heroi = Personagem('Silver', 1000, 200)
vilao = Personagem('Darkrey', 2000, 50)

heroi.abrirbau()
while vilao.hp != 0:
    print(f'{heroi.nome} deixou {vilao.nome} com {heroi.atacar(vilao)} de hp')

    if vilao.hp == 0:
        print(f'{vilao.nome} faleceu')
        heroi.abrirbau()
