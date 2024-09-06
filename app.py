from flask import Flask, render_template, request, send_from_directory
import nmap
import os

# Création de l'application Flask
app = Flask(__name__)

# Instanciation de l'objet scanner nmap
nm = nmap.PortScanner()

# Répertoire où les résultats seront sauvegardés
RESULTS_DIR = 'results'
os.makedirs(RESULTS_DIR, exist_ok=True)

# Route principale pour afficher l'interface graphique
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Route pour exécuter le scan Nmap
@app.route('/scan', methods=['POST'])
def scan():
    target = request.form['target']
    arguments = request.form['arguments']
    
    # Nom de fichier basé sur l'adresse IP cible
    filename = f"{target.replace('.', '_')}.txt"
    filepath = os.path.join(RESULTS_DIR, filename)
    
    try:
        # Exécution du scan Nmap
        nm.scan(target, arguments=arguments)
        
        # Génération des résultats en format texte
        results = nm.csv()
        
        # Écriture des résultats dans un fichier
        with open(filepath, 'w') as file:
            file.write(results)
        
        # Retourner le chemin du fichier pour téléchargement
        return f"<p>Scan terminé. <a href='/results/{filename}'>Télécharger les résultats</a></p>"
    except Exception as e:
        return f"<p>Erreur lors du scan : {str(e)}</p>"

# Route pour servir les fichiers de résultats
@app.route('/results/<filename>')
def download_file(filename):
    return send_from_directory(RESULTS_DIR, filename)

# Fonction principale pour démarrer le serveur
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
