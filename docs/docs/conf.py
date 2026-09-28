import os
import sys
from unittest.mock import MagicMock

# 1. Заглушка для OpenAPI моделей FastAPI (устраняет ошибку Pydantic v2)
sys.modules['fastapi.openapi.models'] = MagicMock()

# 2. Добавляем корневую папку проекта в путь поиска модулей Python
sys.path.insert(0, os.path.abspath('..'))

# --- Основные настройки проекта ---
project = 'REST API Docs'
copyright = '2026, Developer'
author = 'Developer'

# --- Расширения Sphinx ---
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# --- Настройки оформления (Тема) ---
html_theme = 'alabaster'
html_static_path = ['_static']
# Fix for Pydantic / Sphinx Dict NameError
import typing
typing.Dict = typing.Dict
