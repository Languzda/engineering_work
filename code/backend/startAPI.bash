#!/bin/bash
PROJECT_NAME="env"
source $PROJECT_NAME/bin/activate

uvicorn api:app