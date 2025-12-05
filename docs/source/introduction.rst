Introduction
============



Présentation du projet
----------------------



**Health4Earth** est une plateforme web développée dans le cadre d’un projet universitaire, dont l’objectif est d’analyser l’impact des émissions de CO₂ sur la santé humaine.

Notre travail se concentre sur l’étude de plusieurs indicateurs essentiels tels que l’espérance de vie, le taux de mortalité, ou encore certains facteurs démographiques, afin de mettre en évidence les conséquences mesurables de la pollution sur les populations.

À travers une interface cartographique et des visualisations interactives, la plateforme permet d’explorer les données au fil des années, de comparer plusieurs pays et de comprendre comment la hausse des émissions influence concrètement la santé publique.

Objectifs principaux
--------------------

Objectifs principaux
--------------------

- **Analyse historique et actuelle**  
  Étudier l’évolution des émissions de CO₂ et leurs effets mesurables sur la santé humaine à travers différents indicateurs (espérance de vie, taux de mortalité, population, etc.).
- **Prédiction des impacts sanitaires**  
  Fournir des estimations par pays et par année pour comprendre comment les variations des émissions influencent la santé publique.
- **Visualisation interactive**  
  Offrir des graphiques et cartes interactifs permettant de comparer pays et tendances dans le temps, pour une exploration intuitive des données.
- **Sensibilisation et communication**  
  Rendre accessibles les informations clés aux citoyens, chercheurs et décideurs afin de mettre en lumière les enjeux santé-environnement.


Technologies utilisées
----------------------

.. list-table::
   :widths: 25 75
   :header-rows: 1
   :stub-columns: 1

   * - Domaine
     - Technologies
   * - Backend & Analyse
     - Python 3.9+, Pandas, NumPy, Scikit-learn, Matplotlib
   * - Visualisation du site web
     - **Quarto**, le framework principal, Plotly
   * - Documentation
     - **Sphinx**, la documentation actuelle 
   * - Gestion de code
     - Git, GitHub, Visual Studio Code
   * - Déploiement
     - GitHub Pages, Netlify


Structure du projet
-------------------

.. code-block:: bash

   Health4Earth/
   │
   ├── quarto_site/          # Site web principal (Quarto)
   │   ├── _quarto.yml       # Configuration Quarto
   │   ├── index.qmd         # Page d'accueil
   │   ├── analysis.qmd      # Analyse globale
   │   └── predictions.qmd   # Prédictions France
   │
   ├── docs/                 # Documentation technique (Sphinx)
   │   ├── source/
   │   │   ├── conf.py
   │   │   ├── index.rst
   │   │   ├── introduction.rst    
   │   │   └── traitement_donnees.rst
   │   └── build/           # Documentation générée
   │
   ├── src/                  # Code source Python
   │   ├── data_processing/
   │   ├── models/
   │   └── utils/
   │
   ├── data/                 # Données
   │   ├── raw/              # Données brutes
   │   └── processed/        # Données nettoyées
   │
   └── README.md             # Description générale

Équipe projet
-------------

* **Étudiants en M1 SSD** - Université de Montpellier
* **Encadré par** : Bensaid Bilel
* **projet** : 2025 - 2026

.. note::
   Cette documentation est technique et s'adresse aux développeurs, contributeurs
   et utilisateurs avancés souhaitant comprendre le fonctionnement interne
   de Health4Earth.