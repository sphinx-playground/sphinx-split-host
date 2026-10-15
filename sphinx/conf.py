import os
import sys

# --- PICK ONE --------------------------------------------------------#
# For local VM builds, step one level up to look for your codebase repository:
# sys.path.insert(0, os.path.abspath('..'))

# For the GitHub Cloud Runner, point to the parallel sibling folder that was cloned by the CI workflow:
sys.path.insert(0, os.path.abspath('../../sphinx-split-host'))
# ---------------------------------------------------------------------#

project = 'Sphinx Sandbox: Docs Pipeline'
copyright = '2026, Elliria'
author = 'Elliria'

extensions = [
    'sphinx.ext.autodoc',  # The engine that executes the code to grab docstrings
    'sphinx.ext.viewcode', # Adds handy "[source]" links to your compiled site
]

html_theme = 'sphinx_rtd_theme'
