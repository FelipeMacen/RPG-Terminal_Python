from efeitos import *
from abc import abstractmethod


class Inimigos(ABC):
    def __init__(self, nome, danobase):
        self.nome = nome
        self.vida = 100
        self.curabase = 20
        self.danobase = danobase
        self.defesa = 30
        self.ataques = {}
        self.habilidades = {}
        self.carrega = 0
        self.efeitos = []

    @abstractmethod
    def curar(self):
        pass

    @abstractmethod
    def atacar(self, inimigo):
        pass

    def atualizar_efeito(self):
        for efeito in self.efeitos:
            efeito.duracao -= 1
            try:
                efeito.atualizar(self)
            except:
                pass

        self.efeitos = [
            efeito for efeito in self.efeitos if efeito.duracao > 0
        ]

    @abstractmethod
    def hability(self,principal):
        pass

class Minotauro(Inimigos):
    def __init__(self):
        super().__init__("Minotauro", 30)
        self.ataques = {"Soco Pesado":1, "Coice Duplo":1, "Lançardor Subterraneo":1}
        self.habilidades = {"Chife Demoníaco": 44, "Furia Divina":10}
        #investida para chifrar o inimigo
        #furia divina: os proximos 3 ataques dele terão +50% de dano.

    def atacar(self, inimigo):
        sorteado = randint(0, 2)

        exibe(f"[red]Minotauro[/] escolheu [red]{list(self.ataques.keys())[sorteado]}[/]", self, sorteado)
        dmg = dano(self, inimigo, sorteado)
        return dmg

    def curar(self):
        if self.vida < 100:
            sorteado = randint(20, 25)
            if self.vida + sorteado > 100:
                self.vida = 100
                exibe(f"[red]{self.nome}[/] atingiu a [red]vida maxima[/] (100 de vida)", self)
                return
            self.vida += sorteado
            exibe(f"[red]Minotauro[/] recuperou [green]{sorteado}[/] pontos de vida", sorteado)
        else:
            exibe("vida no maximo irmaozao")

        return

    def hability(self, principal):
        sorteado = randint(0,1)
        exibe(f"Habilidade Escolhida: [red]{list(self.habilidades.keys())[sorteado]}[/]", self, sorteado)
        if sorteado == 0:
            exibe(f"[red]Minotauro[/] começa a correr como um touro na direção de {principal.nome},"
                  f" acertando-lhe uma [red]chifrada em cheio[/]", principal, time=0.02)
            exibe(f"[blue]{principal.nome}[/] ficará [red]atordoado por 2 rodadas[/]", principal, time=0.02)
            principal.efeitos.append(Atordoado(2))
        if sorteado == 1:
            exibe("[red]Minotauro solta um grito ensurdecedor[/]...")
            exibe("[red]Minotauro[/] recebeu o efeito [red]Fúria[/] por 3 rodadas")
            self.efeitos.append(Furia(3))

class Curupira(Inimigos):
    def __init__(self):
        super().__init__("Curupira", 30)
        self.ataques = {"Chute Trocado": 1, "Investida Furiosa": 1, "Chicote de Cipó":1}
        self.habilidades = { "Pai Natureza":44, "Confusão Mental": 35}

    def atacar(self, inimigo):
        sorteado = randint(0, 2)

        exibe(f"[red]Curupira[/] escolheu [red]{list(self.ataques.keys())[sorteado]}[/]", self, sorteado)
        dmg = dano(self, inimigo, sorteado)
        return dmg

    def curar(self):
        if self.vida < 100:
            sorteado = randint(20, 25)
            if self.vida + sorteado > 100:
                self.vida = 100
                exibe(f"[red]{self.nome}[/] atingiu a [red]vida maxima[/] (100 de vida)", self)
                return
            self.vida += sorteado
            exibe(f"[red]Curupira[/] recuperou [green]{sorteado}[/] pontos de vida", sorteado)
        else:
            exibe("vida no maximo irmaozao")

        return

    def hability(self, principal):
        sorteado = randint(0,1)
        exibe(f"Habilidade Escolhida: [red]{list(self.habilidades.keys())[sorteado]}[/]", self, sorteado)
        if sorteado == 0:
            exibe(f"[red]Curupira[/] toca o berrante e chama uma [red]enxurrada de animais[/] para atacar {principal.nome}", principal, time=0.02)
            exibe(f"[blue]{principal.nome}[/] recebe [red]40 pontos de dano[/] e ficará [red]atordoado[/] por 2 rodadas")
            principal.vida -= 40
            principal.efeitos.append(Atordoado(2))
        if sorteado == 1:
            exibe("De repente, você começa a ouvir um [red]assobio hipnotizante..[/]")
            exibe(f"[blue]{principal.nome}[/] está preso na ilusão de curupira \n"
                  f"(ficando impossibilitado de fazer ações até escapar da ilusão).", principal)
            principal.efeitos.append(Perdido())
        return

class Nessie(Inimigos):
    def __init__(self):
        super().__init__("Nessie", 30)
        self.ataques = {"Martelo de Cauda":1, "Tiro de Água":1, "Mordida Feroz": 1}
        self.habilidades = { "Canhão de Água": 44, "Território": 0}
        #territorio: tentar levar o inimigo para o fundo do mar. Os ataques do nessie ficariam muito mais fortes
        #e o do principal muito mais fracos

    def atacar(self, inimigo):
        sorteado = randint(0, 2)

        exibe(f"Nessie escolheu {list(self.ataques.keys())[sorteado]}", self, sorteado)
        dmg = dano(self, inimigo, sorteado)
        return dmg

    def curar(self):
        if self.vida < 100:
            if self.vida < 100:
                sorteado = randint(20, 25)
                if self.vida + sorteado > 100:
                    self.vida = 100
                    exibe(f"[red]{self.nome}[/] atingiu a [red]vida maxima[/] (100 de vida)", self)
                    return
                self.vida += sorteado
                exibe(f"[red]Nessie[/] recuperou [green]{sorteado}[/] pontos de vida", sorteado)
            else:
                exibe("vida no maximo irmaozao")

            return

    def hability(self, principal):
        sorteado = randint(0,1)
        exibe(f"Habilidade Escolhida: [red]{list(self.habilidades.keys())[sorteado]}[/]", self, sorteado)
        if sorteado == 0:
            exibe(f"[red]Nessie[/] prepara um [red]jato de água compressurizada[/] e atira na direção de {principal.nome}", principal)
            exibe(f"{principal.nome} recebe [red]40 pontos de dano[/] e ficará [red]atordoado[/] por 2 rodadas.")
            principal.vida -= 40
            principal.efeitos.append(Atordoado(2))
        if sorteado == 1:
            exibe("[red]Nessie te abocanha[/] e num rapido movimento te leva para [red]debaixo da água[/].")
            exibe(f"[red]Nessie tem aumento de ataque e cura[/] por 3 turnos")
            self.efeitos.append(Territorio(3))
        return