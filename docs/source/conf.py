# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Explore Sphinx with PlantUML and my extensions'
copyright = '2024, Françoise CONIL'
author = 'Françoise CONIL'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
        'sphinx.ext.intersphinx',
        'sphinxcontrib.plantuml',
        'sphinxcontrib.mermaid',
        'hoverxref.extension'
        ]

templates_path = ['_templates']
exclude_patterns = []

language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']

# -- Options for intersphinx  ------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html
intersphinx_mapping = {
        'python': ('https://docs.python.org/3', None),
        'readthedocs': ('https://docs.readthedocs.io/en/stable/', None),
        'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
        'ntt': ('https://ntt.readthedocs.io/en/latest/', None),
        }

# -- Options for PlantUML ----------------------------------------------------
# Based on https://github.com/readthedocs/readthedocs.org/issues/9958
local_plantuml_path = os.path.join(os.path.dirname(__file__), "utils", "plantuml-lgpl-1.2024.4.jar")
plantuml = f"java -Djava.awt.headless=true -jar {local_plantuml_path}"

# -- Options for sphinxcontrib.mermaid extension  ------------------------------
mermaid_init_js = """mermaid.initialize({
    startOnLoad: true, 
    sequence: {showSequenceNumbers: true}
});"""

# -- Options for hoverxref ---------------------------------------------------
# https://github.com/readthedocs/sphinx-hoverxref/blob/main/docs/conf.py
hoverxref_intersphinx = [
    'readthedocs',
    'sphinx',
    'python',
    'ntt'
]
