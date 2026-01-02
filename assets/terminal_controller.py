import subprocess

def Local_repository():

    resultado = subprocess.run(
        ["ls", "-la"],
        capture_output=True,
        text=True
    )

    print(resultado.stdout)

Local_repository()