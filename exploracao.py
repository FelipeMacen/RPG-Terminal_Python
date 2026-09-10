from inimigos import *
from principais import *
import sys
from npcs import buscar_npc
from ia import *

def controla_exploracao(principal, local):
    while True:
        if local != "portoes":
            exibe(f"[blue]{principal.nome}[/] se encontra em {local}", time=0.03)
            enter()
        principal.mapa()

        if local == "vila":
            exibe("Por onde deseja seguir?\n[1]LAGO DO ESQUECIMENTO\n"
                  "[2]FLORESTA DA PERDIÇÃO\n[3]CAVERNA LABIRÍNTICA\n", time=0.03)
        elif local == "lago" or local == "floresta" or local == "caverna":
            exibe("Por onde deseja seguir?\n[1]VILA INICIAl\n[2]'?'", time=0.03)
        else:
            exibe(f"[blue]{principal.nome}[/] se encontra em frente a [red]enormes portões de prata.[/]", time=0.03)
            exibe("Por onde deseja seguir?\n[1]LAGO DO ESQUECIMENTO\n"
                  "[2]FLORESTA DA PERDIÇÃO\n[3]CAVERNA LABIRÍNTICA\n", time=0.03)

        resp = input()
        if local == "vila" or local == "portoes":
            match resp:
                case "1":
                    local = lago_do_esquecimento(principal)
                case "2":
                    local = floresta_da_perdicao(principal)
                case "3":
                    local = caverna_labirintica(principal)
                case _:
                    print("[red]Digite uma opção válida.[/]")
                    continue
        else:
            match resp:
                case "1":
                    local = vila_inicial(principal)
                case "2":
                    local = portoes(principal)
                case _:
                    print("[red]Digite uma opção válida.[/]")
                    continue


def vila_inicial(principal):
    exibe(f"[blue]{principal.nome}[/] se encontra na vila inicial")
    enter()
    exibe("O que deseja fazer?\n[1]Descansar\n[2]Mecadinho\n")
    resp = input()
    while True:
        match resp:
            case "1":
                descanso(principal)
                enter()
            case "2":
                mercadinho(principal)
            case _:
                continue
        break

    return "vila"


def descanso(principal):
    if principal.__class__.__name__ == "Cavaleiro":
        exibe(
            f"[blue]{principal.nome}[/] gasta algum tempo na academia pois isso o ajuda a colcoar os pensamentos em ordem. "
            f"Logo após ele volta para casa e tem uma boa noite de sono antes de prosseguir viagem...")
        principal.vida = 100
        exibe(f"[green]Vida regenerada\nCheck Point atualizado[/]")
        enter()
    elif principal.__class__.__name__ == "Mago":
        exibe(
            f"[purple]{principal.nome}[/] passa na [purple]biblioteca de Spell Town[/]"
            f" em busca de alguma resposta para os estranhos acontecimentos da jornada. E após algumas horas de leitura"
            f"vai para casa descansar antes de prosseguir na sua jornada...")
        principal.vida = 100
        exibe(f"[green]Vida regenerada\nCheck Point atualizado[/]")
        enter()
    else:
        exibe(
            f"[bright_yellow]{principal.nome}[/] volta para sua humilde vila antes de prosseguir viagem. Encontra bons amigos no caminho"
            f" e finalmente chega em casa, onde é recebido com muito amor por todos da familia...")
        principal.vida = 100
        exibe(f"[green]Vida regenerada\nCheck Point atualizado[/]")
        enter()


def mercadinho(principal):
    exibe(f"[blue]{principal.nome}[/] chega ao [light_salmon1]mercadinho do Rudolf[/]:")
    enter()
    while True:
        exibe("OPÇÕES:\n"
              f"[bright_yellow]Dinheiro de {principal.nome}: {principal.dinheiro}[/]"
              "[0]Voltar\n"
              "[1]Item de Cura [bright_yellow](10 moedas)[/]\n"
              "[2]Em breve\n"
              "[3]Em breve\n"
              "Qual item deseja comprar?\n")
        resp = input()
        match resp:
            case "0":
                break
            case "1":
                if principal.dinheiro >= 10:
                    principal.dinheiro -= 10
                    principal.inventario[list(principal.inventario.keys())[1]] += 1
                else:
                    exibe("[red]dinheiro insuficiente[/]")
            case _:
                continue


def lago_do_esquecimento(principal):
    limpa()

    if "[blue]Mascara de Agua[/]" in principal.inventario:
        exibe(f"[blue]{principal.nome}[/] se encontra no lago onde anteriormente derretou [red]Nessie[/].")
        enter()
        limpa()
        evento_aleatorio(principal, "lago")
        return "lago"
    else:
        evento_aleatorio(principal, "lago")
        enter()
        limpa()
        try:
            npc(principal, "lago")
        except:
            print("[red]Ocorreu algum erro ao tentar executar o envento de interação com npc.[/]")

        exibe(
            f"Após algumas horas... Você se vê sozinho em um [red]imenso e denso lago...[/]")
        enter()
        exibe(f"{principal.nome} olha para baixo e percebe que é como se"
            f" algo enorme estivesse se movimentando no fundo do lago. "
            f"[blue]{principal.nome}[/] ainda pensa em voltar, mas antes mesmo de qualquer possível reação.."
            f"\n[red]O Monstro Do Lago Aparece: NESSIE[/]", obj=principal)

        enter()
        if combate(principal, Nessie()):
            exibe("[red]Nessie derrotado[/]!...\n")
            enter()
            limpa()
            exibe("Após a derrota, o corpo do monstro permanece boiando de barriga para cima na água.")
            enter()
            exibe(f"[blue]{principal.nome}[/] percebe que tem algo como uma [bright_blue]Máscara[/] presa ao peito de Nissie."
                  f"[blue]{principal.nome}[/] se aproxima e com pouco esforço arranca a máscara do peito de Nessie.")
            exibe(f"[bright_blue]Máscara de água[/] adicionada ao inventário do jogador.")
            enter()
            limpa()
            principal.inventario["[blue]Mascara de Agua[/]"] = 1
            exibe("Deseja abrir o inventário?\n[1]Sim\n[2]Não\n")
            resp = input()
            if resp == "1":
                inventario(principal)
        else:
            if principal.vida <= 0:
                exibe("[red]GAME OVER[/]\nretornando para o último checkpoint...")
                principal.vida = 100
                return "lago"
            else:
                exibe(f"[blue]{principal.nome} fugiu![/]")
                return "lago"


def floresta_da_perdicao(principal):
    limpa()
    if "[green]Máscara de Folha[/]" in principal.inventario:
        exibe(f"[blue]{principal.nome}[/] retorna para a floresta onde derretou [red]Curupira[/].")
        enter()
        return "floresta"
    else:
        evento_aleatorio(principal, "floresta")
        enter()
        limpa()
        try:
            npc(principal, "floresta")
        except:
            print("[red]Ocorreu algum erro ao tentar executar o envento de interação com npc.[/]")

        exibe("Após muito vagar na densa floresta..\nVocê começa a ouvir [red]longos assobios..[/]\n"
              f"[blue]{principal.nome}[/] vai ficando cada vez mais [red]zonzo e perdido...[/]")
        exibe(f"Quando se da conta, você está totalmente [red]perdido, no coração da floresta.[/] Quando de repente...\n"
              f"[red]CURUPIRA aparece[/]", obj=principal)

        enter()
        if combate(principal, Curupira()):
            exibe("[red]Curupira derrotado![/]...\n")
            enter()
            limpa()
            exibe(
                "Com a queda do corpo de Curupira, todos os animais fazem um [red]barulho ensurcedor[/] e grande tumulto se"
                "instaura na floresta...")
            enter()
            exibe(f"[blue]{principal.nome}[/] percebe que a[green]Máscara[/] de curupira começa a  brilhar.."
                  f"[blue]{principal.nome}[/] se aproxima e com pouco esforço arranca a [green]máscara de curupira[/].")
            exibe(f"[green]Mascara de Folha[/] adicionada ao inventário do jogador.")
            enter()
            limpa()
            principal.inventario["[green]Máscara de Folha[/]"] = 1
            exibe("Deseja abrir o inventário?\n[1]Sim\n[2]Não\n")
            resp = input()
            if resp == "1":
                inventario(principal)
        else:
            if principal.vida <= 0:
                exibe("[red]GAME OVER[/]\nretornando para o último checkpoint...")
                principal.vida = 100
                return "floresta"
            else:
                exibe(f"[blue]{principal.nome}[/] fugiu!")
                return "floresta"


def caverna_labirintica(principal):
    limpa()
    if "[dark_orange3]Mascara de Pedra[/]" in principal.inventario:
        exibe(f"[blue]{principal.nome}[/] retorna para caverna onde teve seu terrível confronto com [red]Minotauro[/]")
        evento_aleatorio(principal, "caverna")
        return "caverna"
    else:
        while True:
            evento_aleatorio(principal, "caverna")
            enter()
            limpa()
            try:
                npc(principal, "caverna")
            except:
                print("[red]Ocorreu algum erro ao tentar executar o envento de interação com npc.[/]")


            exibe("Após vagar muito no labirinto... Você encontra uma figura estranha. Algo como um [red]urso com chifres[/]"
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
            exibe("[red]Minotauro derrotado![/]...\n")
            enter()
            limpa()
            exibe("Seu enorme corpo [red]despenca para frente[/] causando grande estrondo em toda a caverna...")
            enter()
            exibe(
                f"[blue]{principal.nome}[/] percebe que tem algo como uma [dark_orange3]Máscara[/] presa nas costas de minotauro."
                f"[blue]{principal.nome}[/] se aproxima e com pouco esforço arranca a [dark_orange3]máscara das costas de Minotauro[/].", principal)
            exibe(f"[dark_orange3]Máscara de Pedra[/] adicionada ao inventário do jogador.")
            enter()
            limpa()
            principal.inventario["[dark_orange3]Mascara de Pedra[/]"] = 1
            exibe("Deseja abrir o inventário?\n[1]Sim\n[2]Não\n")
            resp = input()
            if resp == "1":
                inventario(principal)
        else:
            if principal.vida <= 0:
                exibe("[red]GAME OVER[/]\nretornando para o último checkpoint...")
                principal.vida = 100
                return "caverna"
            else:
                exibe(f"[bright_yellow]{principal.nome} fugiu![/]")
                return "caverna"


def portoes(principal):
    exibe(f"[blue]{principal.nome}[/] se encontra em frente a um [red]portão de porta dupla[/] enorme e de prata...")
    enter()
    limpa()
    exibe("Nesse portão tem [red]três rostos de estatuas[/] e uma mensagem abaixo...\n"
          "Prove sua força aventureiro, colocando no portão as [red]máscaras dos guardiões[/].")
    enter()
    for i in range(2, len(principal.inventario)):
        if list(principal.inventario.values())[i] == 1:
            while True:
                exibe(f"Deseja inserir {list(principal.inventario.keys())[i]} no rosto da estátua?\n"
                      f"[1]Sim\n[2]Não\n", principal)
                resp = input()
                match resp:
                    case "1":
                        exibe(
                            f"[blue]{principal.nome}[/] insere {list(principal.inventario.keys())[i]} em um dos rostos das estatuas.")
                        principal.inventario[list(principal.inventario.keys())[i]] = 0
                        break
                    case "2":
                        break
                    case _:
                        print("Digite uma opção válida")
                enter()

    if len(principal.inventario) == 5 and list(principal.inventario.values())[2] == 0 and \
            list(principal.inventario.values())[3] == 0 and list(principal.inventario.values())[4] == 0:
        exibe("Os enormes portões começam a [red]tremer[/] assim como os muros que o cercam...")
        enter()
        exibe("Lentamente eles vão se abrindo e uma [red]névoa densa[/] começa a sair de dentro do ambiente...")
        enter()
        exibe("[green]Continua...[/]")
        exibe("Obrigado por ter jogado até aqui o primeiro capítulo de MistyLand.")
        enter()
        sys.exit(0)
    else:
        return "portoes"

def evento_aleatorio(principal, lugar):
    sorteado = randint(1, 2)

    match sorteado:
        case 1:
            item_aleatorio(principal, lugar)
        case _:
            nada_acontece(principal, lugar)


def npc(principal, lugar):#ESSA FUNÇÃO VAI MUDAR TOTALMENTE.
    while True:
        match lugar:
            case "lago":
                chave = "pescador"
                exibe(f"{principal.nome} avista um [yellow]velho pescador[/] e decide parar para conversar...")
                enter()
                break
            case "floresta":
                chave = "aventureiro"
                exibe(f"{principal.nome} avista um [green]aventureiro[/] e decide parar para conversar...")
                enter()
                break
            case "caverna":
                chave = "mascarado"
                exibe(f"{principal.nome} avista um [red]homem mascarado bizarro[/] e decide parar para conversar...")
                enter()
                break
            case _:
                raise PermissionError("Não tem como")

    dados_npc = buscar_npc(chave)
    conversa = ConversaNpc(dados_npc)

    while True:
        exibe("[0] Sair")
        mensagem = input("Digite a mensagem: ")
        if mensagem == "0":
            exibe("saindo...")
            limpa()
            break

        resultado = conversa.enviar(mensagem)

        exibe(f"{dados_npc['nome']}: {resultado['fala']}\n")
        enter()
        limpa()
        if resultado["encerrar"]:
            exibe(f"{dados_npc['nome']} começa a se a afastar e encerra a conversa.")
            break
    #aventureiro,pescador e mascarado
#AQUI É SÓ VER O LUGAR. E CHAMAR O NPC DE ACORDO.


def item_aleatorio(principal, lugar):
    sorteado = randint(0, 2)
    if lugar == "lago":
        exibe(f"{principal.nome} [yellow]avista um bote abandonado[/] vindo em sua direção. Ao vasculhar",
              obj=principal)
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
                    exibe("O caderno de anotações está com diversas folhas rasgadas. Mas as poucas restantes dizem:\n"
                          "...Esses caras são [red]insanos[/]. Tive que rasgar a maioria das folhas do meu diário para"
                          " não descobrirem. Eles pretendem dominar o mundo com a [bright_magenta]EPI[/]."
                          f"Estão pensando até em colocar algum tipo de [red]Guardião[/] nesse lugar!"
                          f"Se alguém encontrar esse diário, [red]fuja imediatamente desse lugar[/].")
                case _:
                    exibe(f"[blue]{principal.nome}[/] devolve o caderno de anotações e continua sua aventura.", obj=principal)


def nada_acontece(principal, lugar):
    if lugar == "lago":
        exibe(
            f"{principal.nome} [yellow]avista um bote abandonado[/] vindo em sua direção. Deseja verificar se encontra algo?\n"
            f"[1] Sim\n[2] Não\n", obj=principal)
        input()
        exibe(f"[blue]{principal.nome}[/] Não encontra nada no bote.", obj=principal)
    elif lugar == "floresta":
        exibe(
            f"{principal.nome} [yellow]Encontra uma bolsa[/] velha jogada perto de uma arvóre. Deseja verificar se encontra algo?\n"
            f"[1] Sim\n[2] Não\n", obj=principal)
        input()
        exibe(f"[blue]{principal.nome}[/] Não encontra nada na bolsa.", obj=principal)
    elif lugar == "caverna":
        exibe(f"{principal.nome} [yellow]encontra um báu[/]. Deseja verificar se encontra algo?\n"
              f"[1] Sim\n[2] Não\n", obj=principal)
        input()
        exibe(f"[blue]{principal.nome}[/] Não encontra nada no baú.", obj=principal)
    else:
        print("[red]erro[/]")
        pass