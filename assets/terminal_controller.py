import subprocess
from . import interface


def Do_github_commit(descricao:str, location:str):
    commands = [
        ["git", "add", "."],
        ["git", "commit", "-m", descricao],
        ["git", "push", "origin"]
    ]


    for cmd in commands:

        resultado = subprocess.run(cmd, capture_output=True, text=True, cwd=location)

        if resultado.returncode != 0:
            print("Error: " + resultado.stderr)
            interface.show_label(interface.github_bad_message)

        else:
            print("Success: " + resultado.stdout)
            
            interface.show_label(interface.commit_good_message)
            interface.Label_commands(3)




def Do_gitlab_commit(descricao:str, location:str):
    commands = [
        ["git", "add", "."],
        ["git", "commit", "-m", descricao],
        ["git", "push", "gitlab"]
    ]

    for cmd in commands:

        resultado = subprocess.run(cmd, capture_output=True, text=True, cwd=location)
        
        if resultado.returncode != 0:
            print("Error: " + resultado.stderr)
            interface.show_label(interface.gitlab_bad_message)

        else:
            print("Success: " + resultado.stdout)
            interface.show_label(interface.commit_good_message)
            interface.Label_commands(4)


def Do_both_commits(descricao:str, location:str):
    commands = [
        ["git", "add", "."],
        ["git", "commit", "-m", descricao],
        ["git", "push", "origin"],
        ["git", "push", "gitlab"]
    ]

    for i, cmd in enumerate(commands):

        resultado = subprocess.run(cmd, capture_output=True, text=True, cwd=location)
        
        if resultado.returncode != 0:
            print("Error: " + resultado.stderr)

            if i == 2:
                interface.show_label(interface.github_bad_message)
                break
        
            elif i == 3:
                interface.show_label(interface.gitlab_bad_message)

        else:
            print("Success: " + resultado.stdout)
            interface.show_label(interface.commit_good_message)
            interface.Label_commands(5)


def detect_git_repository(location:str):

    resultado = subprocess.run(["git", "rev-parse", "--is-inside-work-tree"], capture_output=True, text=True, cwd=location)

    if resultado.returncode != 0:
        print("Error: ")
        print(resultado.stderr)
        return False
    else:
        print("Success: ")
        print(resultado.stdout)
        return True
