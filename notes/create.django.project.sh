#!/bin/bash


mkdir src db_sqlite static_content
mkdir -p ./docker/{docker,postgres}

touch .env.example docker-compose.yml README.md requirements.txt .gitignor
# touch .gitkeep

# chmod +x pyc.reset.sh
# pythot -m venv django_env