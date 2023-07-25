import os
from dotenv import load_dotenv, find_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

print(f"ORIG_AUTHOR: {os.getenv('ORIG_AUTHOR')}")
