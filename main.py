import subprocess

chemin_programme = 'C:/Users/Dylserker/Desktop/BotDokkan/dokkan/Dokkan-FarmBot'

try:
    subprocess.run(chemin_programme, check=True)
    print(f"{chemin_programme} a été lancé avec succès.")
except subprocess.CalledProcessError as e:
    print(f"Erreur lors de l'exécution de {chemin_programme}: {e}")
except FileNotFoundError:
    print(f"Le fichier {chemin_programme} n'a pas été trouvé.")
except Exception as e:
    print(f"Une erreur est survenue: {e}")