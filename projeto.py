from time import sleep
import os
from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel
from rich.live import Live
from random import randint


def exibe(txt_completo, obj=None, secundario= None, terceiro=None, time=0.04):
    txt_atual = ""
    painel = Panel(txt_atual, width=120, border_style="yellow")
    with Live(painel, refresh_per_second=25) as live:
        for letra in txt_completo:
            txt_atual += letra
            live.update(Panel(txt_atual, width=80, border_style="yellow"))
            sleep(time)


#Apresentação do Jogo:
def menuinicial():
    exibe("MistyLand".center(75),time=0)
    while True:
        try:
            exibe("\n[1] Novo Jogo\n[2] Sair\n")
            resp = int(input())
            limpa()
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

    limpa()

    exibe(f"Olá [green]{meth.nome}[/]! Seja bem vindo ao mundo de MistyLand. \n"
          f"No Mundo de MistyLand existem duas principais forças dominantes.", meth, time=0.02)

    if meth.__class__.__name__ == "Cavaleiro":#Parafina(Vem do petroleo) e Drake (Edwin Drake) por causa do Petróleo.
        exibe(
            "Uma dessas forças é um reino chamado [blue]Parafina[/]. Onde o [blue]Rei Drake[/], "
            "com sua potência militar de cavaleiros, conquistaram seu espaço no mapa vencendo guerras e principalmente"
            " após a descoberta de um é um [blue]combustível fóssil[/] líquido, oleoso e inflamável, "
            "que foi usado como energia por esse reino para criar diversas evoluções."
        , time=0.02)

    if meth.__class__.__name__ == "Mago":
        exibe(
            "Uma dessas forças é um lugar chamado [red]Spell Town[/]. Onde [red]Gargamel[/], o mestre dos magos, juntou"
            "muitos sábios e estudiosos, para pesquisarem uma fonte de energia gerada pelo movimento de partículas minúsculas"
            "que possuem [red]carga elétrica negativa[/]. A pesquisa foi um sucesso e Spell Town, através de muitas evoluções"
            "geradas por essa energia, conquistou seu lugar no mundo de MistyLand."
        , time=0.02)

    if meth.__class__.__name__ == "Mercenario":
        exibe(
            " Uma delas é [blue]Parafina[/], um reino que prosperou muito após a descoberta de uma fonte de energia vinda de um "
            "[blue]combustível fóssil[/] líquido, oleoso e inflamável.\n"
            " A segunda por sua vez, se chama [red]Spell Town[/]. Uma cidade que teve sua ascensão após descobrir uma "
            "fonte de energia através da manipulação de [red]cargas elétricas negativas[/] de particulas subatômicas."
        , time=0.02)

    enter()
    limpa()
    vila_inicial(meth)

#Funcionalidade que controla toda a parte de criação do personagem.
def criacao():
    limpa()
    infs = []
    while True:
        try:
            while True:
                exibe("\nEscolha uma classe:\n[1] Cavaleiro\n[2] Mago\n[3] Mercenário\n")
                try:
                    resp = int(input())
                except:
                    continue
                else:
                    if 0 < resp < 4:
                        infs.append(resp)
                        break
                    else:
                        continue

            limpa()
            if infs[0] == 1:
                exibe("\nClasse Cavaleiro:\n"
                      "Vida: HP base + Armadura.\n"
                      "Arma Principal: Espada (Médio Alcance)\n"
                      "Ataques Básicos: Ataque Com Espada, Aparo, Esquiva\n"
                      "Habilidades Especias: Ataque Pesado e Bloqueio Com Escudo", time=0.01)
            elif infs[0] == 2:
                exibe("\nClasse Mago:\n"
                      "Vida: Menor HP.\n"
                      "Armas Principais: Cajado e Livro de Magias (Longo Alcance).\n"
                      "Ataques Básicos: Ataque Com Cajado, Bola de Fogo, Teletransporte\n"
                      "Habilidades Especias: Chuva de Relâmpagos e Feitiço de cura", time=0.01)
            elif infs[0] == 3:
                exibe("\nClasse Mercenário:\n"
                      "Vida: HP base.\n"
                      "Armas Principais: Adagas Duplas (Curto Alcance).\n"
                      "Ataques Básicos: Ataque Com Adaga, Chute Giratório, Arremessar Faca\n"
                      "Habilidades Especias: Investida Vorpal e Filho da luz (aumenta a velocidade temporariamente)", time=0.01)
        except Exception as e:
            continue
        exibe(f"Confirmar escolha da classe {infs[0]}\n[1] Sim\n[2] Não", infs, time = 0)
        resp = input()
        limpa()
        if resp == "1":
            break
        infs.pop()

    exibe("\nAgora escolha o nome:")
    infs.append(input())

    meth = "nada"
    match infs[0]:
        case 1:
            meth = Cavaleiro(infs[1], 30, 30)
        case 2:
            meth = Mago(infs[1], 10, 30)
        case 3:
            meth = Mercenario(infs[1],25, 30)

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
        exibe(f"{principal.nome} se encontra na Vila Inicial.\n"
              f"Após receber sua missão, Você pode escolher 3 caminhos para seguir:\n", principal, time=0.02)
        principal.mapa()
        exibe("Por Qual Delas Deseja Seguir?\n[1]LAGO DO ESQUECIMENTO\n"
                     "[2]FLORESTA DA PERDIÇÃO\n[3]CAVERNA LABIRÍNTICA\n", time=0.03)
        resp = input()

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
    limpa()
    evento_aleatorio(principal, "lago")

    exibe(f"Você se vê sozinho em um imenso e denso lago...\n{principal.nome} olha para baixo e percebe que é como se"
          f" algo enorme estivesse se movimentando no fundo do lago.Causando uma enorme sombra por onde passa."
          f"{principal.nome} ainda pensa em voltar, mas antes mesmo de qualquer possível reação.."
          f"\n[red]O Monstro Do Lago Aparece:[/] [blue]NESSIE[/]",obj=principal)

    enter()
    if combate(principal, Nessie()):
        exibe("Após derrotar Nissie, a densidade do lago desaparece e você consegue ver que no fundo"
              "do profundo lago, parece ter algo como um laboratório.\n")
        #talvez adquirir um item
    else:
        if principal.vida <= 0:
            exibe("[red]GAME OVER[/]\nretornando para o último checkpoint...")
        else:
            exibe(f"[bright_yellow]{principal.nome} fugiu![/]")


def floresta_da_perdicao(principal):
    limpa()
    evento_aleatorio(principal, "floresta")

    exibe("De repente, em meio a densa floresta..\nVocê começa a ouvir [red]longos assobios..[/]\n"
          f"{principal.nome} vai ficando cada vez mais zonzo e [red]perdido...[/]\n"
          f"Quando se da conta, você está totalmente perdido. No coração da floresta, Diante do que se parece"
          f"um [red]templo de pedra.[/]Os assobios voltam de forma ainda mais intensa. Quando de repente...\n"
          f"[red]CURUPIRA aparece[/]", obj=principal)

    enter()
    if combate(principal, Curupira()):
        exibe("ganhou paezao")
    # talvez adquirir um item
    else:
        if principal.vida <= 0:
            exibe("[red]GAME OVER[/]\nretornando para o último checkpoint...")
        else:
            exibe(f"[bright_yellow]{principal.nome} fugiu![/]")

def caverna_labirintica(principal):
    limpa()
    while True:
        evento_aleatorio(principal, "caverna")
        exibe("Você encontra uma figura estranha. Algo como um [red]urso com chifres[/]"
              " aparentemente dormindo...\nDeseja se aproximar?\n[1]Sim\n[2]Não\n")

        resp = input()
        if resp == "1":
            break
        else:
            exibe("Você volta para o labirinto na esperança de encontrar um outro caminho")
            continue


    exibe("[red]MINOTAURO Acorda..[/]")
    enter()
    if combate(principal, Minotauro()):
        exibe("ganhou pae")
    # talvez adquirir um item
    else:
        if principal.vida <= 0:
            exibe("[red]GAME OVER[/]\nretornando para o último checkpoint...")
        else:
            exibe(f"[bright_yellow]{principal.nome} fugiu![/]")

def evento_aleatorio(principal, lugar):
    sorteado = randint(0,2)

    match sorteado:
        case 0:
            npc(principal, lugar)
        case 1:
            item_aleatorio(principal, lugar)
        case _:
            nada_acontece(principal, lugar)

def npc(principal, lugar):
    if lugar == "lago":
        exibe(f"{principal.nome} avista um grupo de pescadores\nDeseja se aproximar?\n[1]Sim\n[2]Não\n",obj=principal)
        resp = input()
        match resp:
            case "1":
                exibe(f"[yellow]Pescadores:[/] O que está fazendo aqui?\n[blue]{principal.nome}:[/]\n"
                      f"[1]Apenas de passagem...\n[2]Não é da sua conta\n", obj=principal)
                resp = input()
                match resp:
                    case "1":
                        exibe("[yellow]Pescadores:[/] Normalmente ninguém vem aqui. Até o número de pescadores diminui"
                              "depois que os peixes começaram a morrer de forma misteriosa. Deve ser"
                              "o [red]Monstro do lago ness[/] que ronda essa região. Tome cuidado amigo...")
                    case _:
                        exibe("[yellow]Pescadores:[/] Entendido, boa viagem.")
            case _:
                pass
        return
    elif lugar == "floresta":
        exibe(f"{principal.nome} avista um aventureiro com uma cara de confuso assustadora.\nDeseja se aproximar?"
              f"\n[1]Sim\n[2]Não\n", obj=principal)
        resp = input()
        match resp:
            case "1":
                exibe("[yellow]Aventureiro:[/] Que bom ver um rosto humano após tanto tempo...")
                while True:
                    exibe("Por favor companheiro, diga me por qual caminho você entrou na Floresta?"
                          "\n[1]Apontar Direção\n[2]Perguntar o que aconteceu.\n")
                    resp = input()
                    if resp == "1":
                        break
                    else:
                        exibe("Não sei. Tudo que eu me lembro é daquele [red]tenebroso assobio[/]")
                        continue

            case _:
                pass
        return
    else:
        exibe(f"Assim que {principal.nome} vira mais uma esquina do labirinto, se depara com um homem mascarado.", obj=principal)
        enter()
        exibe("[yellow]Mascarado: [/]Ainda bem que você chegou!\nVamos, me dê logo o que combinamos com a realeza.\n"
              "[1]Não sei do que está falando\n[2]Putz! Devo ter deixado cair no caminho.\n")
        input()
        exibe("[red]Como assim!?[/] Você é de fato um subordinado do Herold? Me diga o código que ele te mandou dizer:\nCódigo: \n")
        input()
        exibe("[red]Certo..[/] ignore tudo que aconteceu tá bom garoto? Só finja que nunca me viu..."
              "\n [red]Mascarado vira uma esquerda do labirinto e desaparece.[/]")
        return


def item_aleatorio(principal, lugar):
    sorteado = randint(0,2)
    if lugar == "lago":
        exibe(f"{principal.nome} [yellow]avista um bote abandonado[/] vindo em sua direção. Ao vasculhar", obj=principal)
    elif lugar == "floresta":
        exibe(f"{principal.nome} [yellow]Encontra uma bolsa[/]"
              f" velha jogada perto de uma arvóre. Ao verificar ", obj=principal)
    else:
        exibe(f"{principal.nome} [yellow]encontra um báu[/]. Ao verificar ", obj=principal)

    match sorteado:
        case 0:
            quant = randint(2, 6)
            exibe(f"{principal.nome} encontra [bright_yellow]{quant} moedas de ouro[/] e guarda em sua bolsa"
                  , obj=principal, secundario=quant)
            principal.dinheiro += quant
        case 1:
            item = list(principal.inventario.keys())[1]
            exibe(f"{principal.nome} encontra [magenta] 2 {item}[/] e guarda em sua bolsa", obj=principal,
                  secundario=item)
            principal.inventario[item] += 2
        case _:
            exibe(f"{principal.nome} encontra [bright_yellow]um caderno de anotações[/]"
                  f", Deseja ler?\n[1] Sim\n[2] Não", obj=principal)
            resp = input()
            match resp:
                case "1":
                    exibe("O cader no de anotações está com diversas folhas rasgadas. As poucas restantes dizem:\n"
                          "...Esses caras são [red]insanos[/]. Tive que rasgar a maioria das folhas do meu diário para"
                          "não descobrirem. Eles pretendem dominar o mundo com a [bright_magenta]EPI[/]."
                          f"Estão pensando até em colocar algum tipo de [red]Guardião[/] nesse lugar!"
                          f"Se alguém encontrar esse diário, [red]fuja imediatamente desse lugar[/].")
                case _:
                    exibe(f"{principal.nome} devolve o caderno de anotações e continua sua aventura.", obj=principal)

def nada_acontece(principal, lugar):
    if lugar == "lago":
        exibe(f"{principal.nome} [yellow]avista um bote abandonado[/] vindo em sua direção. Deseja verificar se encontra algo?\n"
                     f"[1] Sim\n[2] Não\n", obj=principal)
        input()
        exibe(f"{principal.nome} Não encontra nada no bote.", obj=principal)
    elif lugar == "floresta":
        exibe(f"{principal.nome} [yellow]Encontra uma bolsa[/] velha jogada perto de uma arvóre. Deseja verificar se encontra algo?\n"
              f"[1] Sim\n[2] Não\n", obj=principal)
        input()
        exibe(f"{principal.nome} Não encontra nada na bolsa.", obj=principal)
    elif lugar == "caverna":
        exibe(f"{principal.nome} [yellow]encontra um báu[/]. Deseja verificar se encontra algo?\n"
              f"[1] Sim\n[2] Não\n", obj=principal)
        input()
        exibe(f"{principal.nome} Não encontra nada no baú.", obj=principal)
    else:
        print("erro")
        pass

#Sistema de Combate:
def combate(principal, inimigo):
    while True:
            for efeito in principal.efeitos:
                efeito.aplicar(principal, inimigo)

            fugir = turno_jogador(principal, inimigo)
            enter()
            if inimigo.vida > 0:
                principal.atualizar_efeito()
            if principal.vida <= 0:
                return False
            if inimigo.vida <= 0:
                return True

            if fugir == True:
                break

            if fugir == "esquiva":
                continue

            else:
                for efeito in inimigo.efeitos:
                    efeito.aplicar(inimigo, principal)


                turno_inimigo(principal, inimigo)
                enter()
                if principal.vida > 0:
                    inimigo.atualizar_efeito()
                if principal.vida <= 0:
                    return False
                if inimigo.vida <= 0:
                    return True


def turno_jogador(principal, inimigo):
    while True:
        limpa()
        exibe(f"\nO que deseja fazer?")
        exibe(
            "[bright_white][1][/]Atacar\n[bright_white][2][/]Defender\n[bright_white][3][/]Usar Item\n[bright_white][4]"
            "[/]Fugir", time=0.02)
        try:
            resp = int(input())
        except:
            continue
        else:

            match resp:
                case 1:
                    resultado = atacar(principal, inimigo)
                    if resultado == "cancel":
                        continue
                    elif resultado == "esquiva":
                        return "esquiva"
                    break
                case 2:
                    defender(principal, inimigo)
                    break
                case 3:
                    if inventario(principal, inimigo) == "cancel":
                        continue
                    break
                case 4:
                    return True
                case _:
                    continue
    try:
        if principal.dragao != None:
            principal.dragao.decida(principal, inimigo)
    except:
        pass

    return False

def turno_inimigo(principal, inimigo):
    decisao = randint(0, 1)

    match decisao:#talvez fazer um defender depois
        case 0:#atacar
            if inimigo.carrega >= 100:
                inimigo.hability(principal)
                inimigo.carrega = 0
            dmg = inimigo.atacar(principal)
            inimigo.carrega += 50

            exibe(f"[blue]{principal.nome}[/] recebeu [red]{dmg}[/] de dano", obj=principal, secundario=dmg)
            return dmg
        case 1:#curar
            inimigo.curar()
            return
        case _:
            print("opção errada")
    return

def atacar(principal, inimigo):
    limpa()
    while True:
        conteudo = "[0] Sair\n"
        for i in range(len(principal.ataques.keys())):
            conteudo += f"[bright_white]{[i + 1]}[/] {list(principal.ataques.keys())[i]}\n"

        exibe(f"Ataques Disponiveis:\n{conteudo}", time=0.03)
        if principal.carrega >= 100:
            exibe(f"[{len(principal.ataques) + 1}]Habilidade Está Carregada!\n", obj=principal)
        try:
            resp = int(input())
        except:
            continue
        else:
            while True:

                if 0 <= resp < 4:
                    break
                elif principal.carrega >= 100 and resp == 4:
                    break
                else:
                    while True:
                        print("[red]Digite uma opção válida[/]")
                        try:
                            resp = int(input())
                        except:
                            continue
                        else:
                            break
                    continue
            if resp == 0:
                return "cancel"

            if resp == len(principal.ataques) + 1 and principal.carrega >= 100:
                if principal.hability(inimigo) == "cancel":
                    continue
                principal.carrega = 0
                return

            if list(principal.ataques.keys())[resp-1] != "Esquiva" and list(principal.ataques.keys())[resp-1] !="Teletransporte":
                dmg = dano(principal, inimigo)
                exibe(f"[red]{inimigo.nome}[/] recebeu [red]{dmg}[/] de dano.", dmg)
                principal.carrega += 15
            # FAZER O DA ESQUIVA E TELEPORTE AQUI
                return
            else:
                exibe(f"{principal.nome} tenta esquivar:\nRolando dado...", principal, time = 0.02)
                sorteado = randint(1, 6)
                if sorteado > 2:
                    exibe(f"[green]Sucesso![/]\nDado: {sorteado}")
                    return "esquiva"
                else:
                    exibe(f"[red]Fracasso![/]\nDado: {sorteado}")
                    return


def dano(principal, vitima):
    vitima.vida -= principal.danobase - principal.danobase * vitima.defesa / 100
    return principal.danobase - principal.danobase * vitima.defesa / 100

def defender(principal, inimigo):
    limpa()
    principal.defesa += principal.defesa * 0.20

    exibe(f"{principal.nome} defenderá o dano parcialmente! [blue](defesa aumentada em 20%)[/]")
    return


def inventario(principal, inimigo):
    limpa()
    cont = 1
    conteudo = "Deseja usar qual item:\n"
    conteudo += "[0]Sair\n"
    for i, k in principal.inventario.items():
        conteudo += f"[[bright_white]{cont}[/]]{i}: {k}\n"
        cont += 1
    conteudo += ""
    exibe(conteudo)
    while True:
        try:
            resp = int(input())
        except:
            continue
        else:
            match resp:
                case 0:
                    return "cancel"
                case 1:
                    limpa()
                    principal.mapa()
                case 2:
                    if list(principal.inventario.values())[1] > 0:
                        if principal.vida < 100:
                            exibe(str(principal.curar(inimigo)), principal)
                            principal.inventario[list(principal.inventario.keys())[1]] -= 1
                        else:
                            exibe("vida já está no máximo")
                            return "cancel"
                    else:
                        pass
            break

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
        self.dinheiro = 0

    def mapa(self):
        exibe(
            f"\nLAGO DO ESQUECIMENTO{' '*8}FLORESTA DA PERDIÇÃO{' '*8}CAVERNA LABIRÍNTICA\n"
            f"[bright_white]{' '*21} {chr(92)}{' '*15}|{' '*17}/[/]\n\n"
            f"{' '* 32}VILA INICIAL"
        , time=0)
        enter()
        return

    def curar(self, inimigo):
        if self.vida < 100:
            self.vida += 20
            return f"{self.nome} usou {list(self.inventario.keys())[1]} e recuperou 20 pontos de vida."
        else:
            print(f"Vida no maximo")
            turno_jogador(self, inimigo)


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
        self.ataques = {"Ataque Com Espada": self.danobase*0.8, "Aparo": self.danobase*0.8, "Esquiva": self.danobase*0}
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
                        exibe(f"[red]{inimigo.vida}[/] recebeu [red]40[/] de dano e ficará [red]atordoado[/]"
                              f"por 3 rodadas", inimigo)
                        inimigo.efeitos.append(Atordoado(3))
                        break
                    elif atk == 2:
                        exibe("Habilidade Escohida: [blue]Bloqueio com Escudo[/] pelas proximas"
                              " [blue]3 rodadas a defesa é aumentada em 30%[/]")
                        self.defesa *= 1.3
                        self.efeitos.append(Defensor(3))
                        break
        return


class Mago(Personagem):
    def __init__(self, nome, defesa, danobase):
        super().__init__(nome, defesa, danobase)
        self.vida = 100
        self.equipamentos = {"Livro de Feitiços":"descrição", "Cajado Mágico":"descrição",}
        self.ataques = {"Ataque Com Cajado":self.danobase * 0.7, "Bola de Fogo":self.danobase * 0.8, "Teletransporte":self.danobase * 0}
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
                    exibe(f"Habilidade Escolhida: [deep_purple]{list(self.habilidades.keys())[atk-1]}[/]", self)
                    if atk == 1:
                        inimigo.vida -= 40

                        exibe(f"{self.nome} Núvens negras cobrem o céu..\n[deep_purple]Diversos relâmpagos[/]"
                              f" de repente caem sobre [deep_purple]{inimigo.nome}[/]"
                              f"[red]{inimigo.nome}[/] Recebe [red]40[/] de dano e ficará [red]paralizado[/]", self, inimigo)
                        inimigo.efeitos.append(Paralizado(2))
                        break
                    elif atk == 2:
                        self.ctrlinvoc()
                        exibe("[deep_purple]Bebê Dragão[/] foi invocado! \nEle pode"
                              " [deep_purple]atacar o inimigo[/] ou [deep_purple]curar o mago[/] por 2 rodadas")
                        break

    def ctrlinvoc(self):
        if self.dragao == None:
            self.dragao = Dragao()
        return

class Dragao:
    def __init__(self):
        self.nome = "Bebê Dragão"
        self.turnos_restantes = 2
        self.ataques = {"bola de fogo": 10, "Chicote de Cauda":20, "Dentada violenta":20}

    def decida(self, principal, inimigo):
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
        self.ataques = {"Ataque Com Adaga": self.danobase * 0.8, "Arremessar Faca":self.danobase * 0.8, "Esquiva": self.danobase * 0}
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
            exibe(f"[blue]{self.nome}[/] se aproxima rapidamente de inimigo e aplica [blue]diversos golpes[/]\n"
                  f"[red]{inimigo.nome}[/] ficará [red]atordoado por 2 rodadas[/]", self)
            inimigo.efeitos.append(Atordoado(2))
        elif atk == 2:
            exibe(f"[bright_yellow]{self.nome}[/] de repente fica muito rapido.\n "
                  f"[bright_yellow]{self.nome}[/] fazer [bright_yellow]2 açoes no proximo turno[/]", self)
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

        exibe(f"Minotauro escolheu {list(self.ataques.keys())[sorteado]}", self, sorteado)
        dmg = dano(self, inimigo)
        return dmg

    def curar(self):
        sorteado = randint(20, 30)
        self.vida += sorteado
        exibe(f"[red]Minotauro[/] recuperou [bright_yellow]{sorteado}[/] pontos de vida", sorteado)
        return

    def hability(self, principal):
        sorteado = randint(0,1)
        exibe(f"Habilidade Escolhida: {list(self.habilidades.keys())[sorteado]}", self, sorteado)
        if sorteado == 0:
            exibe("Minotauro se preprara para chifrar..")
            principal.efeitos.append(Atordoado(2))
        if sorteado == 1:
            exibe("Minotauro solta um grito ensurdecedor")
            self.efeitos.append(Furia(3))

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

        exibe(f"Curupira escolheu {list(self.ataques.keys())[sorteado]}", self, sorteado)
        dmg = dano(self, inimigo)
        return dmg

    def curar(self):
        sorteado = randint(20, 30)
        self.vida += sorteado
        exibe(f"[red]Curupira[/] recuperou [bright_yellow]{sorteado}[/] pontos de vida", sorteado)

        return

    def hability(self, principal):
        sorteado = randint(0,1)
        exibe(f"Habilidade Escolhida: {list(self.habilidades.keys())[sorteado]}", self, sorteado)
        if sorteado == 0:
            exibe("Curupira toca o berrante e chama uma enxurrada de animais")
            principal.vida -= 40
            principal.efeitos.append(Atordoado(2))
        if sorteado == 1:
            exibe("De repente, você começa a ouvir um assobio hipnotizante..")
            exibe(f"{principal.nome} está preso na ilusão de curupira", principal)
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
        sorteado = randint(0, 2)

        exibe(f"Nessie escolheu {list(self.ataques.keys())[sorteado]}", self, sorteado)
        dmg = dano(self, inimigo)
        return dmg

    def curar(self):
        sorteado = randint(20, 30)
        self.vida += sorteado
        exibe(f"[red]Nessie[/] recuperou [bright_yellow]{sorteado}[/] pontos de vida", sorteado)

        return

    def hability(self, principal):
        sorteado = randint(0,1)
        exibe(f"Habilidade Escolhida: {list(self.habilidades.keys())[sorteado]}", self, sorteado)
        if sorteado == 0:
            exibe(f"Nissie prepara um jato de água compressurizada e atira na direção de {principal.nome}", principal)
            principal.vida -= 40
            principal.efeitos.append(Atordoado(2))
        if sorteado == 1:
            exibe("Nissie te abocanha e num rapido movimento tenta te levar para debaixo da água")
            exibe(f"[blue]Debaixo da água Nissie tem aumento de ataque e cura[/]")
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
        print(inimigo.__dict__)

    def atualizar(self, inimigo):
        inimigo.danobase /= 0.6

class Paralizado(Efeitos):
    def __init__(self, duracao):
        super().__init__("Paralizado", duracao, "Debuff")

    def aplicar(self, principal = None, inimigo = None):
        for i in range(randint(1,2)):
            print(f"{inimigo.nome} está atordoado")
            turno_jogador(principal, inimigo)

class Perdido(Efeitos):
    def __init__(self):
        super().__init__("Lost", 3, "Debuff")

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

mer = Mercenario("laion", 30, 25)
enemy = Curupira()
combate(mer, enemy)