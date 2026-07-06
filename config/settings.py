"""
===========================================================
Heritage Operations Center
Global Application Settings
===========================================================
"""

from pathlib import Path

# ===========================================================
# Application Information
# ===========================================================

APP_NAME = "Heritage Operations Center"
APP_SHORT_NAME = "HOC"

VERSION = "1.0.0"

COMPANY = "Majesco"

AUTHOR = "Atima Tiwari"

# ===========================================================
# Base Directory
# ===========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

# ===========================================================
# Project Directories
# ===========================================================

CONFIG_DIR = BASE_DIR / "config"

STATIC_DIR = BASE_DIR / "static"

TEMPLATE_DIR = BASE_DIR / "templates"

SERVICE_DIR = BASE_DIR / "services"

LOG_DIR = BASE_DIR / "logs"

UPLOAD_DIR = BASE_DIR / "uploads"

DOWNLOAD_DIR = BASE_DIR / "downloads"

TEMP_DIR = BASE_DIR / "temp"

HISTORY_DIR = BASE_DIR / "history"

# ===========================================================
# Excel Configuration
# ===========================================================

EXCEL_DIR = CONFIG_DIR / "excel"

ENVIRONMENT_FILE = EXCEL_DIR / "Environment.xlsx"

DEPLOYMENT_FILE = EXCEL_DIR / "Heritage_deployment_details.xlsx"

# ===========================================================
# Dashboard
# ===========================================================

AUTO_REFRESH = True

AUTO_REFRESH_INTERVAL = 15

DEFAULT_THEME = "dark"

SHOW_CHARTS = True

SHOW_RECENT_ACTIVITY = True

SHOW_NOTIFICATIONS = True

SHOW_SERVER_STATUS = True

# ===========================================================
# Login
# ===========================================================

ENABLE_LOGIN = False

SESSION_TIMEOUT = 30

# ===========================================================
# Logging
# ===========================================================

LOG_LEVEL = "INFO"

LOG_FILE = LOG_DIR / "heritage_operations.log"

# ===========================================================
# Modules
# ===========================================================

ENABLE_RESTART_CENTER = True

ENABLE_DEPLOYMENT_CENTER = True

ENABLE_REPOSITORY = True

ENABLE_DATABASE = True

ENABLE_UTILITIES = True

ENABLE_REPORTS = True

ENABLE_HISTORY = True

ENABLE_JBEAM = True

ENABLE_SSH = True
