import tkinter as tk
from tkinter import filedialog
from . import terminal_controller as tc

location:str = ""
commit_text:str = ""
previous_label:tk.Label = None

def Local_repository_location():
    
    global location

    location = filedialog.askdirectory(
        title="Choose a directory"
    )

    answer = tc.detect_git_repository(location)

    if answer:
        local_repository_path.config(text=location)
        show_label(local_repository_good_message)
        Label_commands(1)
    else:
        show_label(local_repository_bad_message)


def Get_description():

    global commit_text

    commit_text = commit_description.get()

    if commit_text == "":
        show_label(entry_bad_message)
        return
    else:
        show_label(entry_good_message)
        Label_commands(2)
        commit_text = "'" + commit_text + "'"


def show_label(label:tk.Label):

    global previous_label

    if previous_label != None:
        previous_label.forget()

    previous_label = label

    label.pack(fill="x")


def Label_commands(command:int):

    match command:
        case 1:
            command_label.config(text="cd " + location)

        case 2:
            command_label.config(text="git commit -m '" + commit_text + "'")

        case 3:
            command_label.config(text="git push origin")

        case 4:
            command_label.config(text="git push gitlab")

        case 5:
            command_label.config(text="git push")



#-- Screen configs

screen = tk.Tk()
screen.title("GitAlgorithm")
screen.geometry("600x400")



#-- Local Repository configs

local_repository_frame = tk.Frame(screen)
local_repository_frame.pack(fill="x", padx=20, pady=20)

local_repository_btn = tk.Button(local_repository_frame, text="add local repository", command=Local_repository_location)
local_repository_btn.pack(side="left", fill="x", padx=20)

local_repository_path = tk.Label(local_repository_frame, text="", bg="#333333", fg="white", width=40, height=1)

local_repository_path.pack(side="left", fill="x", expand=True)

local_repository_good_message = tk.Label(screen, text="Succesfully conected to a git repository", fg="green")

local_repository_bad_message = tk.Label(screen, text="This is not a git repository", fg="red")



#-- Entrada de dados

commit_description = tk.StringVar()

entry_frame = tk.Frame(screen)
entry_frame.pack(fill="x", padx=4, pady=4)

entry_label = tk.Label(entry_frame, text="Insert the description:", width=20, height=1)
entry_label.pack(side="left", padx=25)

entry = tk.Entry(entry_frame, textvariable=commit_description, justify="center")
entry.pack(side="left", fill="x", expand=True)

description_btn = tk.Button(entry_frame, text="confirm", command=Get_description)
description_btn.pack(fill="x", padx=15)

entry_good_message = tk.Label(screen, text="commit description confirmed", fg="green")

entry_bad_message = tk.Label(screen, text="commit description cannot be empty", fg="red")



#-- Git commands

command_frame = tk.Frame(screen)
command_frame.pack(fill="x", padx=15, pady=15)

command_label = tk.Label(command_frame, text="Do something", width=40, height=3, bg="#333333", fg="white")
command_label.pack(fill="x")



#-- Buttons Frame

commit_buttons_frame = tk.Frame(screen, bg="#333333", borderwidth=2, relief="solid")
commit_buttons_frame.pack(fill="x", padx=10, pady=10)


#-- Github commit config

github_btn = tk.Button(commit_buttons_frame, text="github commit", command=lambda: tc.Do_github_commit(commit_text, location))
github_btn.pack(side="top", fill="x", padx=10, pady=5)

github_bad_message = tk.Label(screen, text="Error: It was not possible to commit on github", fg="red")

commit_good_message = tk.Label(screen, text="Success: Git commited", fg="green")


#-- Gitlab commit config

gitlab_btn = tk.Button(commit_buttons_frame, text="gitlab commit", command=lambda: tc.Do_gitlab_commit(commit_text, location))
gitlab_btn.pack(side="top", fill="x", padx=10, pady=5)

gitlab_bad_message = tk.Label(screen, text="Error: It was not possible to commit on gitlab", fg="red")


#-- Both commit config

both_btn = tk.Button(commit_buttons_frame, text="both commit", command=lambda: tc.Do_gitlab_commit(commit_text, location))
both_btn.pack(side="top", fill="x", padx=10, pady=5)


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