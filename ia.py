from ollama import chat
import json

formato ={
    "type": "object",
    "properties": {
        "fala": {"type": "string"},
        "emocao": {"type": "string"},
        "encerrar": {"type": "boolean"},
    },
    "required": ["fala", "emocao", "encerrar"],
}

class ConversaNpc:
    def __init__(self, dados):
        self.dados = dados
        self.historico = [
            {
            "role": "system", "content": self.prompt()
            }
        ]

    def prompt(self):
        conhecimentos = ""
        for item in self.dados["conhecimentos"]:
            conhecimentos += "," + item

        return (
            f"Você é {self.dados['nome']}, um npc de um jogo rpg.\n"
            f"Sua personalidade é: {self.dados['personalidade']}.\n"
            f"Seu objetivo nessa conversa é: {self.dados['objetivo']}.\n"
            f"O que você sabe: {conhecimentos}.\n"
            f"Responda sempre em português, mantendo-se no personagem. Não invente conhecimento que não foi listado acima."
        )

    def enviar(self, mensagem):
        self.historico.append({
            "role": "user", "content": mensagem
        })

        resposta = chat(
            model = "gemma3:4b", messages = self.historico, format = formato
        )

        self.historico.append({
            "role": "assistant", "content": resposta.message.content
        })
        return json.loads(resposta.message.content)

