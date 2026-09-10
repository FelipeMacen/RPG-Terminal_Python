import json


def buscar_npc(chave):
    with open("dados/npcs.json", encoding="utf-8") as arquivo:
        npcs = json.load(arquivo)

    return npcs[chave]