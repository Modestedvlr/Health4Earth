import os
import sys
# On ajoute le chemin vers le code source
sys.path.insert(0, os.path.abspath('../../'))

# -- Project information -----------------------------------------------------
project = 'Health4Earth'
copyright = '2025, Master SSD Team'
author = 'Dossou Modeste AGOSSOU, Firdaousse KARIMOU, Julien OLLIER'
release = '1.0'

# -- General configuration ---------------------------------------------------
# L'ajout clé ici est 'sphinx.ext.napoleon' pour lire les docstrings complexes
# et 'sphinx.ext.viewcode' pour voir le code source sur le site.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx_rtd_theme'
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Configuration CSS pour le plein écran (ce qu'on a fait avant)
def setup(app):
    app.add_css_file('custom.css')