import subprocess # Para executar comandos no terminal.
import os # Apenas para limpar o terminal, já que subprocess não limpa corretamente em algumas IDEs.
 

# Dicionário de apps para futuras atualizações
apps = {
    "VSCode": "Microsoft.VisualStudioCode", 
    "IntelliJ": "JetBrains.IntelliJIDEA.Community", 
    "WebStorm": "JetBrains.WebStorm ", 
    "PyCharm": "JetBrains.PyCharm", 
    "Git": "Git.Git", 
    "GitHub": "GitHub.GitHubDesktop", 
    "GitLab": "GLab.GLab", 
    "Docker": "Docker.DockerDesktop", 
    "Postman": "Postman.Postman", 
    "Postman (ARM64)": "Postman.Postman.arm64",
    "Insomnia": "Insomnia.Insomnia", 
    "DBeaver": "DBeaver.DBeaver.Community", 
    "TablePlus": "TablePlus.TablePlus",
    "Notion": "Notion.Notion", 
    "Todoist": "Doist.Todoist", 
    "Obsidian": "Obsidian.Obsidian", 
    "Slack": "SlackTechnologies.Slack", 
    "Discord": "Discord.Discord", 
    "Trello (MS Store)": "9NBLGGH4XXVW", 
    "Linear": "LinearOrbit.Linear",  
    "Figma": "Figma.Figma", 
    "Canva": "Canva.Canva"
}

# Lista das apps em ordem alfabética
apps_abc = sorted(apps)

# Dicionário de apps em UPPER case para cuidado de escrita
apps_upper = {app.upper(): apps[app] for app in sorted(apps)}




# Execussão do código no terminal
def escolha(type, esc):
    try:
        resultado = subprocess.run(["winget", type, apps_upper[esc]], capture_output=True, text=True) # Captura o output e transforma de bytes para texto
        print(resultado.stdout.splitlines()[-1]) # Printa o resultado
    except KeyError:
        print("No app found.")
            

while True:
    print("========================================================================================================================================")
    print("Welcome to app installer\n" \
          "Choose from the apps listed below the ones you would like to install / update / uninstall.\n")
    print("========================================================================================================================================")
    for i in range(0, len(apps_abc) - 3, 1):
        if i & 3 == 0:
            print("\n")
        print(" | " + apps_abc[i] + (" " * (len(max(apps_abc, key=len)) - len(apps_abc[i]))), end="")
        
    print("\n\n\n========================================================================================================================================")
    action = input("What you want to do? [Install / Update / Uninstall]").strip().upper()
    while action not in ["INSTALL", "UPDATE", "UNINSTALL"]:
        action = input("Invalid option, try again [Install / Update / Uninstall]").strip().upper()
    escolha(action, input("\nEnter the name: ").strip().upper())
    print("========================================================================================================================================")
    mais = input("Do you want to do something else? [Y/N]: ").upper()

    while mais not in ["YES", "Y", "SIM", "S", "NO", "N", "NÃO", "NAO"]:
            mais = input("\n\nInvalid option, try again: ").strip().upper()
    if mais in ["YES", "Y", "SIM", "S"]:
        os.system('cls')
        continue
    elif mais in ["NO", "N", "NÃO", "NAO"]:
        break
        