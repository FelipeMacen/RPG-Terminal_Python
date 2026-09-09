from rich import print
from rich.panel import Panel
from time import sleep
from rich.live import Live
import os

def exibe(txt_completo, obj=None, secundario= None, terceiro=None, time=0.04):
    txt_atual = ""
    painel = Panel(txt_atual, width=120, border_style="yellow")
    with Live(painel, refresh_per_second=25) as live:
        for letra in txt_completo:
            txt_atual += letra
            live.update(Panel(txt_atual, width=80, border_style="yellow"))
            sleep(time)

def limpa():
    os.system('cls' if os.name == 'nt' else 'clear')
    for _ in range(3):
        print(".", end= "")
        sleep(0.1)

def enter():
    while True:
        print("Pressione [green][ENTER][/] para continuar...")
        if input() == "":
            break
