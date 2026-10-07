# PROGRAMACIÓN II
# Python / Odoo / Django
# =========================================================

# ---------------------------------------------------------
# PYTHON
# ---------------------------------------------------------

# Caché de Python
__pycache__/
*.py[cod]
*$py.class

# Archivos compilados
*.so

# Entornos virtuales
.venv/
venv/
env/
ENV/

# Variables de entorno
.env
.env.*
!.env.example

# Configuración de herramientas
.pytest_cache/
.mypy_cache/
.ruff_cache/
.coverage
.coverage.*
htmlcov/

# Jupyter Notebook
.ipynb_checkpoints/

# ---------------------------------------------------------
# DJANGO
# ---------------------------------------------------------

# Base de datos local
db.sqlite3
db.sqlite3-journal

# Archivos estáticos y media generados
staticfiles/
media/

# ---------------------------------------------------------
# ODOO
# ---------------------------------------------------------

# Archivos temporales
*.log

# Filestore generado por Odoo
filestore/

# Sesiones
sessions/

# Configuración local
odoo.conf

# ---------------------------------------------------------
# SISTEMAS OPERATIVOS
# ---------------------------------------------------------

# Linux
*~

# Windows
Thumbs.db
ehthumbs.db
Desktop.ini

# macOS
.DS_Store

# ---------------------------------------------------------
# EDITORES / IDE
# ---------------------------------------------------------

# Visual Studio Code
.vscode/

# PyCharm / IntelliJ
.idea/

# Sublime Text
*.sublime-workspace
*.sublime-project


# SECRETOS / CREDENCIALES

*.pem
*.key
*.crt

# Nunca subir contraseñas
secrets.json
credentials.json

-
# ARCHIVOS TEMPORALES


*.tmp
*.temp
*.swp
*.swo
