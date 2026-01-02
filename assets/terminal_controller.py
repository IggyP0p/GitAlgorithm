import subprocess


def Do_github_commit(descricao:str):
    commands = [
        ["git", "add", "."],
        ["git", "commit", "-m", descricao],
        ["git", "push"]
    ]


    for cmd in commands:

        resultado = subprocess.run(cmd, capture_output=True, text=True)
        
        if resultado.returncode != 0:
            print("Error: " + resultado.stderr)

        else:
            print("Success: " + resultado.stdout)




def Do_gitlab_commit(descricao:str):
    commands = [
        ["git", "add", "."],
        ["git", "commit", "-m", descricao],
        ["git", "push", "gitlab"]
    ]

    for cmd in commands:

        resultado = subprocess.run(cmd, capture_output=True, text=True)
        print(resultado.stdout)


def Do_both_commits(descricao:str):
    commands = [
        ["git", "add", "."],
        ["git", "commit", "-m", descricao],
        ["git", "push"],
        ["git", "push", "gitlab"]
    ]

    for cmd in commands:

        resultado = subprocess.run(cmd, capture_output=True, text=True)
        
        if resultado.returncode != 0:
            print("Error: ")
            print(resultado.stderr)
        else:
            print("Success: ")
            print(resultado.stdout)