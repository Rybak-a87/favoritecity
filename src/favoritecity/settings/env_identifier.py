import os
from pathlib import Path


PROJECT_PATH = os.environ.get('PROJECT_ROOT', Path(__file__).resolve().parent.parent.parent.parent)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY_DJ", "debug_secret_key")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("SERVER", "dev") == "dev"
