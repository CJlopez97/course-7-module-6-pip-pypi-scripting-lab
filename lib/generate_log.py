from datetime import datetime
import os
import requests


def generate_log(data):
    if not isinstance(data, list):
        raise ValueError("data must be a list")

    today = datetime.now().strftime("%Y%m%d")
    filename = f"log_{today}.txt"

    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    print(f"Log written to {filename}")

    return filename


def fetch_data():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    if response.status_code == 200:
        return response.json()
    return {}


if __name__ == "__main__":
    post = fetch_data()
    title = post.get("title", "No title found")
    print("Fetched Post Title:", title)

    log_file = generate_log([f"Title: {title}", f"Body: {post.get('body', '')}"])