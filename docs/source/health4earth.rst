Health4Earth - Documentation des modules
========================================

.. note::
   Cette documentation est **générée automatiquement** à partir des
   docstrings Python du code source.

Aperçu du package
-----------------

**Health4Earth** est organisé en plusieurs modules spécialisés :

.. list-table:: Modules principaux
   :widths: 30 70
   :header-rows: 1
   
   * - **Module**
     - **Responsabilité**
   * - ``data_ingest``
     - Collecte et chargement des données
   * - ``data_clean``
     - Nettoyage et prétraitement
   * - ``data_transform``
     - Transformations des données
   * - ``analytics``
     - Analyses statistiques
   * - ``viz``
     - Visualisations

Modules de données
------------------

Ces modules gèrent les sources de données spécifiques :

health4earth.data_capitales module
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: health4earth.data_capitales
   :members:
   :show-inheritance:

**Description :** Gestion des données des capitales et villes principales.

health4earth.data_co2 module
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: health4earth.data_co2
   :members:
   :show-inheritance:

**Description :** Données d'émissions CO₂.

Module principal
----------------

.. automodule:: health4earth
   :members:
   :show-inheritance:

**Description :** Point d'entrée principal du package.

