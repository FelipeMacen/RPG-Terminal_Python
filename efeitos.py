from combate import *
from abc import ABC

class Efeitos(ABC):
    def __init__(self, nome, duracao, tipo):
        self.nome = nome
        self.duracao = duracao
        self.tipo = tipo

class Defensor(Efeitos):
    def __init__(self, duracao):
        super().__init__("Defensor", duracao, "Buff")

    def aplicar(self, afetado, dscrt=None):
        if self.duracao == 1:
            afetado.defesa /= 1.3

class Luz(Efeitos):
    def __init__(self, duracao):
        super().__init__("Filho da Luz", duracao, "Buff")

    def aplicar(self, principal = None, inimigo = None):
        turno_jogador(principal, inimigo)

class Furia(Efeitos):
    def __init__(self, duracao):
        super().__init__("Furia Demoniaca", duracao, "Buff")

    def aplicar(self,afetado, dscrt=None):
        afetado.danobase *= 1.5

    def atualizar(self, afetado):
        afetado.danobase /= 1.5

class Territorio(Efeitos):
    def __init__(self, duracao):
        super().__init__("Territorio", duracao, "Buff")

    def aplicar(self,inimigo,principal):
        inimigo.curabase *= 1.5
        inimigo.danobase *= 1.5

    def atualizar(self, afetado):
        afetado.danobase /= 1.5
        afetado.curabase /= 1.5


class Afogamento(Efeitos):#tentar implementar depois
    def __init__(self):
        super().__init__("Afogamento", 1, "Debuff")

    def aplicar(self, afetado):
        afetado.vida -= 10

class Atordoado(Efeitos):#cavaleiro e mercenario
    def __init__(self, duracao):
        super().__init__("Atordoado", duracao, "Debuff")

    def aplicar(self,inimigo,dscrt=None):
        #diminuir o dano do inimigo as proximas rodadas
        inimigo.danobase *= 0.6

    def atualizar(self, inimigo):
        inimigo.danobase /= 0.6

class Paralizado(Efeitos):
    def __init__(self, duracao):
        super().__init__("Paralizado", duracao, "Debuff")

    def aplicar(self, inimigo = None, principal = None):
        pass


class Perdido(Efeitos):
    def __init__(self):
        super().__init__("Lost", 3, "Debuff")

    def aplicar(self, personagem = None, inimigo = None):
        while True:
            personagem.vida -= 5
            exibe(f"{personagem.nome} recebe [red]5 de dano[/] por estar preso na ilusão de Curupira.")
            enter()
            exibe(f"{personagem.nome} vai tentar escapar da ilusão..", personagem)
            sleep(0.8)

            if personagem.vida <= 0:
                return

            if self.duracao < 3:
                if randint(0,1) == 1:
                    exibe(f"[green]Sucesso![/]{personagem.nome} [blue]recobra os sentidos[/]", personagem)
                    self.duracao = 0
                    enter()
                    return
            exibe("[red]Fracasso![/] Turno inimigo:")
            enter()
            turno_inimigo(personagem, inimigo)
            self.duracao -= 1