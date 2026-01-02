import tkinter as tk
from tkinter import filedialog
from . import terminal_controller as tc



def Local_repository_location():
    global location
    
    location = filedialog.askdirectory(
        title="Choose a directory"
    )

    local_repository_path.config(text=location)


#-- Screen configs

screen = tk.Tk()
screen.title("GitAlgorithm")
screen.geometry("800x600")


#-- Local Repository configs

local_repository_frame = tk.Frame(screen)
local_repository_frame.pack(fill="x", padx=20, pady=20)

local_repository_btn = tk.Button(local_repository_frame, text="add local repository", command=Local_repository_location)
local_repository_btn.pack(side="left", fill="x", padx=20)

local_repository_path = tk.Label(
    local_repository_frame, 
    text="", 
    bg="#333333", 
    fg="white",
    width=40,
    height=1)

local_repository_path.pack(side="left", fill="x", expand=True)


#-- Github commit config

github_frame = tk.Frame(screen)
github_frame.pack(fill="y", padx=10, pady=10)

github_btn = tk.Button(github_frame, text="github commit", command=tc.Do_github_commit)
github_btn.pack(side="top", fill="x", padx=10)


# Configura Git (Apenas uma vez)
#
# git config --global user.name "Seu nome"
# git config --global user.email "Seu@email.com"
# git config --list -> confere
#
# URL Repositório: https://github.com/usuario/meu-projeto.git
#
# git init
# git remote add github https://github.com/usuario/meu-projeto.git
# git remote add gitlab git@gitlab.com:usuario/meu-projeto.git 
# git commit -m "Mensagem"