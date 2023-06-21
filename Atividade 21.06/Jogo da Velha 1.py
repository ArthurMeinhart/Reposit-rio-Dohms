import tkinter as tk
from tkinter import messagebox

class JogoDaVelha:
    def __init__(self):
        self.jogador = 'X'
        self.tabuleiro = [['' for _ in range(3)] for _ in range(3)]
        self.vitorias_x = 0
        self.vitorias_o = 0
        self.empates = 0
        
        self.janela = tk.Tk()
        self.janela.title('Jogo da Velha')
        
        self.botoes = []
        for i in range(3):
            linha = []
            for j in range(3):
                botao = tk.Button(self.janela, text='', width=8, height=4, font=('Arial', 20),
                                  command=lambda i=i, j=j: self.fazer_jogada(i, j))
                botao.grid(row=i, column=j, padx=5, pady=5)
                linha.append(botao)
            self.botoes.append(linha)
        
        self.label_vitorias = tk.Label(self.janela, text='Vitórias\n\nX: 0\nO: 0\nEmpates: 0', font=('Arial', 14))
        self.label_vitorias.grid(row=3, columnspan=3, pady=10)
        
        self.estilo_botao = tk.style() 
        # O programa está dando erro para iniciar pois o ChatGPT usou o módulo "style", que não foi importado para este código. 

        # Eu disse para ele usar a biblioteca "tkinter", mas o módulo "style" só existe na biblioteca "tkinter.font". O ChatGPT provavelmente errou pois eu não disse para 
        # ele usar outra biblioteca, apenas a "tkinter", então mesmo ele usando métodos de outras bibliotecas, eu não dei a liberdade para ele importá-las.

        self.estilo_botao.configure('Win.TButton', font=('Arial', 20, 'bold'))
        
    def fazer_jogada(self, linha, coluna):
        if self.tabuleiro[linha][coluna] == '':
            self.tabuleiro[linha][coluna] = self.jogador
            self.botoes[linha][coluna].config(text=self.jogador, state='disabled')
            
            if self.verificar_vitoria():
                messagebox.showinfo('Fim de jogo', f'O jogador {self.jogador} venceu!')
                self.atualizar_vitorias()
                self.reiniciar_jogo()
            elif self.verificar_empate():
                messagebox.showinfo('Fim de jogo', 'Empate!')
                self.atualizar_empates()
                self.reiniciar_jogo()
            else:
                self.alterar_jogador()
    
    def verificar_vitoria(self):
        # Verificar linhas
        for i in range(3):
            if self.tabuleiro[i][0] == self.tabuleiro[i][1] == self.tabuleiro[i][2] != '':
                return True
        # Verificar colunas
        for j in range(3):
            if self.tabuleiro[0][j] == self.tabuleiro[1][j] == self.tabuleiro[2][j] != '':
                return True
        # Verificar diagonais
        if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] != '':
            return True
        if self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] != '':
            return True
        return False
    
    def verificar_empate(self):
        for linha in self.tabuleiro:
            if '' in linha:
                return False
        return True
    
    def alterar_jogador(self):
        self.jogador = 'O' if self.jogador == 'X' else 'X'
    
    def reiniciar_jogo(self):
        self.jogador = 'X'
        self.tabuleiro = [['' for _ in range(3)] for _ in range(3)]
        
        for i in range(3):
            for j in range(3):
                self.botoes[i][j].config(text='', state='normal')
    
    def atualizar_vitorias(self):
        if self.jogador == 'X':
            self.vitorias_x += 1
        elif self.jogador == 'O':
            self.vitorias_o += 1
        
        self.label_vitorias.config(text=f'Vitórias\n\nX: {self.vitorias_x}\nO: {self.vitorias_o}\nEmpates: {self.empates}')
    
    def atualizar_empates(self):
        self.empates += 1
        self.label_vitorias.config(text=f'Vitórias\n\nX: {self.vitorias_x}\nO: {self.vitorias_o}\nEmpates: {self.empates}')
    
    def iniciar(self):
        self.janela.mainloop()

jogo = JogoDaVelha()
jogo.iniciar()
