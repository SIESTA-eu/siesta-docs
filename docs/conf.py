project = "SIESTA User Documentation"
author = "EOSC-SIESTA"

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "_ext"))

extensions = ["myst_parser", "youtube_thumbnail"]
source_suffix = {".rst": "restructuredtext", ".md": "markdown"}
master_doc = "index"
language = "en"

html_theme = "sphinx_book_theme"
html_title = "SIESTA User Guide"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_static_path = ["_static"]
html_css_files = ["custom.css"]

html_theme_options = {
    "logo": {
        "image_light": "_static/EOSCSiesta_PosColour.png",
        "image_dark": "_static/EOSCSiesta_White.png",
    },

    "use_download_button": False,
    "use_fullscreen_button": False,
    "use_repository_button": False,
    "use_issues_button": False,
    "use_edit_page_button": False,
    "use_source_button": False,

    "article_header_start": [],

    "show_toc_level": 2,
}
