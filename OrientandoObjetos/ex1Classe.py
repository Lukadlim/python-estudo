from random import randint


class Personagem:
    def __init__(self, nome, hp, atk):
        self.nome = nome
        self.hp = hp
        self.atk = atk

    def atacar(self, quem):
        quem.hp -= self.atk
        return quem.hp

    @staticmethod
    def abrirbau():
        resp = randint(1, 2)
        if resp == 1:
            print('Parabens voce ganhou uma arma')
        else:
            print('Ganhou poha nenhuma')