# Health4Earth

![CI Status](https://github.com/JulienOllier/Health4Earth/actions/workflows/publish.yml/badge.svg)

> **Analyse des liens entre les émissions de CO₂, la pollution atmosphérique et la santé publique à l’échelle mondiale.**

Ce projet a été réalisé dans le cadre du cours **HAX712X - Développement Logiciel** (Université de Montpellier). Il propose une suite d'outils Python pour télécharger, nettoyer et analyser des données environnementales et sanitaires, ainsi qu'un tableau de bord interactif.

🔗 **[Accéder au Site Web du Projet (Dashboard)](https://[PSEUDO_DU_PROPRIETAIRE].github.io/[NOM_DU_DEPO]/)**

---

## Fonctionnalités Clés

*   **Ingestion Automatique :** Téléchargement des données (OWID) avec gestion de cache système via `pooch` (reproductibilité garantie).
*   **Analyses Statistiques :** Calculs de corrélations et tendances via une architecture Orientée Objet (`HealthAnalyzer`).
*   **Visualisation Interactive :** Cartes dynamiques (`folium`) et graphiques intégrés dans un rapport Web (`Quarto`).
*   **Qualité Logicielle :** Tests unitaires automatisés (`pytest`), Intégration Continue (GitHub Actions) et documentation technique (`Sphinx`).

---

## Installation

Pour tester ce projet sur votre machine locale :

1.  **Cloner le dépôt :**
    ```bash
    git clone https://github.com/[PSEUDO_DU_PROPRIETAIRE]/[NOM_DU_DEPO].git
    cd [NOM_DU_DEPO]
    ```

2.  **Installer les dépendances :**
    ```bash
    # Installation en mode éditable avec les dépendances
    pip install -e .
    
    # (Optionnel) Installer les outils de développement (tests, doc)
    pip install -e .[dev]
    ```

---

## Exemple d'utilisation

Voici un script rapide pour lancer une analyse :

```python
from health4earth.data_ingest import load_co2_data
from health4earth.analytics import HealthAnalyzer

# 1. Chargement des données (téléchargement auto si premier lancement)
print("Chargement des données...")
df = load_co2_data()

# 2. Initialisation de l'analyseur
analyzer = HealthAnalyzer(df)

# 3. Filtrage des années à forte émission (> 50 MT)
polluted_years = analyzer.get_polluted_years(threshold=50.0)
print(f"Nombre d'années concernées : {len(polluted_years)}")

# 4. Affichage des premières lignes
print(polluted_years[['country', 'year', 'co2']].head())
```

---

## Roadmap du Projet
Le développement a suivi les étapes suivantes :
gantt
    title Planning de Développement Health4Earth
    dateFormat  YYYY-MM-DD
    axisFormat  %d/%m
    
    section Conception
    Choix du sujet          :done,    des1, 2025-10-01, 7d
    Architecture & Git      :done,    des2, after des1, 5d
    
    section Développement
    Ingestion (Pooch)       :done,    dev1, 2025-10-15, 10d
    Nettoyage & Classes     :done,    dev2, after dev1, 10d
    Tests & CI/CD           :active,  dev3, 2025-11-01, 25d
    
    section Rendu Final
    Site Web (Quarto)       :active,  web1, 2025-11-20, 10d
    Documentation & Slides  :         doc1, after web1, 5d

---

## Développement & Tests
Le projet intègre une suite de tests automatisés.
```Bash
# Lancer les tests unitaires
python -m pytest tests/

# Générer la documentation technique (HTML)
cd docs
python -m sphinx.cmd.build -b html source build/html
```

## Auteurs
[Dossou Modeste AGOSSOU]
[Firdaousse KARIMOU]
[Juien OLLIER]


## Licence
Projet sous licence MIT.
