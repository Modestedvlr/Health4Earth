# 🌍 Health4Earth

![CI Status](https://github.com/JulienOllier/Health4Earth/actions/workflows/publish.yml/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

> **Analyse des liens entre les émissions de CO₂, la pollution atmosphérique et la santé publique à l’échelle mondiale.**

---

### ⚠️ Note Importante : Déploiement du Site Web

Le déploiement automatique (GitHub Pages) nécessitant des droits d'administration spécifiques sur ce dépôt, nous avons mis en place un **Fork de démonstration** pour valider le fonctionnement de notre pipeline CI/CD et du site web.

**Le site est pleinement fonctionnel et accessible ici :**
**[🔗 https://modestedvlr.github.io/Health4Earth/](https://modestedvlr.github.io/Health4Earth/)**

*(Ce lien démontre la génération automatique du rapport Quarto, de la documentation Sphinx et des cartes interactives).*

---

## Présentation

Ce projet a été réalisé dans le cadre du cours **HAX712X - Développement Logiciel** (Université de Montpellier). Il propose une suite d'outils Python pour télécharger, nettoyer et analyser des données environnementales et sanitaires, ainsi qu'un tableau de bord interactif.

## Fonctionnalités Clés

*   **Ingestion Automatique :** Téléchargement des données (OWID) avec gestion de cache système via `pooch` (reproductibilité garantie).
*   
*   **Analyses Statistiques :** Calculs de corrélations et tendances via une architecture Orientée Objet (`HealthAnalyzer`).
*   
*   **Visualisation Interactive :** Cartes dynamiques (`folium`) et graphiques interactifs (`plotly`) intégrés dans un rapport Web.
*   
*   **Qualité Logicielle :** Tests unitaires automatisés (`pytest`), Intégration Continue (GitHub Actions) et documentation technique (`Sphinx`).

---

## Installation

Pour tester ce projet sur votre machine locale :

1.  **Cloner le dépôt :**
    ```bash
    git clone https://github.com/JulienOllier/Health4Earth.git
    cd Health4Earth
    ```

2.  **Installer les dépendances :**
    ```bash
    # Installation en mode éditable avec les dépendances
    pip install -e .
    
    # (Optionnel) Installer les outils de développement (tests, doc)
    pip install -e .[dev]
    ```

3.  **Slides de presentation :**
   ```bash
   quarto preview slides/presentation.qmd
   ```
---

## Exemple d'utilisation

Voici un script rapide pour lancer une analyse via notre package :

```python
from health4earth.data_ingest import load_merged_data
from health4earth.analytics import HealthAnalyzer

# 1. Chargement des données (téléchargement auto avec Fallback si API indisponible)
print("Chargement des données...")
df = load_merged_data()

# 2. Initialisation de l'analyseur
analyzer = HealthAnalyzer(df)

# 3. Prédiction IA pour la France (Horizon 2030)
pred = analyzer.predict_evolution("France", "co2", year_end=2030)

# 4. Affichage des résultats
print(pred.tail())
```

---

## Développement & Tests

Le projet intègre une suite de tests automatisés pour garantir la stabilité.
```bash
   # Lancer les tests unitaires
python -m pytest tests/

# Générer la documentation technique (HTML)
cd docs
python -m sphinx.cmd.build -b html source build/html
```

---

## Auteurs :

Projet réalisé par les étudiants du Master SSD :

Dossou AGOSSOU
Firdaousse KARIMOU
Julien OLLIER

---

## Licence
Projet sous licence MIT.
