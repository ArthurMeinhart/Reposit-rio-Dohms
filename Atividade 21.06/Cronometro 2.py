import tkinter as tk
import time

class Cronometro:
    def __init__(self, master):
        self.master = master
        self.tempo_inicial = 0
        self.tempo_passado = 0
        self.executando = False

        self.label_tempo = tk.Label(self.master, text="00:00:00.000", font=("Helvetica", 48))
        self.label_tempo.pack()

        frame_botoes = tk.Frame(self.master)
        frame_botoes.pack()

        self.botao_iniciar = tk.Button(frame_botoes, text="Iniciar", command=self.iniciar, font=("Helvetica", 14), width=10, height=10, relief=tk.GROOVE)
        self.botao_iniciar.pack(side=tk.LEFT, padx=10, pady=10)

        self.botao_parar = tk.Button(frame_botoes, text="Parar", command=self.parar, font=("Helvetica", 14), width=10, height=10, relief=tk.GROOVE)
        self.botao_parar.pack(side=tk.LEFT, padx=10, pady=10)

        self.botao_resetar = tk.Button(frame_botoes, text="Resetar", command=self.resetar, font=("Helvetica", 14), width=10, height=10, relief=tk.GROOVE)
        self.botao_resetar.pack(side=tk.LEFT, padx=10, pady=10)

    def iniciar(self):
        if not self.executando:
            self.tempo_inicial = time.time() - self.tempo_passado
            self.atualizar()
            self.botao_resetar.configure(state=tk.DISABLED) 
            # Para solucionar o problema, adicionei uma configuração de estado "DISABLE" (DESABILITADO) no botão resetar quando a função "iniciar" for executada
            # Assim, o botão não irá mais aparentar estar funcionando quando o cronômetro estiver rodando, forçando com que o usuário pare o cronômetro para usar a função de resetar

    def parar(self):
        if self.executando:
            self.master.after_cancel(self.contagem)
            self.tempo_passado = time.time() - self.tempo_inicial
            self.executando = False
            self.botao_resetar.configure(state=tk.NORMAL)  
            # Para o botão voltar a funcionar, também adicionei uma configuração de estado "NORMAL" no botão resetar quando a função "parar" for executada

    def resetar(self):
        self.tempo_passado = 0
        self.label_tempo.configure(text="00:00:00.000")

    def atualizar(self):
        self.executando = True
        tempo_atual = time.time() - self.tempo_inicial
        horas, resto = divmod(tempo_atual, 3600)
        minutos, segundos = divmod(resto, 60)
        segundos, milissegundos = divmod(segundos, 1)
        milissegundos = int(milissegundos * 1000)
        tempo_formatado = "{:02d}:{:02d}:{:02d}.{:03d}".format(int(horas), int(minutos), int(segundos), milissegundos)
        self.label_tempo.configure(text=tempo_formatado)
        self.contagem = self.master.after(1, self.atualizar)

root = tk.Tk()
root.title("Cronômetro")

largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()

largura_janela = 400
altura_janela = 300

posicao_x = (largura_tela - largura_janela) // 2
posicao_y = (altura_tela - altura_janela) // 2

root.geometry(f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}")

cronometro = Cronometro(root)
root.mainloop()