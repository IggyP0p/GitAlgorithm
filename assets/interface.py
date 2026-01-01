import tkinter as tk

def clicou():
    label_resultado.config(text="git add upstream --'htpps//:www.github.com/joaozin/trabalho-colegio'")

def start():
    janela.mainloop()

janela = tk.Tk()

janela.title("GitAlgorithm")

janela.geometry("800x600")

botao = tk.Button(janela, text="Clique aqui", command=clicou)
botao.pack(side="top", pady=100, padx=300, fill="y")

label_resultado = tk.Label(
    janela, 
    text="", 
    bg="#333333", 
    fg="white",
    width=80,
    height=1)

label_resultado.pack()


# Configura Git (Apenas uma vez)
#
# git config --global user.name "Seu nome"
# git config --global user.email "Seu@email.com"
# git config --list -> confere
#
# URL Repositório: https://github.com/usuario/meu-projeto.git
#
# git init
# git remote add origin https://github.com/usuario/meu-projeto.git
# git commit -m "Mensagem"