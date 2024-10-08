# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "pastelpink-modpack"
copyright = "2024, Noelle"
author = "No767"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx_copybutton"]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_title = "Pastelpink Modpack"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_static_path = ["_static"]

html_theme_options = {
    "dark_css_variables": {
        "color-brand-primary": "#A685E2",
        "color-brand-content": "#FFABE1",
    },
    "light_css_variables": {
        "color-brand-primary": "#6867AC",
        "color-brand-content": "#CE7BB0",
    },
}

ogp_site_url = "https://pastelpink-modpack.readthedocs.io"