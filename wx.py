from termcolor import colored

text = """
 █     █░▓█████   ██████  ██▓    ▓█████▓██   ██▓    ▄████▄   ██▓     ██▓▓█████  ███▄    █ ▄▄▄█████▓
▓█░ █ ░█░▓█   ▀ ▒██    ▒ ▓██▒    ▓█   ▀ ▒██  ██▒   ▒██▀ ▀█  ▓██▒    ▓██▒▓█   ▀  ██ ▀█   █ ▓  ██▒ ▓▒
▒█░ █ ░█ ▒███   ░ ▓██▄   ▒██░    ▒███    ▒██ ██░   ▒▓█    ▄ ▒██░    ▒██▒▒███   ▓██  ▀█ ██▒▒ ▓██░ ▒░
░█░ █ ░█ ▒▓█  ▄   ▒   ██▒▒██░    ▒▓█  ▄  ░ ▐██▓░   ▒▓▓▄ ▄██▒▒██░    ░██░▒▓█  ▄ ▓██▒  ▐▌██▒░ ▓██▓ ░ 
░░██▒██▓ ░▒████▒▒██████▒▒░██████▒░▒████▒ ░ ██▒▓░   ▒ ▓███▀ ░░██████▒░██░░▒████▒▒██░   ▓██░  ▒██▒ ░ 
░ ▓░▒ ▒  ░░ ▒░ ░▒ ▒▓▒ ▒ ░░ ▒░▓  ░░░ ▒░ ░  ██▒▒▒    ░ ░▒ ▒  ░░ ▒░▓  ░░▓  ░░ ▒░ ░░ ▒░   ▒ ▒   ▒ ░░   
  ▒ ░ ░   ░ ░  ░░ ░▒  ░ ░░ ░ ▒  ░ ░ ░  ░▓██ ░▒░      ░  ▒   ░ ░ ▒  ░ ▒ ░ ░ ░  ░░ ░░   ░ ▒░    ░    
  ░   ░     ░   ░  ░  ░    ░ ░      ░   ▒ ▒ ░░     ░          ░ ░    ▒ ░   ░      ░   ░ ░   ░      
    ░       ░  ░      ░      ░  ░   ░  ░░ ░        ░ ░          ░  ░ ░     ░  ░         ░          
                                        ░ ░        ░                                               
"""

colored_text = colored(text, "blue")
print(colored_text)

user_input = input("Entrez une commande (help pour afficher les options) : ")

while user_input != "help":
    print("Commande invalide. Veuillez réessayer.")
    user_input = input("Entrez une commande (help pour afficher les options) : ")

print("\n- autoclick\n- velocity\n- w1sley toggle sprint\nkb négatif\n ")
user_input = input("Your choice: ")