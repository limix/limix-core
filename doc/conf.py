from __future__ import unicode_literals

import os

try:
    import limix_core
    version = limix_core.__version__
except ImportError:
    version = 'unknown'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
]
napoleon_google_docstring = True
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = 'limix-core'
copyright = '2017, Stegle group'
author = 'Stegle group'
release = version
language = None
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'conf.py']
pygments_style = 'sphinx'
todo_include_todos = False
html_theme = 'default'
htmlhelp_basename = 'limix-coredoc'
latex_elements = {
}
latex_documents = [
    (master_doc, 'limix-core.tex', 'limix-core Documentation',
     'Stegle group', 'manual'),
]
man_pages = [
    (master_doc, 'limix-core', 'limix-core Documentation',
     [author], 1)
]
texinfo_documents = [
    (master_doc, 'limix-core', 'limix-core Documentation',
     author, 'limix-core', 'One line description of project.',
     'Miscellaneous'),
]

intersphinx_mapping = {'https://docs.python.org/': None}
