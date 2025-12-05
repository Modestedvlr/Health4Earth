Traitement des données
======================

Cette section décrit le pipeline complet de traitement des données, de la collecte à l'analyse.

Sources de données
------------------

.. list-table:: Sources principales
   :widths: 25 50 25
   :header-rows: 1
   
   * - Source
     - Description
     - Fréquence
   * - **Santé Publique France**
     - Données sanitaires (hospitalisations, maladies)
     - Quotidienne
   * - **Météo-France**
     - Données météorologiques (température, qualité air)
     - Horaires
   * - **data.gouv.fr**
     - Données environnementales (pollution, occupation sol)
     - Mensuelle
   * - **INSEE**
     - Données démographiques par région
     - Annuelle
   * - **OurworldInData**


Nettoyage des données
---------------------

Étapes principales de prétraitement :

1. **Suppression des valeurs aberrantes**
   
   .. code-block:: python
      
      def remove_outliers(df, column):
          Q1 = df[column].quantile(0.25)
          Q3 = df[column].quantile(0.75)
          IQR = Q3 - Q1
          return df[(df[column] >= Q1 - 1.5*IQR) & 
                    (df[column] <= Q3 + 1.5*IQR)]

2. **Gestion des valeurs manquantes**
   
   - Interpolation pour séries temporelles
   - Moyenne par région pour données spatiales
   - Suppression si >30% manquants



Structure des données traitées
------------------------------

.. code-block:: python

   # Exemple de DataFrame final
   import pandas as pd
   
   data_structure = {
       'date': 'datetime64[ns]',        # Date de l'observation
       'region': 'str',                 # Code région INSEE
       'temperature': 'float64',        # °C moyen
       'air_quality': 'float64',        # Indice ATMO
       'hospitalizations': 'int64',     # Nombre d'hospitalisations
       'population': 'int64',           # Population de la région
       'risk_level': 'category'         # Niveau de risque calculé
   }

Indicateurs calculés
--------------------

.. glossary::

   IRSE
      Indice Régional Santé-Environnement : combine pollution et hospitalisations.
   
   TCR
      Taux de Corrélation Régionale : mesure lien température/santé.
   
   PDI
      Prévision des Dangers Imminents : alerte précoce basée sur ML.

Validation des données
----------------------

.. warning::
   Avant toute analyse, nous vérifions :
   
   1. Cohérence temporelle (pas de trous dans les dates)
   2. Cohérence spatiale (toutes régions présentes)
   3. Plages de valeurs réalistes
   4. Corrélations attendues vérifiées

Exemple complet de pipeline
---------------------------

.. code-block:: python
   :linenos:
   
   # health4earth/src/data_processing/pipeline.py
   
   import pandas as pd
   from sklearn.preprocessing import StandardScaler
   
   class DataPipeline:
       """Pipeline complet de traitement des données Health4Earth"""
       
       def __init__(self, raw_data_path):
           self.raw_data = pd.read_csv(raw_data_path)
           self.processed_data = None
           
       def run(self):
           """Exécute toutes les étapes du pipeline"""
           self.clean()
           self.merge_sources()
           self.calculate_indicators()
           self.prepare_for_analysis()
           return self.processed_data
       
       def clean(self):
           """Nettoyage des données brutes"""
           # Implémentation détaillée...
           pass
       
       # ... autres méthodes




Formats de sortie
-----------------

Les données traitées sont disponibles en plusieurs formats :

- **Parquet** : pour l'analyse Python (performant)
- **CSV** : pour l'export et compatibilité
- **JSON** : pour l'API web
- **GeoJSON** : pour les visualisations cartographiques