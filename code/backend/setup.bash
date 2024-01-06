#!/bin/bash

# Nazwa projektu
PROJECT_NAME="env"

# Tworzenie wirtualnego środowiska
python3 -m venv $PROJECT_NAME

# Aktywacja wirtualnego środowiska
source $PROJECT_NAME/bin/activate

# Instalacja zależności
pip install -r requirements.txt  

echo "Wirtualne środowisko zostało utworzone i zależności zostały zainstalowane."
