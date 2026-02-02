import requests
import gzip
import shutil
import os

def download_and_unzip(url, output_gz, output_csv):
    os.makedirs(os.path.dirname(output_csv), exist_ok=True)

    response = requests.get(url, timeout=60)
    response.raise_for_status()

    with open(output_gz, "wb") as f:
        f.write(response.content)

    with gzip.open(output_gz, "rb") as f_in:
        with open(output_csv, "wb") as f_out:
            shutil.copyfileobj(f_in, f_out)
