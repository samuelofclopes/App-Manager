import subprocess # Para executar comandos no terminal.
import os # Apenas para limpar o terminal, já que subprocess não limpa corretamente em algumas IDEs.
import platform

system = platform.system()

# DICIONÁRIO DE APPS PARA CADA SISTEMA OPERACIONAL
if system == "Windows":
    Sys_installer = ["winget"]
    apps = {
    "VSCode":             "Microsoft.VisualStudioCode",
    "IntelliJ":           "JetBrains.IntelliJIDEA.Community",
    "WebStorm":           "JetBrains.WebStorm",          # removido espaço extra no final
    "PyCharm":            "JetBrains.PyCharm.Community",
    "Git":                "Git.Git",
    "GitHub Desktop":     "GitHub.GitHubDesktop",
    "GitLab":             "GLab.GLab",
    "Docker":             "Docker.DockerDesktop",
    "Postman":            "Postman.Postman",
    "Postman (ARM64)":    "Postman.Postman.arm64",
    "Insomnia":           "Insomnia.Insomnia",
    "DBeaver":            "dbeaver.dbeaver",
    "TablePlus":          "TablePlus.TablePlus",
    "Notion":             "Notion.Notion",
    "Todoist":            "Doist.Todoist",
    "Obsidian":           "Obsidian.Obsidian",
    "Slack":              "SlackTechnologies.Slack",
    "Discord":            "Discord.Discord",
    "Trello (MS Store)":  "9NBLGGH4XXVW",
    "Linear":             "LinearOrbit.Linear",
    "Figma":              "Figma.Figma",
    "Canva":              "Canva.Canva"
    }
elif system == "Linux":
    Sys_installer = ["sudo", "apt"]
    apps = {
    "Git":               "git",
    "GitHub Desktop":    "github-desktop",    # requer o repositório do shiftkey adicionado antes
    "VSCode":            "code",              # requer o repositório da Microsoft adicionado antes
    "Docker":            "docker.io",
    "HTOP":              "htop",
    "Vim":               "vim",
    "Neofetch":          "neofetch",
    "Curl":              "curl",
    "Wget":              "wget",
    "Tmux":              "tmux",
    "Tree":              "tree",
    "Net-Tools":         "net-tools",
    "Build Essential":   "build-essential",
    "UFW":               "ufw",
    "Zip":               "zip",
    "Unzip":             "unzip",
    "Tldr":              "tldr",
    "NCDU":              "ncdu",
    "Zsh":               "zsh",
    "JQ":                "jq",
    "Fzf":               "fzf",
    "Asciinema":         "asciinema",
    "Python3-PIP":       "python3-pip",
    "Node.js":           "nodejs",
    "NPM":               "npm",
    "Netcat":            "netcat-openbsd",
    "Shellcheck":        "shellcheck",
    "GDB":               "gdb",
    "Valgrind":          "valgrind",
    "Strace":            "strace",
    "Ag":                "silversearcher-ag",
    "Exuberant Ctags":   "exuberant-ctags",   # corrigido: "exctags" não existe no apt
    "Mosh":              "mosh",
    "VS Code (OSS)":     "code-oss",
    "Geany":             "geany",
    "Lazarus":           "lazarus",
    "Code::Blocks":      "codeblocks",
    "Emacs":             "emacs",
    "Kdenlive":          "kdenlive",
    "Shotcut":           "shotcut",
    "OpenShot":          "openshot-qt",
    "Pitivi":            "pitivi",
    "Blender":           "blender",
    "Inkscape":          "inkscape",
    "GIMP":              "gimp"
    }
elif system == "Darwin":
    Sys_installer = ["brew"]
    apps = {
    "VSCode":            "visual-studio-code",
    "WebStorm":          "webstorm",
    "PyCharm":           "pycharm-ce",         # corrigido: "pycharm" instala a versão paga
    "Git":               "git",
    "GitHub CLI":        "gh",
    "GitLab Runner":     "gitlab-runner",
    "Docker":            "docker",
    "Postman":           "postman",
    "Insomnia":          "insomnia",
    "DBeaver":           "dbeaver-community",
    "TablePlus":         "tableplus",
    "Notion":            "notion",
    "Todoist":           "todoist",
    "Obsidian":          "obsidian",
    "Slack":             "slack",
    "Discord":           "discord",
    "Trello":            "trello",
    "Linear":            "linear",
    "Figma":             "figma",
    "Canva":             "canva",
    "HTOP":              "htop",
    "Vim":               "vim",
    "Neofetch":          "neofetch",
    "Curl":              "curl",
    "Wget":              "wget",
    "Tmux":              "tmux",
    "Tree":              "tree",
    "Build Essential":   "gcc",
    "Zip":               "zip",
    "Unzip":             "unzip",
    "Tldr":              "tldr",
    "NCDU":              "ncdu",
    "Zsh":               "zsh",
    "JQ":                "jq",
    "Fzf":               "fzf",
    "Asciinema":         "asciinema",
    "Python3-PIP":       "python",
    "Node.js":           "node",
    "NPM":               "node",               # npm vem incluído com o node via brew
    "Netcat":            "netcat",
    "Shellcheck":        "shellcheck",
    "GDB":               "gdb",
    "Valgrind":          "valgrind",
    "Ag":                "the_silver_searcher",
    "Exuberant Ctags":   "ctags",
    "Mosh":              "mosh",
    "Geany":             "geany",
    "Lazarus":           "lazarus",
    "Code::Blocks":      "codeblocks",
    "Emacs":             "emacs",
    "Kdenlive":          "kdenlive",
    "Shotcut":           "shotcut",
    "OpenShot":          "openshot-video-editor",
    "Blender":           "blender",
    "Inkscape":          "inkscape",
    "GIMP":              "gimp"
    }

# AÇÕES PARA CADA SISTEMA OPERACIONAL
systemact = {
    "Windows": {
        "INSTALL":   ["install", "--silent"],
        "UPGRADE":   ["upgrade"],
        "UNINSTALL": ["uninstall"]
    },
    "Linux": {
        "INSTALL":   ["install", "-y"],
        "UPGRADE":   ["install", "--only-upgrade", "-y"],
        "UNINSTALL": ["remove", "-y"]
    },
    "Darwin": {
        "INSTALL":   ["install"],
        "UPGRADE":   ["upgrade"],
        "UNINSTALL": ["uninstall"]
    }
}


# Lista das apps em ordem alfabética
apps_abc = sorted(apps)

# Dicionário de apps em UPPER case para lidar com diferenças de escrita do utilizador
apps_upper = {app.upper(): apps[app] for app in sorted(apps)}


while True:
    # ==================================================================================================================================
    print("=" * 80)
    print("Welcome to app installer\nChoose from the apps listed below the ones you would like to install / upgrade / uninstall.\n")
    print("=" * 80)
    # ==================================================================================================================================


    # ==================================================================================================================================
    # PRINTA A TABELA
    col_width = len(max(apps_abc, key=len)) + 2 # largura de cada coluna baseada no nome mais longo
    for i, app in enumerate(apps_abc):
        print(f" | {app:{col_width}}", end="")
        if (i + 1) % 4 == 0: # quebra de linha a cada 4 apps
            print()
    print("\n\n" + "=" * 80)
    # ==================================================================================================================================


    # ==================================================================================================================================
    # EXECUTA O QUE É PEDIDO
    action = input("What do you want to do? [Install / Upgrade / Uninstall]: ").strip().upper() # Escolha do que será feito.
    while action not in ["INSTALL", "UPGRADE", "UNINSTALL"]: # Força o utilizador a escolher uma opção válida.
        action = input("Invalid option, try again [Install / Upgrade / Uninstall]: ").strip().upper()
    # =====================================

    choosed_app = input(f"\nChoose one app to {action.lower()}: ").strip().upper()
    while choosed_app not in apps_upper: # Força o utilizador a escolher uma app válida.
        choosed_app = input("\nInvalid app name, try again: ").strip().upper()
    # =====================================

    command = Sys_installer + systemact[system][action] + [apps_upper[choosed_app]] # Junta o instalador, a ação e o package da app escolhida.
    try:
        if system == "Linux":
            subprocess.run(["sudo", "apt", "update"], check=True) # Atualiza os repositórios antes de qualquer ação no Linux.
        subprocess.run(command, check=True) # Executa o comando no terminal.
    except subprocess.CalledProcessError:
        print("Something went wrong while running the command.")
    except FileNotFoundError:
        print(f"Installer '{Sys_installer[0]}' not found.")
    print("=" * 80)
    # ==================================================================================================================================


    # ==================================================================================================================================
    # CONTINUA OU PARA O CÓDIGO
    mais = input("Do you want to do something else? [Y/N]: ").strip().upper()

    while mais not in ["YES", "Y", "SIM", "S", "NO", "N", "NÃO", "NAO"]:
        mais = input("Invalid option, try again: ").strip().upper()
    if mais in ["YES", "Y", "SIM", "S"]:
        os.system("cls" if system == "Windows" else "clear") # Limpa o terminal.
        continue
    elif mais in ["NO", "N", "NÃO", "NAO"]:
        break
    # ==================================================================================================================================