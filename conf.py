tl_ref_url = 'http://NoSpamPlus.tk'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]


source_suffix = ['.rst', '.md']

master_doc = 'index'

project = 'NoSpamPlus'
copyright = '2020 - Midhun Km'
author = 'Midhun Km'



html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'collapse_navigation': True,
    'display_version': True,
    'navigation_depth': 3,
}

html_sidebars = {
    '**': [
        'globaltoc.html',
        'relations.html',
        'searchbox.html',
    ]
}

htmlhelp_basename = 'NoSpamPlus'
