import os
import sys
import sphinx_rtd_theme  # <--- Important d'importer le module

sys.path.insert(0, os.path.abspath('../../'))

project = 'Health4Earth'
copyright = '2025, Health4Earth Team'
author = 'Health4Earth Team'
release = '0.1'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx_rtd_theme',
    'sphinx.ext.imgmath',
    'sphinx.ext.todo',    # <--- Important de l'ajouter ici
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_rtd_theme'  # <--- Le thème qu'on veut
html_static_path = ['_static']

html_sidebars = {
    '**': ['globaltoc.html', 'relations.html', 'sourcelink.html', 'searchbox.html']
}


# --- Configuration CSS Personnalisée ---
# Pour que la doc prenne toute la largeur de l'écran
def setup(app):
    app.add_css_file('custom.css')