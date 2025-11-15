---
Nom du projet: "Health4Earth"
author: "Équipe Health4Earth"
date: "25 octobre 2025"
format: html
editor: visual

---

# Health4Earth — Aperçu du projet
## Dépôt GitHub
- URL du dépôt : https://github.com/JulienOllier/Health4Earth

---

## Composition du groupe
| Prénom            | Nom             | 
|-------------------|-----------------|
| Dossou Modeste    | AGOSSOU         | 
| Firdaousse        | KARIMOU         | 
| Julien            | OLLIER          | 

---

## Objectif du projet
Le projet **Health4Earth** vise à analyser les liens entre les émissions de CO₂, la pollution atmosphérique et 
la santé publique à l’échelle mondiale. Il s’inscrit dans les thématiques de l’écologie et de la santé globale.

## Question centrale
Comment les **émissions de CO₂** et la **pollution atmosphérique** influencent-elles la santé publique, notamment les **maladies 
respiratoires**, la **mortalité** et l'**espérance de vie** des populations à travers le monde ?

---

## Architecture du projet minimum viable
### Arborescence du dépôt
Health4Earth/

├── data/

│ ├── raw/               # Données brutes téléchargées

│ ├── clean/             # Données nettoyées et préparées

│ └── metadata/          # Documentation des fichiers et codebook

├── docs/

│ ├── figures/           # Images et graphiques

│ ├── notes/             # Roadmap, diagrammes de Gantt, notes du projet

│ └── sketches/          # Croquis et idées pour le site

├── scripts/

│ ├── cleaning/          # Scripts de nettoyage et préparation des données

│ ├── eda/               # Analyse exploratoire

│ ├── models/            # Modélisation prédictive

│ └── utils/             # Fonctions utilitaires

├── website/

│ ├── assets/            # Images, CSS, JS

│ ├── index.qmd          # Page d'accueil

│ ├── data.qmd           # Présentation des données

│ ├── eda.qmd            # Analyse exploratoire

│ ├── model.qmd          # Résultats des modèles

│ ├── team.qmd           # Présentation de l'équipe

│ └── visualisations.qmd # Graphiques et cartes interactives

├── report/

│ └── annexes/           # Annexes pour le rapport final

├── LICENSE              # Licence MIT

└── README.md            # Ce fichier

---

## Visualisations principales
L’interface du site web proposera une **carte interactive** des capitales mondiales. En cliquant sur une capitale, l’utilisateur pourra visualiser :

- Une courbe des émissions de CO₂
- Une courbe de pollution atmosphérique (PM2.5)
- Une courbe de mortalité liée à la pollution
- Une courbe d’espérance de vie

### Exemples de visualisations
Voici les croquis et illustrations qui représentent ces objectifs :

![Carte interactive](docs/Carte_Interactive_Souhaitee.png)

### Pollution atmosphérique par capitale
![Pollution par capitale](docs/Air_Pollution_Per_Capital.jpg)

### Pollution mondiale
![Pollution mondiale](docs/Air-Pollution-Around-the-World.jpg)

### Décès liés à la pollution
![Décès liés à la pollution](docs/Die_Of_Air_pollution.jpg)

### Espérance de vie gagnée grâce à un air plus pur
![Espérance de vie](docs/Life_Expectancy_From_Cleaner_Air.jpg)


---

### Pipeline de développement
1. **Collecte des données** :
   - Our World in Data (OWID): émissions de CO₂, pollution atmosphérique
   - World Health Organization (WHO) : mortalité et espérance de vie liées à la pollution
   - Global Burden of Disease (GBD) : maladies respiratoires
   
2. **Nettoyage et fusion** :
   - Sélection des variables pertinentes
   - Harmonisation des formats et des unités

3. **Analyse exploratoire** :
   - Visualisations temporelles et géographiques
   - Corrélations pollution ↔ santé

4. **Modélisation** :
   - Régression linéaire pour prédire la mortalité
   - Validation croisée

5. **Site web Quarto** :
   - Pages interactives avec widgets
   - Déploiement via GitHub Pages

---

## Installation et exécution

1. **Cloner le dépôt** :
```bash
git clone https://github.com/JulienOllier/Health4Earth
cd Health4Earth
```
2. **Installer les dépendances** :
```bash
pip install -r requirements.txt
```

3. **Exécuter le pipeline** :

* Nettoyage des données
```bash
python scripts/cleaning/data_cleaning.py
```
* Analyse exploratoire et visualisations
```bash
quarto render website/eda.qmd
```
* Modélisation prédictive
```bash
python scripts/models/model.py
```
* Génération du site web interactif
```bash
quarto render website/index.qmd
```

---

## Prévisualisation du site Quarto localement
```bash
cd website
quarto preview
```
Le site s’ouvrira automatiquement dans votre navigateur à l’adresse : http://127.0.0.1:4200/

---

## Accès au site en ligne
Le site est déployé via GitHub Pages :
https://JulienOllier.github.io/Health4Earth/

---

## Technologies utilisées
- **Python** : pandas, scikit-learn, plotly, folium
- **Quarto** : pour le site web interactif
- **Git & GitHub** : gestion collaborative
- **Mermaid** : diagramme de Gantt
- **Markdown/LaTeX** : rédaction technique

---

## Branches Git :
main : branche principale

dev : branche de développement

data : nettoyage et préparation des données

model : modélisation prédictive

site : développement du site Quarto

---

## Contribution
Membre	                   Rôle
Firda               <--->   Nettoyage des données, fusion et préparation
Julien              <--->   Analyse exploratoire et visualisations interactives
Modeste	           <--->   Modélisation prédictive et validation
Tous les membres    <---> 	 Développement du site web, intégration Quarto, déploiement

---

## Licence
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

---

## Remarques
* Toutes les données utilisées sont publiquement disponibles et reproduisibles.
* Chaque script contient des docstrings et la documentation API sera générée via Sphinx.
* Des tests unitaires et un workflow d’intégration continue sont inclus pour garantir la fiabilité du projet.

---

```bash
git add README.md
git commit -m "Ajout du README final détaillé"
git push origin main
```