import subprocess


def Do_github_commit():
    commands = [
        ["git", "add", "."],
        ["git", "commit", "-m", "'primeiro commit automatico'"],
        ["git", "push"]
    ]
    
    for cmd in commands:
        
        resultado = subprocess.run(cmd, capture_output=True, text=True)
        print(resultado.stdout)

