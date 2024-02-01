import logging
import os
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s")

PROJECT_NAME = "phone_recommender"

list_of_file = [
    ".github/workflow/.gitkeep",
    f"src/{PROJECT_NAME}/__init__.py",
    f"src/{PROJECT_NAME}/constants/__init__.py",
    f"src/{PROJECT_NAME}/logging/__init__.py",
    f"src/{PROJECT_NAME}/utils/__init__.py",
    f"src/{PROJECT_NAME}/utils/common.py",
    f"src/{PROJECT_NAME}/entity/__init__.py",
    f"src/{PROJECT_NAME}/config/__init__.py",
    f"src/{PROJECT_NAME}/config/configuration.py",
    f"src/{PROJECT_NAME}/components/__init__.py",
    f"src/{PROJECT_NAME}/pipeline/__init__.py",
    "research/trails.ipynb",
    "config/config.yaml",
    "templates/index.html",
    "staticFiles/index.css",
    "requirements.txt",
    "setup.py",
    "params.yaml",
    "main.py",
    "app.py",
]


for filepath in list_of_file:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    # print(filedir, filename)

    if filedir != "":
        # print(filedir)
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating folder: {filedir} for {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        # print(filename)
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating file: {filename} in {filedir}")

    else:
        logging.info(f"{filepath} already exists!")
