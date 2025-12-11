Galerie d'Exemples
==================

Bienvenue dans la galerie d'utilisation. Vous trouverez ici des scénarios concrets pour exploiter le package **Health4Earth** dans vos propres scripts d'analyse ou Jupyter Notebooks.

.. contents:: Sommaire
   :local:
   :depth: 2

--------------------------------------------------------------------------------

Exemple 1 : Analyse Prédictive Simple
-------------------------------------

Ce script montre comment charger les données et prédire les émissions de CO2 de la France pour 2035.

.. code-block:: python
   :caption: script_prediction_france.py
   :linenos:

   from health4earth.data_ingest import load_merged_data
   from health4earth.analytics import HealthAnalyzer

   # 1. Chargement des données (avec mise en cache automatique)
   print("Chargement des données...")
   df = load_merged_data()

   # 2. Initialisation du moteur d'analyse
   analyzer = HealthAnalyzer(df)

   # 3. Prédiction à l'horizon 2035
   # Nous ciblons la colonne 'co2' pour la France
   forecast = analyzer.predict_evolution(
       country="France", 
       target_col="co2", 
       year_end=2035
   )

   if forecast is not None:
       # Affichage des 5 dernières années prédites
       print("Prédictions pour la France :")
       print(forecast[forecast['type'] == 'Prédiction'].tail())
   else:
       print("Données insuffisantes pour ce pays.")

--------------------------------------------------------------------------------

Exemple 2 : Comparaison Internationale
--------------------------------------

Comment comparer l'espérance de vie entre deux puissances économiques (Chine vs USA) ?

.. code-block:: python
   :caption: script_comparaison.py
   :linenos:

   import matplotlib.pyplot as plt
   import seaborn as sns
   from health4earth.data_ingest import load_merged_data

   # Chargement
   df = load_merged_data()

   # Filtrage sur les deux pays cibles depuis l'an 2000
   target_countries = ["China", "United States"]
   df_subset = df[
       (df['country'].isin(target_countries)) & 
       (df['year'] >= 2000)
   ]

   # Visualisation avec Seaborn
   plt.figure(figsize=(10, 6))
   sns.lineplot(
       data=df_subset, 
       x="year", 
       y="life_expectancy", 
       hue="country",
       style="country",
       markers=True,
       linewidth=2.5
   )

   plt.title("Comparaison de l'Espérance de Vie (2000-2024)")
   plt.ylabel("Années")
   plt.grid(True, alpha=0.3)
   plt.show()

--------------------------------------------------------------------------------

Exemple 3 : Analyse de la Pollution (Mortalité)
-----------------------------------------------

Ce script identifie les années où la mortalité liée à la pollution a été la plus critique pour un pays donné.

.. code-block:: python
   :caption: script_analyse_sante.py
   :linenos:

   from health4earth.data_ingest import load_merged_data
   from health4earth.analytics import HealthAnalyzer

   df = load_merged_data()
   analyzer = HealthAnalyzer(df)

   # Récupération des données brutes pour l'Inde
   df_india = analyzer.get_country_data("India")

   # Tri par nombre de décès décroissant
   top_worst_years = df_india.sort_values(
       by='pollution_deaths', 
       ascending=False
   ).head(5)

   print("Les 5 années les plus meurtrières en Inde (Pollution) :")
   for index, row in top_worst_years.iterrows():
       print(f"- {int(row['year'])} : {int(row['pollution_deaths'])} décès")

--------------------------------------------------------------------------------

Aller plus loin
---------------

Pour intégrer ces graphiques dans une page web interactive, consultez le code source de notre site web dans le dossier :

.. raw:: html

   <a href="https://github.com/modestedvlr/Health4Earth/tree/main/website" target="_blank" style="color: #2980b9; font-weight: bold;">
       website/ (Cliquez pour ouvrir GitHub) ↗
   </a>

du dépôt GitHub.