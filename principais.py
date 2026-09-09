from efeitos import *
from abc import abstractmethod

class Personagem(ABC):
    def __init__(self, nome, defesa, danobase):
        self.nome = nome
        self.vida = 100
        self.defesabase = defesa
        self.defesa = defesa
        self.danobase = danobase
        self.equipamentos = {}
        self.ataques = {}
        self.habilidades = {}
        self.inventario = {}
        self.carrega = 0
        self.efeitos = []
        self.dinheiro = 0

    def atualiza_defesa(self):
        self.defesa = self.defesabase

    def mapa(self):
        exibe(
            f"{' ' * 38}?\n"
            f"\n{' '*18}/{' '* 19}|{' '*18}{chr(92)}"
            f"\nLAGO DO ESQUECIMENTO{' '*8}FLORESTA DA PERDIÇÃO{' '*8}CAVERNA LABIRÍNTICA\n"
            f"[bright_white]{' '*21} {chr(92)}{' '*15}|{' '*17}/[/]\n\n"
            f"{' '* 32}VILA INICIAL"
        , time=0)
        enter()
        return

    def curar(self):
        if self.vida < 100:
            if self.vida + 30 > 100:
                self.vida = 100
                return f"{self.nome} usou {list(self.inventario.keys())[1]} e ficou com 100 de vida"
            self.vida += 30
            return f"{self.nome} usou {list(self.inventario.keys())[1]} e recuperou 30 pontos de vida."
        else:
            exibe(f"Vida no maximo")
            return "cancel"


    @abstractmethod
    def hability(self, inimigo):
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



class Cavaleiro(Personagem):
    def __init__(self, nome, defesa, danobase):
        super().__init__(nome, defesa, danobase)
        self.vida = 100
        self.equipamentos = {"Espada": "descrição", "Escudo":"descrição"}
        self.ataques = {"Ataque Com Espada": 0.9, "Aparo": 0.9, "Esquiva": 0}
        self.habilidades = {"Ataque Pesado":"descrição", "Bloqueio Com Escudo":"descrição"}
        self.inventario = {"Mapa":1, "Ataduras":2}


    def hability(self, inimigo):
        conteudo = "\nQual habilidade especial deseja usar?\n[0]Sair\n"
        for i, k in enumerate(self.habilidades.keys()):
            conteudo += f"[[bright_white]{i + 1}[/]]{k}\n"
        while True:
            exibe(conteudo, time=0.02)
            try:
                atk = int(input())
            except:
                continue
            else:
                if 0 <= atk < 3:
                    if atk == 0:
                        exibe("saindo..")
                        return "cancel"
                    if atk == 1:
                        inimigo.vida -= 40
                        exibe("Habilidade escolhida: [red]Ataque Pesado[/]")
                        exibe(f"[red]{inimigo.nome}[/] recebeu [red]40[/] de dano e ficará [red]atordoado[/]"
                              f" por 3 rodadas", inimigo)
                        inimigo.efeitos.append(Atordoado(3))
                        break
                    elif atk == 2:
                        exibe("Habilidade Escohida: [blue]Bloqueio com Escudo[/] pelas proximas"
                              " 3 rodadas a [blue]defesa é aumentada em 30%[/]")
                        self.defesa *= 1.3
                        self.efeitos.append(Defensor(3))
                        break
        return


class Mago(Personagem):
    def __init__(self, nome, defesa, danobase):
        super().__init__(nome, defesa, danobase)
        self.vida = 100
        self.equipamentos = {"Livro de Feitiços":"descrição", "Cajado Mágico":"descrição",}
        self.ataques = {"Ataque Com Cajado":0.9, "Bola de Fogo":0.9, "Teletransporte":0}
        self.habilidades = {"Tempestade de Relâmpagos": "descrição", "Invocação Amiga": "descrição"}
        self.inventario = {"Mapa":1, "Poções de cura":2}
        self.dragao = None

    def hability(self, inimigo):
        conteudo = "\nQual habilidade especial deseja usar?\n[0]Sair\n"
        for i, k in enumerate(self.habilidades.keys()):
            conteudo += f"[[bright_white]{i + 1}[/]]{k}\n"
        while True:
            exibe(conteudo, time=0.02)
            try:
                atk = int(input())
            except:
                continue
            else:
                if 0 <= atk < 3:
                    if atk == 0:
                        exibe("saindo..")
                        return "cancel"
                    exibe(f"Habilidade Escolhida: [purple]{list(self.habilidades.keys())[atk-1]}[/]", self)
                    if atk == 1:
                        inimigo.vida -= 40

                        exibe(f"[purple]Núvens negras[/] cobrem o céu..\n[purple]Diversos relâmpagos[/]"
                              f" de repente caem sobre "
                              f"[red]{inimigo.nome}[/], que recebe [red]40[/] de dano e ficará [red]paralizado[/]"
                              f"(1 ou 2 turnos)", self, inimigo)
                        inimigo.efeitos.append(Paralizado(randint(1,2)))
                        return 0
                    elif atk == 2:
                        self.ctrlinvoc()
                        exibe("[purple]Bebê Dragão[/] foi invocado! \nEle pode"
                              " [purple]atacar o inimigo[/] ou [purple]curar o mago[/] por 2 rodadas")
                        return 0

    def ctrlinvoc(self):
        if self.dragao == None:
            self.dragao = Dragao()
        return

class Dragao:
    def __init__(self):
        self.nome = "Bebê Dragão"
        self.turnos_restantes = 2
        self.ataques = {"bola de fogo": 35, "Chicote de Cauda":30, "Dentada violenta":40}

    def decida(self, principal, inimigo):
        sorteado = randint(0,1)
        match sorteado:
            case 1:
                self.atacar(principal, inimigo)
            case 0:
                self.curar(principal)

    def atacar(self, principal, inimigo):
        sorteado = randint(0,2)
        inimigo.vida -= list(self.ataques.values())[sorteado]

        exibe(f"{self.nome} usou o ataque {list(self.ataques.keys())[sorteado]}", self, sorteado)
        exibe(f"{inimigo.nome} recebeu {list(self.ataques.values())[sorteado]} de dano", self, inimigo, sorteado)
        self.turnos_restantes -= 1
        if self.turnos_restantes == 0:
            principal.dragao = None


    def curar(self, principal):
        sorteado = randint(20, 40)
        principal.vida += sorteado

        exibe(f"{principal.vida} recebeu {sorteado} pontos de vida", principal, sorteado)
        self.turnos_restantes -= 1
        if self.turnos_restantes == 0:
            principal.dragao = None


class Mercenario(Personagem):
    def __init__(self, nome, defesa, danobase):
        super().__init__(nome, defesa, danobase)
        self.vida = 100
        self.equipamentos = {"Adagas":"descrição",  "Facas arremessaveis":"descrição"}
        self.ataques = {"Ataque Com Adaga":0.9, "Arremessar Faca":0.9, "Esquiva": 0}
        self.habilidades = {"Investida Vorpal":"descrição", "Filho da luz":"descrição"}
        self.inventario = {"Mapa":1, "Ataduras":2}


    def hability(self, inimigo):
        conteudo = "\nQual habilidade especial deseja usar?\n[0]Sair\n"
        for i, k in enumerate(self.habilidades.keys()):
            conteudo += f"[[bright_white]{i + 1}[/]]{k}\n"
        while True:
            exibe(conteudo, time=0.02)
            try:
                atk = int(input())
            except:
                continue
            else:
                if  0 <= atk < 3:
                    break
                else:
                    continue
        if atk == 0:
            exibe("saindo..")
            return "cancel"
        exibe(f"Habilidade Escolhida: [bright_yellow]{list(self.habilidades.keys())[atk - 1]}[/]", self)

        if atk == 1:
            inimigo.vida -= 40
            exibe(f"[bright_yellow]{self.nome}[/] se aproxima rapidamente de inimigo e aplica [bright_yellow]diversos golpes[/]\n"
                  f"[red]{inimigo.nome}[/] ficará [red]atordoado por 2 rodadas[/]", self)
            inimigo.efeitos.append(Atordoado(2))
        elif atk == 2:
            exibe(f"[bright_yellow]{self.nome}[/] de repente fica muito rapido.\n "
                  f"[bright_yellow]{self.nome}[/] fará [bright_yellow]2 açoes no proximo turno[/]", self)
            self.efeitos.append(Luz(2))

        return
