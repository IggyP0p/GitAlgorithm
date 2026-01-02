import subprocess


def Do_github_commit(descricao:str, location:str):
    commands = [
        ["git", "add", "."],
        ["git", "commit", "-m", descricao],
        ["git", "push"]
    ]


    for cmd in commands:
        try:
            resultado = subprocess.run(cmd, capture_output=True, text=True, cwd=location)
        except Exception as e:
            print("Error: ", e)

        if resultado.returncode != 0:
            print("Error: " + resultado.stderr)

        else:
            print("Success: " + resultado.stdout)




def Do_gitlab_commit(descricao:str, location:str):
    commands = [
        ["git", "add", "."],
        ["git", "commit", "-m", descricao],
        ["git", "push", "gitlab"]
    ]

    for cmd in commands:

        resultado = subprocess.run(cmd, capture_output=True, text=True, cwd=location)
        print(resultado.stdout)


def Do_both_commits(descricao:str, location:str):
    commands = [
        ["git", "add", "."],
        ["git", "commit", "-m", descricao],
        ["git", "push"],
        ["git", "push", "gitlab"]
    ]

    for cmd in commands:

        resultado = subprocess.run(cmd, capture_output=True, text=True, cwd=location)
        
        if resultado.returncode != 0:
            print("Error: ")
            print(resultado.stderr)
        else:
            print("Success: ")
            print(resultado.stdout)


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
