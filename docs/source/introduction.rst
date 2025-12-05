Introduction
============



Présentation du projet
----------------------

**Health4Earth** est une plateforme web développée dans le cadre d'un projet scolaire, visant à analyser et prédire l'impact des facteurs environnementaux sur la santé publique en France.

Notre objectif est de fournir aux citoyens, chercheurs et décideurs des outils de visualisation et d'analyse accessibles pour comprendre les corrélations entre environnement et santé.

Objectifs principaux
--------------------

1. **Analyse en temps réel** des données environnementales
2. **Prédiction** des risques sanitaires par région
3. **Visualisation interactive** via des cartes et graphiques
4. **Sensibilisation** du public aux enjeux santé-environnement

Technologies utilisées
----------------------

.. list-table::
   :widths: 30 70
   :header-rows: 1
   
   * - Domaine
     - Technologies
   * - Backend & Analyse
     - Python 3.9+, Pandas, NumPy, Scikit-learn, Matplotlib
   * - Visualisation web
     - **Quarto** (framework principal), Plotly, D3.js
   * - Documentation
     - **Sphinx** (cette documentation), reStructuredText
   * - Gestion de code
     - Git, GitHub, Visual Studio Code
   * - Déploiement
     - GitHub Pages / Netlify

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
   │   │   ├── introduction.rst      # (ce fichier)
   │   │   └── traitement_donnees.rst
   │   └── _build/           # Documentation générée
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

* **Étudiants en [ta formation]** - [Nom de ton école/université]
* **Encadré par** : [Nom du professeur]
* **Période** : [Date de début] - [Date de fin]

.. note::
   Cette documentation est technique et s'adresse aux développeurs, contributeurs
   et utilisateurs avancés souhaitant comprendre le fonctionnement interne
   de Health4Earth.