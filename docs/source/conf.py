import os
import sys
# C'est ici qu'on dit à Sphinx où trouver votre code
sys.path.insert(0, os.path.abspath('../../'))

# --- Configuration des extensions ---
extensions = [
    'sphinx.ext.autodoc',      # Pour lire vos docstrings
    'sphinx.ext.napoleon',     # Pour le format Google/NumPy
    'sphinx.ext.viewcode',     # Pour mettre des liens vers le code source
]

# --- Thème graphique ---
html_theme = 'sphinx_rtd_theme'
project = 'HEALTH4EARTH'
copyright = '2025, HEALTH4EARTH TEAM'
author = 'HEALTH4EARTH TEAM'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'fr'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
