project = "SIESTA User Documentation"
author = "EOSC-SIESTA"

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "_ext"))

extensions = ["myst_parser", "youtube_thumbnail"]
source_suffix = {".rst": "restructuredtext", ".md": "markdown"}
master_doc = "index"
language = "en"

html_theme = "shibuya"
html_title = "SIESTA User Guide"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
