import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s:%(message)s]')


list_of_files=[
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "research/trails.ipynb",
    "app.py"
    "store_index.py",
    "static",
    "templates/chat.html"
]

for filePath in list_of_files:
    filepath = Path(filePath)
    fileDir, fileName= os.path.split(filepath)
    print(fileDir, fileName)
    if fileDir != "":
        os.makedirs(fileDir, exist_ok=True)
        logging.info(f"creating Directory ; {fileDir} for the file {fileName}")
    if fileName !="":
        if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
            with open(filepath, 'w' ) as f:
                logging.info(f"Creating empty file :{filepath}")
                pass
        else:
            logging.info(f"{fileName} is already Exist")
                