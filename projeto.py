from time import sleep
import os
from abc import ABC, abstractmethod
from rich import print
from random import randint

#Apresentação do Jogo:
def menuinicial():
    print("-"*100)
    print("MistyLand".center(100))
    print("-" * 100)
    while True:
        try:
           resp = int(input("\n[1] Novo Jogo\n[2] Sair\n"))
        except:
            print("Por favor digite uma opçã válida.")
            continue
        else:
            if resp == 2 or resp == 1:
                break
            limpa()

    if resp == 1:
        meth = criacao()
    else:
        return

    print(f"Olá {meth.nome}! Seja bem vindo ao mundo de MistyLand.")
    print("No Mundo de MistyLand existem 2 principais forças dominantes.")

    if meth.__class__.__name__ == "Cavaleiro":#Parafina(Vem do petroleo) e Drake (Edwin Drake) por causa do Petróleo.
        print(
            "Uma dessas forças é um reino chamado Parafina. Onde o Rei Drake, "
            "com sua potência militar de cavaleiros, conquistaram seu espaço no mapa vencendo guerras e principalmente"
            " após a descoberta de um é um combustível fóssil líquido, oleoso e inflamável, "
            "que foi usado como energia por esse reino para criar diversas evoluções."
        )

    if meth.__class__.__name__ == "Mago":
        print(
            "Uma dessas forças é um lugar chamado Spell Town. Onde Gargamel, o mestre dos magos, juntou"
            "muitos sábios e estudiosos, para pesquisarem uma fonte de energia gerada pelo movimento de partículas minúsculas"
            "que possuem carga elétrica negativa. A pesquisa foi um sucesso e Spell Town, através de muitas evoluções"
            "geradas por essa energia, conquistou seu lugar no mundo de MistyLand."
        )

    if meth.__class__.__name__ == "Mercenario":
        print(
            " Uma delas é Parafina, um reino que prosperou muito após a descoberta de uma fonte de energia vinda de um "
            "combustível fóssil líquido, oleoso e inflamável.\n"
            " A segunda por sua vez, se chama Spell Town. Uma cidade que teve sua ascensão após descobrir uma"
            "fonte de energia através da manipulação de cargas elétricas negativas de particulas subatômicas."
        )

#Funcionalidade que controla toda a parte de criação do personagem.
def criacao():
    limpa()
    infs = []
    while True:
        try:
            infs.append(int(input("\nEscolha uma classe:\n[1] Cavaleiro\n[2] Mago\n[3] Mercenário\n")))
            limpa()
            if infs[0] == 1:
                print("\nClasse Cavaleiro:\n"
                      "Vida: HP base + Armadura.\n"
                      "Arma Principal: Espada (Médio Alcance)\n"
                      "Ataques Básicos: Ataque Com Espada, Aparo, Esquiva\n"
                      "Habilidades Especias: Ataque Pesado e Bloqueio Com Escudo")
            elif infs[0] == 2:
                print("\nClasse Mago:\n"
                      "Vida: Menor HP.\n"
                      "Armas Principais: Cajado e Livro de Magias (Longo Alcance).\n"
                      "Ataques Básicos: Ataque Com Cajado, Bola de Fogo, Teletransporte\n"
                      "Habilidades Especias: Chuva de Relâmpagos e Feitiço de cura")
            elif infs[0] == 3:
                print("\nClasse Mercenário:\n"
                      "Vida: HP base.\n"
                      "Armas Principais: Adagas Duplas (Curto Alcance).\n"
                      "Ataques Básicos: Ataque Com Adaga, Chute Giratório, Arremessar Faca\n"
                      "Habilidades Especias: Investida Vorpal e Filho da luz (aumenta a velocidade temporariamente)")
        except Exception as e:
            continue
        resp = input(f"Confirmar escolha da classe {infs[0]}\n[1] Sim\n[2] Não")
        limpa()
        if resp == "1":
            break
        infs.pop()

    infs.append(input("\nAgora escolha o nome:"))

    meth = "nada"
    match infs[0]:
        case 1:
            meth = Cavaleiro(infs[1])
        case 2:
            meth = Mago(infs[1])
        case 3:
            meth = Mercenario(infs[1])

    #print(meth.__dict__)
    return meth

#Funcionalidades para manter o código limpo:
def limpa():
    os.system('cls' if os.name == 'nt' else 'clear')
    for _ in range(3):
        print(".", end= "")
        sleep(0.1)

def enter():

    while True:
        print("Pressione 'ENTER' para continuar...")
        if input() == "":
            break

#Mundo e Exploração:
def vila_inicial(principal):
    while True:
        print(f"{principal.nome} se encontra na Vila Inicial.\n"
              f"Após receber sua missão, Você pode escolher 3 caminhos para seguir:\n")
        principal.mapa()
        resp = input("Por Qual Delas Deseja Seguir?\n[1]LAGO DO ESQUECIMENTO\n"
                     "[2]FLORESTA DA PERDIÇÃO\n[3]CAVERNA LABIRÍNTICA\n")

        match resp:
            case "1":
                lago_do_esquecimento(principal)
                return
            case "2":
                floresta_da_perdicao(principal)
                return
            case "3":
                caverna_labirintica(principal)
                return
            case _:
                print("Por favor, Escolha uma opção válida")
                continue

def lago_do_esquecimento(principal):
    # evento aleatorio:Item, NPC, Historia
    print(f"Você se vê sozinho em um imenso lago...\n{principal.nome} olha para baixo e percebe que é como se"
          f"algo enorme estivesse se movimentando no fundo do lago.Causando uma enorme sombra por onde passa."
          f"{principal.nome} ainda pensa em voltar, mas antes mesmo de qualquer possível reação.."
          f"\n[red]O Monstro Do Lago Aparece:[/] [blue]NESSIE[/]")

    enter()
    combate(principal, Nessie())


def floresta_da_perdicao(principal):
    # evento aleatorio:Item, NPC, Historia
    print("De repente, em meio a densa floresta..\nVocê começa a ouvir [red]longos assobios..[/]\n"
          f"{principal.nome} vai ficando cada vez mais zonzo e [red]perdido...[/]\n"
          f"Quando se da conta, você está totalmente perdido. No coração da floresta, Diante do que se parece"
          f"um [red]templo de pedra.[/]Os assobios voltam de forma ainda mais intensa. Quando de repente...\n"
          f"[red]CURUPIRA aparece[/]")

    enter()
    combate(principal, Curupira())

def caverna_labirintica(principal):
    while True:
        #evento aleatorio:Item, NPC, Historia
        print("Você encontra uma figura estranha. Algo como um [red]urso com chifres[/]"
              " aparentemente dormindo...\nDeseja se aproximar?\n[1]Sim\n[2]Não\n")

        resp = input()
        if resp == "1":
            break
        else:
            print("Você volta para o labirinto na esperança de encontrar um outro caminho")
            continue


    print("[red]MINOTAURO Acorda..[/]")
    enter()
    combate(principal, Minotauro())


#Sistema de Combate:
def combate(principal, inimigo):
    while True:
            for efeito in principal.efeitos:
                efeito.aplicar(principal, inimigo)
            fugir = turno_jogador(principal, inimigo)
            principal.atualizar_efeito()
            if principal.vida == 0 or inimigo.vida == 0:
                return True

            if fugir == True:
                break
            else:
                for efeito in inimigo.efeitos:
                    efeito.aplicar(inimigo, principal)

                turno_inimigo(principal, inimigo)
                inimigo.atualizar_efeito()
                if principal.vida == 0 or inimigo.vida == 0:
                    return False


def turno_jogador(principal, inimigo):
    limpa()
    print(f"\nO que deseja fazer?")
    print(
        "[bright_white][1][/]Atacar\n[bright_white][2][/]Defender\n[bright_white][3][/]Usar Item\n[bright_white][4][/]Fugir")
    resp = int(input())
    match resp:
        case 1:
            atacar(principal, inimigo)
        case 2:
            defender(principal, inimigo)
        case 3:
            inventario(principal)
        case 4:
            return True
        case _:
            raise PermissionError("Deu algum erro")
    try:
        if principal.dragao != None:
            print("ENTROU!!!!!!!!!!!!!")
            principal.dragao.decida(principal, inimigo)
    except:
        pass

    return False

def turno_inimigo(principal, inimigo):
    decisao = randint(0, 1)

    match decisao:#talvez fazer um defender depois
        case 0:#atacar
            dmg = inimigo.atacar(principal)
            inimigo.carrega += 15

            print(f"{principal.nome} recebeu [red]{dmg}[/] de dano")
        case 1:#curar
            inimigo.curar()
        case _:
            print("opção errada")

    if inimigo.carrega >= 100:
        inimigo.hability(principal)



    return

def atacar(principal, inimigo):
    print("Ataques Disponiveis:")
    for i in range(len(principal.ataques.keys())):
        print(f"[bright_white]{[i+1]}[/] {list(principal.ataques.keys())[i]}")
        if principal.carrega >= 100:
            print(f"[{len(principal.ataques) + 1}]Habilidade Está Carregada!")

    resp = int(input("[0] Sair\n"))
    if resp == 0:
        return

    if resp == len(principal.ataques) + 1:
        principal.hability(inimigo)
        return

    if list(principal.ataques.keys())[resp-1] != "Esquiva":
        print(f"inimigo recebeu {dano(principal, inimigo)} de dano.")
        principal.carrega += 15
        #print(f"barra{principal.carrega}")

    return

def dano(principal, vitima):
    vitima.vida -= principal.dano - principal.dano * vitima.defesa / 100
    return principal.dano - principal.dano * vitima.defesa / 100

def defender(principal, inimigo):
    dano = inimigo.atacar(principal)
    dano -= dano * (randint(8,principal.defesa) / 75)

    print(f"{principal.nome} defendeu o dano parcialmente!")
    print(f"Dano Recebido: {int(dano)}")

    return


def inventario(principal):
    limpa()
    cont = 1
    for i, k in principal.inventario.items():
        print(f"\n[[bright_white]{cont}[/]]{i}: {k}\n")
        cont += 1
    print("[[bright_white]0[/]]Sair")

    resp = int(input("Deseja usar qual item?\n"))
    match resp:
        case 1:
            limpa()
            principal.mapa()
        case 2:
            print(principal.vida)
            print(principal.curar())
            print(principal.vida)


    return
#classe de personagens principais
class Personagem(ABC):
    def __init__(self, nome, defesa, danobase):
        self.nome = nome
        self.vida = 100
        self.defesa = defesa
        self.danobase = danobase
        self.equipamentos = {}
        self.ataques = {}
        self.habilidades = {}
        self.inventario = {}
        self.carrega = 0
        self.efeitos = []

    @property
    def dano(self):
        dano = self.danobase
        try:
            for efeito in self.efeitos:
                dano = efeito.aplicar(dano)
        except:
            pass
        return dano

    def mapa(self):
        print(
            f"\nLAGO DO ESQUECIMENTO{' '*8}FLORESTA DA PERDIÇÃO{' '*8}CAVERNA LABIRÍNTICA\n"
            f"[bright_white]{' '*21} {chr(92)}{' '*15}|{' '*17}/[/]\n\n"
            f"{' '* 32}VILA INICIAL"
        )
        enter()
        return

    def curar(self):
        self.vida += 20
        return f"{self.nome} usou {list(self.inventario.keys())[1]} e recuperou 20 pontos de vida."


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
        self.ataques = {"Ataque Com Espada": 30, "Aparo": 30, "Esquiva": 30}
        self.habilidades = {"Ataque Pesado":20, "Bloqueio Com Escudo":0}
        self.inventario = {"Mapa":"descrição", "Ataduras":"descrição"}


    def hability(self, inimigo):
        for i, k in enumerate(self.habilidades.keys()):
            print(f"[[bright_white]{i + 1}[/]]{k}")
        print("[[bright_white]0[/]]Sair")
        atk = int(input("Qual habilidade especial deseja usar?"))

        print(f"Habilidade Escolhida: {list(self.habilidades.keys())[atk - 1]}")
        if atk == 1:
            inimigo.vida -= 40

            print("Habilidade escolhida: [red]Ataque Pesado[/]")
            print(f"{inimigo.vida} recebeu 40 de Dano --talvez receber atributo tonto--")
            inimigo.efeitos.append(Atordoado(3))
        elif atk == 2:
            print("Habilidade Escohida: [red]Bloqueio com Escudo[/]--pelas proximas 3 rodadas a defesa é aumentada em 30%")
            self.defesa *= 1.3
            self.efeitos.append(Defensor(3))
        return


class Mago(Personagem):
    def __init__(self, nome, defesa, danobase):
        super().__init__(nome, defesa, danobase)
        self.vida = 70
        self.equipamentos = {"Livro de Feitiços":"descrição", "Cajado Mágico":"descrição",}
        self.ataques = {"Ataque Com Cajado":30, "Bola de Fogo":30, "Teletransporte":10}
        self.habilidades = {"Tempestade de Relâmpagos": 10, "Invocação Amiga": 10}
        self.inventario = {"Mapa":"descrição", "Poções":"descrição"}
        self.dragao = None

    def hability(self, inimigo):
        for i, k in enumerate(self.habilidades.keys()):
            print(f"[[bright_white]{i + 1}[/]]{k}")
        print("[[bright_white]0[/]]Sair")
        atk = int(input("Qual habilidade especial deseja usar?"))

        print(f"Habilidade Escolhida: {list(self.habilidades.keys())[atk-1]}")
        if atk == 1:
            inimigo.vida -= 40

            print(f"{self.nome} Núvens negras cobrem o céu..\nDiversos relâmpagos de repente caem sobre{inimigo.nome}"
                  f"{inimigo.nome} Recebe 40 de dano e ficará paralizado")
            inimigo.efeitos.append(Paralizado(2))
        if atk == 2:
            self.ctrlinvoc()
            print("bixo foi invocado. por 2 rodadas principal.nome terá ajuda do seu bixo invocado. podendo curar ou atacar"
                  "o inimigo")
            return

    def ctrlinvoc(self):
        if self.dragao == None:
            self.dragao = Dragao()
            print("Criou memo pae")
        return

class Dragao:
    def __init__(self):
        self.nome = "Bebê Dragão"
        self.turnos_restantes = 2
        self.ataques = {"bola de fogo": 10, "Chicote de Cauda":20, "Dentada violenta":20}

    def decida(self, principal, inimigo):
        print("ENTROU?????????????")
        sorteado = randint(0,1)
        match sorteado:
            case 1:
                self.atacar(principal, inimigo)
            case 0:
                self.curar(principal)
        print(sorteado)

    def atacar(self, principal, inimigo):
        sorteado = randint(0,2)
        inimigo.vida -= list(self.ataques.values())[sorteado]

        print(f"{self.nome} usou o ataque {list(self.ataques.keys())[sorteado]}")
        print(f"{inimigo.nome} recebeu {list(self.ataques.values())[sorteado]} de dano")
        self.turnos_restantes -= 1
        if self.turnos_restantes == 0:
            principal.dragao = None


    def curar(self, principal):
        sorteado = randint(20, 40)
        principal.vida += sorteado

        print(f"{principal.vida} recebeu {sorteado} pontos de vida")
        self.turnos_restantes -= 1
        if self.turnos_restantes == 0:
            principal.dragao = None


class Mercenario(Personagem):
    def __init__(self, nome, defesa, danobase):
        super().__init__(nome, defesa, danobase)
        self.vida = 100
        self.equipamentos = {"Adagas":"descrição",  "Facas arremessaveis":"descrição"}
        self.ataques = {"Ataque Com Adaga": 10, "Chute Giratório":5, "Arremessar Faca":7}
        self.habilidades = {"Investida Vorpal":30, "Filho da luz":0}
        self.inventario = {"Mapa":"descrição", "Ataduras":"descrição"}


    def hability(self, inimigo):
        for i, k in enumerate(self.habilidades.keys()):
            print(f"[[bright_white]{i + 1}[/]]{k}")
        print("[[bright_white]0[/]]Sair")
        atk = int(input("Qual habilidade especial deseja usar?"))

        print(f"Habilidade Escolhida: {list(self.habilidades.keys())[atk - 1]}")
        if atk == 1:
            inimigo.vida -= 40
            print(f"{self.nome} se aproxima rapidamente de inimigo e aplica diversos golpes de uma vez\n"
                  f"inimigo fica atordoado--talvez fique atordoado--")
            inimigo.efeitos.append(Atordoado(2))
        if atk == 2:
            print("self.nome fica muito rapido. podera fazer 2 açoes no proximo turno")
            self.efeitos.append(Luz(1))#esse 1 é a quantidade de turnos a mais

        return

#Classes de inimigos, mini-bosses, etc
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

    @property
    def dano(self):
        dano = self.danobase
        try:
            for efeito in self.efeitos:
                dano = efeito.aplicar(dano)
        except:
            pass
        return dano

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
        self.ataques = {"Soco Pesado":self.danobase*1, "Coice Duplo":self.danobase*1, "Lançardor Subterraneo":self.danobase*1}
        self.habilidades = {"Chife Demoníaco": 44, "Furia Divina":10}
        #investida para chifrar o inimigo
        #furia divina: os proximos 3 ataques dele terão +50% de dano.

    def atacar(self, inimigo):
        sorteado = randint(0, 2)

        print(f"Minotauro escolheu {list(self.ataques.keys())[sorteado]}")
        dmg = dano(self, inimigo)
        return dmg

    def curar(self):
        sorteado = randint(20, 30)
        self.vida = sorteado
        print(f"Minotauro recuperou {sorteado} pontos de vida")

        return

    def hability(self, principal):
        sorteado = randint(0,1)
        print(f"Habilidade Escolhida: {list(self.habilidades.keys())[sorteado]}")
        if sorteado == 0:
            print("Minotauro se preprara para chifrar..")
            principal.efeitos.append(Atordoado(2))
        if sorteado == 1:
            print("Minotauro solta um grito ensurdecedor")
            self.efeitos.append(Furia(3))
        return

class Curupira(Inimigos):
    def __init__(self):
        super().__init__("Curupira", 45)
        self.ataques = {"Chute Trocado": 30, "Investida Furiosa": 30, "Chicote de Cipó":30}
        self.habilidades = {"Confusão Mental": 35, "Pai Natureza":44}
        #confusão mental: menos dano, mas a vitima pode ganhar o status, "Lost", perde um turno tentando recobrar
        #a consciencia de onde está e achar o curupira novamente.

        #rei da floresta: pensei em algo como trazer uma enxurrada de animais para atacar o inimigo

    def atacar(self, inimigo):
        sorteado = randint(0, 2)

        print(f"Curupira escolheu {list(self.ataques.keys())[sorteado]}")
        dmg = dano(self, inimigo)
        return dmg

    def curar(self):
        sorteado = randint(20, 30)
        self.vida = sorteado
        print(f"Curupira recuperou {sorteado} pontos de vida")

        return

    def hability(self, principal):
        sorteado = randint(0,1)
        print(f"Habilidade Escolhida: {list(self.habilidades.keys())[sorteado]}")
        if sorteado == 0:
            print("Curupira toca o berrante e chama uma enxurrada de animais")
            principal.vida -= 40
            principal.efeitos.append(Atordoado(2))
        if sorteado == 1:
            print("De repente, você começa a ouvir um assobio hipnotizante..")
            print(f"{principal.nome} está preso na ilusão de curupira")
            principal.efeitos.append(Perdido())
        return

class Nessie(Inimigos):
    def __init__(self):
        super().__init__("Nessie", 30)
        self.ataques = {"Martelo de Cauda": 30, "Tiro de Água":30, "Mordida Feroz": 30}
        self.habilidades = { "Canhão de Água": 44, "Território": 0}
        #territorio: tentar levar o inimigo para o fundo do mar. Os ataques do nessie ficariam muito mais fortes
        #e o do principal muito mais fracos

    def atacar(self, inimigo):
        print(self.__dict__)
        sorteado = randint(0, 2)

        print(f"Nessie escolheu {list(self.ataques.keys())[sorteado]}")
        dmg = dano(self, inimigo)
        return dmg

    def curar(self):
        sorteado = randint(20, 30)
        self.vida = sorteado
        print(f"Minotauro recuperou {sorteado} pontos de vida")

        return

    def hability(self, principal):
        sorteado = 1
        print(f"Habilidade Escolhida: {list(self.habilidades.keys())[sorteado]}")
        if sorteado == 0:
            print(f"Nissie prepara um jato de água compressurizada e atira na direção de {principal.nome}")
            principal.vida -= 40
            principal.efeitos.append(Atordoado(2))
        if sorteado == 1:
            print("Nissie te abocanha e num rapido movimento tenta te levar para debaixo da água")
            print(f"[blue]Debaixo da água Nissie tem aumento de ataque e cura[/]")
            self.efeitos.append(Territorio(3))
        return

#Classe que controla os efeitos que serão aplicados aos personagens e como serão aplicados
class Efeitos(ABC):
    def __init__(self, nome, duracao, tipo):
        self.nome = nome
        self.duracao = duracao
        self.tipo = tipo

class Defensor(Efeitos):
    def __init__(self, duracao):
        super().__init__("Defensor", duracao, "Buff")

    def aplicar(self, afetado):
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
        print(inimigo.__dict__)

    def atualizar(self, inimigo):
        inimigo.danobase /= 0.6

class Paralizado(Efeitos):
    def __init__(self, duracao):
        super().__init__("Paralizado", duracao, "Debuff")

    def aplicar(self, principal = None, inimigo = None):
        for i in range(randint(0,1)):
            print(f"{inimigo.nome} está atordoado")
            turno_jogador(principal, inimigo)

class Perdido(Efeitos):
    def __init__(self):
        super().__init__("Lost", 4, "Debuff")

    def aplicar(self, personagem = None, inimigo = None):
        while True:
            print(f"{personagem.nome} tenta escapar da ilusão..")
            while True:
                print("Pressione 'ENTER' para continuar...")
                if input() == "":
                    break

            if randint(0,1) == 1:
                print(f"{personagem.nome} [blue]recobra os sentidos[/]")
                self.duracao = 0
                break
            turno_inimigo(personagem, inimigo)

cav = Cavaleiro("ricardo", 30, 30)
vila_inicial(cav)