from exploracao import *


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
        principal = criacao()
    else:
        return

    limpa()

    exibe(f"Olá [green]{principal.nome}[/]! Seja bem vindo ao mundo de MistyLand. \n"
          f"No Mundo de MistyLand existem duas principais forças dominantes.", principal, time=0.02)

    if principal.__class__.__name__ == "Cavaleiro":#Parafina(Vem do petroleo) e Drake (Edwin Drake) por causa do Petróleo.
        exibe(
            "Uma dessas forças é um reino chamado [blue]Parafina[/]. Onde o [blue]Rei Drake[/], "
            "com sua potência militar de cavaleiros, conquistaram seu espaço no mapa vencendo guerras e principalmente"
            " após a descoberta de um é um [blue]combustível fóssil[/] líquido, oleoso e inflamável, "
            "que foi usado como energia por esse reino para criar diversas evoluções."
        , time=0.02)
        enter()
        exibe(f"[bright_blue]{principal.nome}[/] é um comandante de um grupo especializado em [bright_blue]investigações"
              f" secretas[/] do reino. Um dia, você é convocado pelo próprio [blue]Rei Drake[/] para tratarem de um "
              f"assunto...", principal, time = 0.02)
        enter()
        exibe(f"[blue]Drake: [/]Seja bem vindo [bright_blue]{principal.nome}[/]! Preciso de sua ajuda pois"
              f" estão surgindo rumores de um [blue]grupo secreto[/] que estaria desenvolvendo uma [blue]nova fonte de energia.[/]"
              f" Nós já fomos muito prejudicados por causa daqueles [blue]nerds de Spell Town[/], preciso que você investigue"
              f" esses rumores mais a fundo...", principal, time=0.02)

    if principal.__class__.__name__ == "Mago":
        exibe(
            "Uma dessas forças é um lugar chamado [purple]Spell Town[/]. Onde [purple]Gargamel[/], o mestre dos magos, juntou"
            " muitos sábios e estudiosos, para pesquisarem uma fonte de energia gerada pelo movimento de partículas minúsculas"
            "que possuem [purple]carga elétrica negativa[/]. A pesquisa foi um sucesso e Spell Town, através de muitas evoluções"
            " geradas por essa energia, conquistou seu lugar no mundo de MistyLand."
        , time=0.02)
        enter()
        exibe("Um dia, gargamel te chama para uma [purple]reunião confidencial...[/]", principal, time=0.02)
        enter()
        exibe(f"[purple]Gargamel: [/] Olá {principal.nome}! ainda bem que te encontrei. Nós do conselho [purple]estamos em agonia"
              f" [/]porque estão surgindo rumores de uma nova [purple]organização secreta[/] que possui uma fonte de energia com o"
              f" [purple]portencial muito maior que a nossa[/]. Como nós do alto escalão somos conhecidos por todas as terras de"
              f" MistyLand, quero que você [purple]investigue[/] essa questão por nós...", principal, time=0.02)

    if principal.__class__.__name__ == "Mercenario":
        exibe(
            " Uma delas é [blue]Parafina[/], um reino que prosperou muito após a descoberta de uma fonte de energia vinda de um "
            "[blue]combustível fóssil[/] líquido, oleoso e inflamável.\n"
            " A segunda por sua vez, se chama [purple]Spell Town[/]. Uma cidade que teve sua ascensão após descobrir uma "
            "fonte de energia através da manipulação de [purple]cargas elétricas negativas[/] de particulas subatômicas."
        , time=0.02)
        enter()
        limpa()
        exibe(f"Nosso herói [bright_yellow]{principal.nome}[/], vive em um mundo diferente...\n"
              f"Um pequeno vilarejo chamado [bright_yellow]WhosTown[/]. Uma terra quase que sem lei, abandonada por todos.", principal,time=0.02)
        enter()
        limpa()
        exibe(f"Porém, talvez sua vida pudesse mudar...\n [bright_yellow]{principal.nome}[/] faz "
              f"parte da [bright_yellow]linha de frente[/] de um grupo de mercenários...\n"
              f"[yellow]Barney[/], o [yellow]líder[/] dos mercenários, pela enorme confiança que tem em [bright_yellow]{principal.nome}[/],"
              f" o chama para uma conversa em particular...", principal, time=0.02)
        enter()
        exibe(f"[yellow]Barney: [/]Tudo bem garoto? Tenho uma [yellow]missão secreta[/] para você."
              f" Fontes confiáveis de dentro do reino de Parafina, me contaram que o rei está agoniado por ter chego aos seus"
              f" ouvidos, rumores de que uma [yellow]organização secreta[/] esteja descobrindo uma [yellow]nova fonte de energia[/]."
              f" Como você é um dos mais antigos dos nossos, preciso que [yellow]busque mais informações[/] sobre isso. "
              f"Se conseguirmos 'morder uma fatia' dessa nova energia, talvez [yellow]nossas vidas possam melhorar[/]...", principal, time= 0.02)

    enter()
    limpa()
    exibe(f"Logo após receber sua primeira missão...")
    dscrt = controla_exploracao(principal, "vila")

#Funcionalidade que controla toda a parte de criação do personagem.
def criacao():
    limpa()
    infs = []
    while True:
        try:
            while True:
                exibe("\nEscolha uma classe:\n[1] [bright_blue]Cavaleiro[/]\n[2] [purple]Mago[/]\n[3] [bright_yellow]Mercenário[/]\n")
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
                exibe("\n[bright_blue]Classe Cavaleiro[/]:\n"
                      "Defesa: 30.\n"
                      "Arma Principal: Espada e Escudo\n"
                      "Ataques Básicos: Ataque Com Espada, Aparo, Esquiva\n"
                      "Habilidades Especias: [blue]Ataque Pesado[/] (causa [red]40 pontos de dano[/] ao inimigo e o deixa [red]atordoado por 3 rodadas[/])"
                      " e [blue]Bloqueio Com Escudo[/](defesa do cavaleiro é aumentada em [blue]30% por 3 rodadas[/])", time=0.01)
            elif infs[0] == 2:
                exibe("\n[purple]Classe Mago[/]:\n"
                      "Defesa: 20.\n"
                      "Armas Principais: Cajado e Livro de Magias.\n"
                      "Ataques Básicos: Ataque Com Cajado, Bola de Fogo, Teletransporte\n"
                      "Habilidades Especias: [purple]Chuva de Relâmpagos[/](causa [red]40 de dano[/] ao inimigo e o deixa [red]paralizado[/] "
                      "por uma ou duas rodadas) e [purple]Invocação Amiga[/](invoca um [purple]Bebê Dragão[/] que pode atacar o inimigo"
                      "ou curar o mago por 2 rodadas)", time=0.01)
            elif infs[0] == 3:
                exibe("\n[bright_yellow]Classe Mercenário[/]:\n"
                      "Defesa: 25.\n"
                      "Armas Principais: Adagas Duplas e Facas arremessaveis.\n"
                      "Ataques Básicos: Ataque Com Adaga, Chute Giratório, Arremessar Faca\n"
                      "Habilidades Especias: [bright_yellow]Investida Vorpal[/](causa [red]40 de dano[/] e pode deixar o inimigo [red]atordoado[/]) "
                      "e [bright_yellow]Filho da luz[/] (mercenario fará [bright_yellow]2 ações[/] no próximo turno)", time=0.01)
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

    principal = "nada"
    match infs[0]:
        case 1:
            principal = Cavaleiro(infs[1], 30, 30)
        case 2:
            principal = Mago(infs[1], 20, 30)
        case 3:
            principal = Mercenario(infs[1], 25, 30)

    return principal

menuinicial()
