import os
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

# URL template
BASE_URL = "https://www.aldiwan.net/poem{}.html"
SAVE_DIR = "poems_html"

if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)


def download_poem(poem_id):
    file_path = os.path.join(SAVE_DIR, f"poem_{poem_id}.html")

    if os.path.exists(file_path):
        print(f"Poem {poem_id} already exists, skipping download.")
        return

    url = BASE_URL.format(poem_id)
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(response.text)
            print(f"Downloaded poem {poem_id}")
        else:
            print(f"Poem {poem_id} not found (status code: {response.status_code})")
    except requests.RequestException as e:
        print(f"Error downloading poem {poem_id}: {e}")


def download_poems(start_id, end_id, max_workers=10):
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {
            executor.submit(download_poem, poem_id): poem_id
            for poem_id in range(start_id, end_id)
        }

        for future in as_completed(futures):
            future.result()


if __name__ == "__main__":
    start_time = time.time()

    download_poems(0, 125000, max_workers=5)

    end_time = time.time()
    print(f"Downloading completed in {end_time - start_time:.2f} seconds.")
