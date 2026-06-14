import os

def safe_create_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)
