# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'My PDS Project'
copyright = '2021 California Institute of Technology'
author = 'NASA Planetary Data System'
release = '0.0'
version = '0.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.autosummary',
    'sphinx_rtd_theme',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.redoc'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- Read the docs config -------

html_logo = '_static/images/PDS_Planets.png'

redoc_uri = 'https://cdn.jsdelivr.net/npm/redoc@2.0.0-alpha.17/bundles/redoc.standalone.js'

redoc = [
    {
        'name': 'PDS Search API',
        'page': 'specifications/search-v0.4.1-redoc',
        'spec': '../../specs/PDS_APIs-search-0.4.1-swagger.yaml',
        'embed': True,
    },
    {
        'name': 'PDS Search API',
        'page': 'specifications/search-v1.0.0-SNAPSHOT-redoc',
        'spec': '../../specs/PDS_APIs-search-1.0.0-SNAPSHOT-swagger.yaml',
        'embed': True,
    },
    {
        'name': 'PDS DOI API',
        'page': 'specifications/doi-v0.2-redoc',
        'spec': '../../specs/PDS_APIs-doi-0.2-swagger.yaml',
        'embed': True,
    }
]

