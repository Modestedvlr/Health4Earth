Installation
============

Pré-requis
----------

Ce projet nécessite **Python 3.10** ou une version supérieure.

Installation via Git
--------------------

Pour installer le package ``health4earth`` et l'utiliser sur votre machine :

.. code-block:: bash

   # 1. Cloner le dépôt
   git clone https://github.com/VOTRE-PSEUDO/Health4Earth.git
   cd Health4Earth

   # 2. Installer les dépendances
   pip install -e .

   # 3. (Optionnel) Installer les outils de développement (tests, doc)
   pip install -e .[dev]

Vérification
------------

Pour vérifier que l'installation a fonctionné :

.. code-block:: python

   import health4earth
   print("Health4Earth est installé !")