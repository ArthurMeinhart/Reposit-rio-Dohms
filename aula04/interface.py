import tkinter as tk


def inserir_texto(x):
    texto.insert(1.0,x)

janela=tk.Tk()

janela.geometry("400x400")

texto=tk.Text(janela,height=4, width=24,font=("Arial",24))
texto.grid(columnspan=4)

botao1=tk.Button(janela, text="1",command=lambda:inserir_texto("1"),width=13, height=4,font=("Arial",12))
botao1.grid(column=1,row=2)

botao2=tk.Button(janela, text="2",command=lambda:inserir_texto("2"),width=13, height=4,font=("Arial",12))
botao2.grid(column=2,row=2)


janela.mainloop()