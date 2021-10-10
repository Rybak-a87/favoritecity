import os


def connect_database(*args, **kwargs) -> dict:
    if mysql_database := os.getenv('MYSQL_DATABASE'):
        databases = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': mysql_database,
                'USER': os.getenv('MYSQL_USER'),
                'PASSWORD': os.getenv('MYSQL_PASSWORD'),
                'HOST': os.getenv('MYSQL_HOST'),
                'PORT': '3306',
                'STORAGE_ENGINE': 'InnoDB',
                'OPTIONS': {
                    'charset': 'utf8mb4',
                    'isolation_level': "repeatable read",
                },
            },
        }
    elif postgres_database := os.getenv('POSTGRES_DATABASE'):
        databases = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': postgres_database,
                'USER': os.getenv('POSTGRES_USER'),
                'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
                'HOST': os.getenv('POSTGRES_HOST'),
                'PORT': '5432',
                # 'STORAGE_ENGINE': 'InnoDB',
                # 'OPTIONS': {
                #     'charset': 'utf8mb4',
                #     'isolation_level': "repeatable read",
                # },
            },
        }
    else:
        path = kwargs.get("project_path")
        databases = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                # 'NAME': PROJECT_PATH / "database_sqlite" / "db.sqlite3",
                "NAME": os.path.join(path, "database_sqlite", "db.sqlite3"),
            },
        }
    return databases
