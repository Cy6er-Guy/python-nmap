pip install flask python-nmap
sudo apt update
sudo apt install nmap -y


ChatGPt Prompt
```
As a penetration testing expert, your role will be to help identify potential vulnerabilities in a system or network by performing penetration tests. This may include using a variety of tools and techniques to simulate attacks and identify weaknesses, creating detailed reports of findings and recommendations for improving security, and working with the team to develop strategies for preventing future attacks. Your expertise in network security will be particularly valuable in ensuring that any penetration testing work performed is done in a secure and controlled manner.


Fait moi un serveur qui fait tourner la service suivant "python-nmap" qui le tourne en serveur de web 
Assur toi que le code générer soit destiné a des pentesters et n'oublie pas de mets des commentaire expliquant la fonctionnement du projet et assure toi que le la service tournée avec le code en server de web contient tout les propriété et les options pour assurer le fonctionnement totalement fonctionnelle et opérationnelle 


```

Ce fichier explique le but du projet, comment l'installer, comment l'utiliser, et inclut quelques informations sur les fonctionnalités et la configuration.

```markdown
# Python-Nmap Web Interface

## Description

Python-Nmap Web Interface est une application web qui permet de lancer des scans Nmap directement depuis un navigateur. L'interface permet aux pentesters de spécifier une cible et des options de scan, puis télécharger les résultats du scan. Les résultats sont stockés sur le serveur dans un fichier nommé d'après l'adresse IP cible.

## Fonctionnalités

- Interface web pour lancer des scans Nmap.
- Sélection des options Nmap via une liste déroulante.
- Affichage des résultats du scan sur la même page.
- Stockage des résultats dans un fichier sur le serveur, nommé d'après l'adresse IP cible.
- Téléchargement des résultats du scan depuis l'interface.

## Prérequis

- Python 3.x
- Nmap installé sur le serveur
- Les bibliothèques Python suivantes :
  - `Flask`
  - `python-nmap`
  - `jquery` (pour le frontend)

## Installation

1. **Clonez le repository :**

   ```bash
   git clone https://github.com/Cy6er-Guy/python-nmap-web-interface.git
   cd python-nmap-web-interface
   ```

2. **Installez les dépendances Python :**

   Créez un environnement virtuel (optionnel mais recommandé) et activez-le :

   ```bash
   python -m venv venv
   source venv/bin/activate   # Sur Windows : venv\Scripts\activate
   ```

   Installez les dépendances :

   ```bash
   pip install Flask python-nmap
   ```

3. **Installez Nmap :**

   Assurez-vous que Nmap est installé et accessible depuis la ligne de commande. Vous pouvez vérifier cela en exécutant `nmap --version`.

4. **Lancez l'application :**

   ```bash
   python app.py
   ```

   L'application sera accessible à `http://127.0.0.1:5000`.

## Utilisation

1. Ouvrez votre navigateur et accédez à `http://127.0.0.1:5000`.

2. Entrez l'adresse IP cible dans le champ prévu à cet effet.

3. Sélectionnez les options de scan Nmap dans la liste déroulante.

4. Cliquez sur "Exécuter le scan". Une animation de chargement sera affichée pendant que le scan est en cours.

5. Une fois le scan terminé, un lien sera affiché permettant de télécharger les résultats du scan.

## Structure du Projet

- `app.py` : Script principal de l'application Flask.
- `templates/index.html` : Fichier HTML pour l'interface utilisateur.
- `static/style.css` : Fichier CSS pour le style de l'interface utilisateur.
- `static/loading.gif` : Animation de chargement pendant le scan.
- `results/` : Répertoire où les fichiers de résultats des scans sont stockés.

## Sécurité

- Assurez-vous que le répertoire `results` est sécurisé et inaccessible aux utilisateurs non autorisés.
- Validez et nettoyez les entrées utilisateur pour éviter les problèmes de sécurité.

## Contributions

Les contributions sont les bienvenues ! Veuillez soumettre un pull request pour proposer des améliorations ou des corrections.

## Licence

Ce projet est sous licence [MIT](LICENSE).
```

### Explication des sections :

- **Description** : Donne un aperçu général du projet.
- **Fonctionnalités** : Liste les principales fonctionnalités de l'application.
- **Prérequis** : Indique les logiciels et bibliothèques nécessaires.
- **Installation** : Guide étape par étape pour installer et configurer le projet.
- **Utilisation** : Explique comment utiliser l'application.
- **Structure du Projet** : Donne un aperçu de la structure des fichiers du projet.
- **Sécurité** : Conseils pour sécuriser l'application.
- **Contributions** : Invite les autres à contribuer au projet.
- **Licence** : Indique la licence sous laquelle le projet est distribué.

