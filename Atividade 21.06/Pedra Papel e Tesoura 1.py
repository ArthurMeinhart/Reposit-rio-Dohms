import tkinter as tk
from tkinter import messagebox
import random

# O erro deste código está na linha 67



# Função para verificar o vencedor
def verificar_vencedor(escolha_jogador, escolha_computador):
    if escolha_jogador == escolha_computador:
        return "Empate"
    elif (
        (escolha_jogador == "Pedra" and escolha_computador == "Tesoura")
        or (escolha_jogador == "Papel" and escolha_computador == "Pedra")
        or (escolha_jogador == "Tesoura" and escolha_computador == "Papel")
    ):
        return "Jogador"
    else:
        return "Computador"

# Função para processar a escolha do jogador
def processar_escolha(escolha_jogador):
    escolhas = ["Pedra", "Papel", "Tesoura"]
    escolha_computador = random.choice(escolhas)
    resultado = verificar_vencedor(escolha_jogador, escolha_computador)

    if resultado == "Empate":
        messagebox.showinfo("Resultado", "Empate!")
    elif resultado == "Jogador":
        messagebox.showinfo("Resultado", "Você venceu!")
        contagem_partidas["jogador"] += 1
    else:
        messagebox.showinfo("Resultado", "O computador venceu!")
        contagem_partidas["computador"] += 1

    contagem_partidas["empates"] += 1 if resultado == "Empate" else 0
    atualizar_contagem()

    if contagem_partidas["jogador"] == 2 or contagem_partidas["computador"] == 2:
        resultado_final()

# Função para atualizar a contagem de vitórias, derrotas e empates
def atualizar_contagem():
    texto_contagem.set(
        f"Vitórias: {contagem_partidas['jogador']} "
        f"Derrotas: {contagem_partidas['computador']} "
        f"Empates: {contagem_partidas['empates']}"
    )

# Função para exibir o resultado final
def resultado_final():
    if contagem_partidas["jogador"] == 2:
        messagebox.showinfo("Resultado Final", "Você venceu a melhor de 3 partidas!")
        contagem_geral["vitorias"] += 1
    elif contagem_partidas["computador"] == 2:
        messagebox.showinfo("Resultado Final", "O computador venceu a melhor de 3 partidas!")
        contagem_geral["derrotas"] += 1

    reiniciar_partida()

# Função para reiniciar a contagem e permitir uma nova partida
def reiniciar_partida():
    contagem_partidas["jogador"] = 0
    contagem_partidas["computador"] = 0
    contagem_partidas["empates"] = 0
    atualizar_contagem()

    #Nessa difinição de reiniciar a partida, apenas a contagem é atualizada, a função de contagem geral não é chamada. 
    #O ChatGPT fez o código para que ele contabilize a contagem geral, e fez a interface em que as exibe, mas esqueceu de atualizar essa interface quando o jogo é reinciiado. 

# Criação da janela principal
janela = tk.Tk()
janela.title("Pedra, Papel e Tesoura")
janela.geometry("600x300")  # Definindo o tamanho da janela

# Estilo para os botões
estilo_botao = {
    "font": ("Arial", 14),
    "width": 10,
    "height": 2,
    "bd": 0,
}

# Criação dos botões
botao_pedra = tk.Button(janela, text="Pedra", command=lambda: processar_escolha("Pedra"), **estilo_botao, bg="lightblue")
botao_pedra.pack(pady=10)

botao_papel = tk.Button(janela, text="Papel", command=lambda: processar_escolha("Papel"), **estilo_botao, bg="lightgreen")
botao_papel.pack(pady=10)

botao_tesoura = tk.Button(janela, text="Tesoura", command=lambda: processar_escolha("Tesoura"), **estilo_botao, bg="lightpink")
botao_tesoura.pack(pady=10)

# Contagem de vitórias, derrotas e empates nas partidas atuais
contagem_partidas = {"jogador": 0, "computador": 0, "empates": 0}
texto_contagem = tk.StringVar()
texto_contagem.set("Vitórias: 0 Derrotas: 0 Empates: 0")
label_contagem = tk.Label(janela, textvariable=texto_contagem, font=("Arial", 12))
label_contagem.pack(pady=10)

# Contagem de vitórias e derrotas nas partidas melhores de 3
contagem_geral = {"vitorias": 0, "derrotas": 0}
texto_contagem_geral = tk.StringVar()
texto_contagem_geral.set("Vitórias Gerais: 0 Derrotas Gerais: 0")
label_contagem_geral = tk.Label(janela, textvariable=texto_contagem_geral, font=("Arial", 12))
label_contagem_geral.pack(pady=10)

# Função para atualizar a contagem geral de vitórias e derrotas
def atualizar_contagem_geral():
    texto_contagem_geral.set(
        f"Vitórias Gerais: {contagem_geral['vitorias']} "
        f"Derrotas Gerais: {contagem_geral['derrotas']}"
    )

atualizar_contagem_geral()

# Execução da janela
janela.mainloop()
