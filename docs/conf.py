import os
import sys
import typing

# 1. Устанавливаем фиктивные переменные окружения для Pydantic Settings
os.environ.setdefault("DATABASE_URL", "postgresql+asyncpg://postgres:5000@localhost:5432/db")
os.environ.setdefault("SECRET_KEY", "secret_key_for_sphinx_build_12345")
os.environ.setdefault("MAIL_USERNAME", "example@test.com")
os.environ.setdefault("MAIL_PASSWORD", "password")
os.environ.setdefault("MAIL_FROM", "example@test.com")
os.environ.setdefault("MAIL_PORT", "465")
os.environ.setdefault("MAIL_SERVER", "smtp.test.com")
os.environ.setdefault("CLOUDINARY_NAME", "test_name")
os.environ.setdefault("CLOUDINARY_API_KEY", "123456789")
os.environ.setdefault("CLOUDINARY_API_SECRET", "secret")

# 2. Добавляем путь к исходному коду проекта
sys.path.insert(0, os.path.abspath('..'))

# --- Основные настройки ---
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

# --- Оформление ---
html_theme = 'alabaster'
html_static_path = ['_static']
autodoc_typehints = "none"
