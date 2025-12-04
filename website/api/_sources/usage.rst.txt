Guide d'Utilisation
===================

Ce guide explique comment utiliser les fonctionnalités principales du package.

Chargement des Données
----------------------

Le module ``data_ingest`` gère le téléchargement automatique (via Pooch) et la fusion des sources.

.. code-block:: python

   from health4earth.data_ingest import load_merged_data

   # Charge le dataset complet (CO2 + Pollution + Santé)
   df = load_merged_data()
   print(df.head())

Analyse et Prédictions
----------------------

La classe ``HealthAnalyzer`` permet de projeter les tendances futures.

.. code-block:: python

   from health4earth.analytics import HealthAnalyzer

   # Initialisation
   analyzer = HealthAnalyzer(df)

   # Prédiction pour la France (Horizon 2030)
   pred = analyzer.predict_evolution(country="France", target_col="co2", year_horizon=2030)
   
   print(pred.tail())