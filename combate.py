from utils import *
from random import randint

def combate(principal, inimigo):
    while True:
        for efeito in principal.efeitos:
            efeito.aplicar(principal, inimigo)

        if principal.vida <= 0:
            return False

        fugir = turno_jogador(principal, inimigo)
        enter()
        limpa()
        if inimigo.vida > 0:
            principal.atualizar_efeito()
        if principal.vida <= 0:
            return False
        if inimigo.vida <= 0:
            return True

        if fugir == True:
            break

        try:
            if principal.dragao != None:
                principal.dragao.decida(principal, inimigo)
        except:
            pass

        if inimigo.vida <= 0:
            exibe("[purple]Bebê Dragão[/] matou o inimigo!")
            return True

        if fugir == "esquiva":
            continue

        for efeito in inimigo.efeitos:
            efeito.aplicar(inimigo, principal)

        for item in inimigo.efeitos:
            atual = item
            if item.__class__.__name__ == "Paralizado":
                break
            else:atual = None
        if len(inimigo.efeitos) == 0:
            atual = None
        try:
            if atual.__class__.__name__ == "Paralizado":
                exibe(f"{inimigo.nome} está [red]paralizado[/]", inimigo)
                inimigo.atualizar_efeito()
                enter()
                continue
        except:
            limpa()
        turno_inimigo(principal, inimigo)
        enter()
        if fugir == "reset_escudo":
            principal.atualiza_defesa()
        if principal.vida > 0:
            inimigo.atualizar_efeito()
        if principal.vida <= 0:
            return False
        if inimigo.vida <= 0:
            return True


def turno_jogador(principal, inimigo):
    while True:
        limpa()
        exibe(f"Sua vida: {int(principal.vida)}\n"
              f"Vida do inimigo: {int(inimigo.vida)}")
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
                    return False
                case 2:
                    defender(principal, inimigo)
                    return "reset_escudo"
                case 3:
                    exibe("Deseja usar qual item:\n")
                    if inventario(principal, inimigo) == "cancel":
                        continue
                    break
                case 4:
                    return True
                case _:
                    continue

    return False

def turno_inimigo(principal, inimigo):
    while True:
        decisao = randint(0, 1)

        match decisao:#talvez fazer um defender depois
            case 0:#atacar
                if inimigo.carrega >= 100:
                    inimigo.hability(principal)
                    inimigo.carrega = 0
                    return
                dmg = inimigo.atacar(principal)
                inimigo.carrega += 25

                exibe(f"[blue]{principal.nome}[/] recebeu [red]{int(dmg)}[/] de dano", obj=principal, secundario=dmg)
                return
            case 1:#curar
                if inimigo.vida > 69:
                    continue
                inimigo.curar()
                return
            case _:
                print("opção errada")

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
            resultado = principal.hability(inimigo)
            if resultado == "cancel":
                continue
            else:
                principal.carrega = 0
                return

        if list(principal.ataques.keys())[resp-1] != "Esquiva" and list(principal.ataques.keys())[resp-1] !="Teletransporte":
            dmg = dano(principal, inimigo, resp-1)
            exibe(f"[red]{inimigo.nome}[/] recebeu [red]{int(dmg)}[/] de dano.", dmg)
            principal.carrega += 25
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


def dano(principal, vitima, atk):
    vitima.vida -= principal.danobase * list(principal.ataques.values())[atk] - principal.danobase * list(principal.ataques.values())[atk] * vitima.defesa / 100
    return principal.danobase * list(principal.ataques.values())[atk] - principal.danobase * list(principal.ataques.values())[atk] * vitima.defesa / 100

def defender(principal, inimigo):
    limpa()
    principal.defesa += principal.defesa * 0.20

    exibe(f"{principal.nome} defenderá o dano parcialmente! [blue](defesa aumentada em 20%)[/]")


def inventario(principal, inimigo= None):
    cont = 1
    conteudo = "\n[0]Sair\n"
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
                            exibe(str(principal.curar()), principal)
                            principal.inventario[list(principal.inventario.keys())[1]] -= 1
                        else:
                            exibe("vida já está no máximo")
                            enter()
                            return "cancel"
                    else:
                        pass
            break

    return