import subprocess # Para executar comandos no terminal.
import os # Apenas para limpar o terminal, já que subprocess não limpa corretamente em algumas IDEs.
import platform

system = platform.system()

# DICIONÁRIO DE APPS PARA CADA SISTEMA OPERACIONAL
if system == "Windows":
    Sys_installer = ["winget"]
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
elif system == "Linux":
    Sys_installer = ["sudo", "apt"]
    apps = { 
    "Git": "git", 
    "Docker": "docker.io", 
    "HTOP": "htop",
    "Vim": "vim",
    "Neofetch": "neofetch",
    "Curl": "curl",
    "Wget": "wget",
    "Tmux": "tmux",
    "Tree": "tree",
    "Net-Tools": "net-tools",
    "Build Essential": "build-essential",
    "UFW": "ufw",
    "Zip": "zip",
    "Unzip": "unzip",
    "Tldr": "tldr",
    "NCDU": "ncdu",
    "Zsh": "zsh",
    "JQ": "jq",
    "Fzf": "fzf",
    "Asciinema": "asciinema",
    "Python3-PIP": "python3-pip",
    "Node.js": "nodejs",
    "NPM": "npm",
    "Netcat": "netcat-openbsd",
    "Shellcheck": "shellcheck",
    "GDB": "gdb",
    "Valgrind": "valgrind",
    "Strace": "strace",
    "Ag": "silversearcher-ag",
    "Exuberant Ctags": "exctags",
    "Mosh": "mosh",
    "VS Code (OSS)": "code-oss",
    "Geany": "geany",
    "Lazarus": "lazarus",
    "Code::Blocks": "codeblocks",
    "Emacs": "emacs",
    "Kdenlive": "kdenlive",
    "Shotcut": "shotcut",
    "OpenShot": "openshot-qt",
    "Pitivi": "pitivi",
    "Blender": "blender",
    "Inkscape": "inkscape",
    "GIMP": "gimp"
    }
elif system == "Darwin":
    Sys_installer = ["brew"]
    apps = {
    "WebStorm": "webstorm",
    "PyCharm": "pycharm",
    "Git": "git",
    "GitHub CLI": "gh",
    "GitLab Runner": "gitlab-runner",
    "Docker": "docker",
    "Postman": "postman",
    "Insomnia": "insomnia",
    "DBeaver": "dbeaver-community",
    "TablePlus": "tableplus",
    "Notion": "notion",
    "Todoist": "todoist",
    "Obsidian": "obsidian",
    "Slack": "slack",
    "Discord": "discord",
    "Trello": "trello",
    "Linear": "linear",
    "Figma": "figma",
    "Canva": "canva",
    "HTOP": "htop",
    "Vim": "vim",
    "Neofetch": "neofetch",
    "Curl": "curl",
    "Wget": "wget",
    "Tmux": "tmux",
    "Tree": "tree",
    "Build Essential": "gcc",
    "Zip": "zip",
    "Unzip": "unzip",
    "Tldr": "tldr",
    "NCDU": "ncdu",
    "Zsh": "zsh",
    "JQ": "jq",
    "Fzf": "fzf",
    "Asciinema": "asciinema",
    "Python3-PIP": "python",
    "Node.js": "node",
    "NPM": "node",
    "Netcat": "netcat",
    "Shellcheck": "shellcheck",
    "GDB": "gdb",
    "Valgrind": "valgrind",
    "Ag": "the_silver_searcher",
    "Exuberant Ctags": "ctags",
    "Mosh": "mosh",
    "VS Code": "visual-studio-code",
    "Geany": "geany",
    "Lazarus": "lazarus",
    "Code::Blocks": "codeblocks",
    "Emacs": "emacs",
    "Kdenlive": "kdenlive",
    "Shotcut": "shotcut",
    "OpenShot": "openshot-video-editor",
    "Blender": "blender",
    "Inkscape": "inkscape",
    "GIMP": "gimp"
    }

# ACÕES PARA CADA SISTEMA OPERACIONAL
systemact = {
    "Windows": {
        "INSTALL": ["install"],
        "UPGRADE": ["upgrade"],
        "UNINSTALL": ["uninstall"]
    },
    "Linux": {
        "INSTALL": ["install"],
        "UPGRADE": ["install", "--only-upgrade"],
        "UNINSTALL": ["remove"]
    },
    "Darwin": {
        "INSTALL": ["install"],
        "UPGRADE": ["upgrade"],
        "UNINSTALL": ["uninstall"]
    }
}


# Lista das apps em ordem alfabética
apps_abc = sorted(apps)

# Dicionário de apps em UPPER case para cuidado de escrita
apps_upper = {app.upper(): apps[app] for app in sorted(apps)}




# Execussão do código no terminal
def escolha(esc):
    try:
        subprocess.run(esc, capture_output=False, text=True)
    except KeyError:
        print("No app found.")
            

while True:
    # ==================================================================================================================================
    print("=" * 80)
    print("Welcome to app installer\nChoose from the apps listed below the ones you would like to install / upgrade / uninstall.\n")
    print("=" * 80) 
    # ==================================================================================================================================


    # ==================================================================================================================================
    # PRINTA A TABELA
    for i in range(0, len(apps_abc) - 3, 1):
        if i & 3 == 0:
            print("\n")
        print(" | " + apps_abc[i] + (" " * (len(max(apps_abc, key=len)) - len(apps_abc[i]))), end="")
        
    print("\n\n\n" + "=" * 80)
    # ==================================================================================================================================


    # ==================================================================================================================================
    # EXECUTA O QUE É PEDIDO
    action = input("What you want to do? [Install / Upgrade / Uninstall]").strip().upper() # Escolha do que será feito.
    while action not in ["INSTALL", "UPGRADE", "UNINSTALL"]: # Força o usuário a escolher uma opção válida.
        action = input("Invalid option, try again [Install / Upgrade / Uninstall]").strip().upper()
    # =====================================
    
    choosed_app = input(f"\nChoose one app to {action.lower()}: ").strip().upper()
    while choosed_app not in apps_upper:
        choosed_app = input("\nInvalid app name, try again: ").strip().upper()
    # =====================================
    command = Sys_installer + systemact[system][action] + [apps_upper[choosed_app]] # Junta as listas do installador, da ação e do codigo da aplicação escolhida.
    try:
        subprocess.run(command, capture_output=False, text=True) # Executa o comando no terminal.
    except KeyError: # Se falhar, printa que a app não foi encontrada.
        print("No app as been found.")
    print("=" * 80)
    # ==================================================================================================================================


    # ==================================================================================================================================
    # CONTINUA OU PARA O CODIGO
    mais = input("Do you want to do something else? [Y/N]: ").upper()

    while mais not in ["YES", "Y", "SIM", "S", "NO", "N", "NÃO", "NAO"]:
            mais = input("\n\nInvalid option, try again: ").strip().upper()
    if mais in ["YES", "Y", "SIM", "S"]:
        os.system("cls" if system == "Windows" else "clear") # Limpa o terminal
        continue
    elif mais in ["NO", "N", "NÃO", "NAO"]:
        break
    # ==================================================================================================================================