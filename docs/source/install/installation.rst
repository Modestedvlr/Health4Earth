Installation
============

Cette section guide l'installation du projet Health4Earth sur votre machine locale.

Pré-requis
----------

Avant de commencer, assurez-vous d'avoir :

.. list-table::
   :widths: 40 60
   :header-rows: 1
   
   * - Logiciel
     - Version minimale
   * - **Python**
     - 3.10 ou supérieur
   * - **Git**
     - 2.30+
   * - **pip** (gestionnaire de paquets Python)
     - 22.0+
   * - **Mémoire RAM**
     - 8 Go (16 Go recommandé)

.. note::
   Nous recommandons fortement l'utilisation d'un **environnement virtuel Python**
   pour isoler les dépendances du projet.

Installation via Git
--------------------

1. **Cloner le dépôt**

Récupérez le code source depuis GitHub :

.. code-block:: bash

   git clone https://github.com/Modestedvlr/Health4Earth.git

**Explication :** Cette commande télécharge l'intégralité du projet sur votre machine.

2. **Accéder au dossier**

Déplacez-vous dans le dossier du projet :

.. code-block:: bash

   cd Health4Earth

**Explication :** Toutes les commandes suivantes doivent être exécutées depuis ce dossier.

3. **Créer un environnement virtuel**

Isolez les dépendances du projet :

.. code-block:: bash

   python -m venv venv

**Explication :** Crée un environnement Python isolé nommé "venv".

4. **Activer l'environnement**

Activez l'environnement selon votre système :

.. code-block:: bash
   :caption: Windows

   venv\Scripts\activate

.. code-block:: bash
   :caption: Linux/Mac

   source venv/bin/activate

**Explication :** Votre terminal est maintenant dans l'environnement virtuel.

 5. **Installer le package**

Installez Health4Earth en mode développement :

.. code-block:: bash

   pip install -e .

**Explication :** Le point `.` signifie "dossier courant". Le mode `-e` permet des modifications sans réinstallation.

6. **Installer les dépendances de développement**

Pour contribuer au code ou à la documentation :

.. code-block:: bash

   pip install -e .[dev]

**Explication :** Installe les outils supplémentaires pour les tests et la qualité de code.

Vérification
------------

**Test d'import**
Vérifiez que l'installation a réussi :

.. code-block:: python

   import health4earth
   print("Health4Earth est correctement installé !")

**Explication :** Si aucun message d'erreur n'apparaît, l'installation est réussie.

**Vérification de version**

Affichez la version installée :

.. code-block:: bash

   python -c "import health4earth; print(f'Version : {health4earth.__version__}')"

**Explication :** Affiche la version exacte du package.

Structure créée
---------------

Après installation, votre projet aura cette structure :

::

   Health4Earth/
   ├── health4earth/     # Code source principal
   ├── docs/            # Documentation
   ├── tests/           # Tests unitaires
   ├── data/            # Dossiers pour les données
   ├── venv/            # Environnement virtuel (créé par vous)
   └── requirements.txt # Dépendances Python

Dépannage rapide
----------------

**"Command not found: python"**

Utilisez `python3` ou installez Python.

**"ModuleNotFoundError"**

Vérifiez que vous êtes dans l'environnement virtuel (vous devriez voir `(venv)` devant votre prompt).

**Problèmes de permissions sur Windows**
Ajoutez `--user` à la commande pip : `pip install --user -e .`

.. important::
   En cas de problème, consultez la section complète de dépannage dans la documentation.