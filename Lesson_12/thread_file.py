import os
import threading
import time

import requests


def encrypt_file(path: str):
    try:
        _ = open(path)
        print(f"Processing file from {path} in process {os.getpid()}")
    except FileNotFoundError:
        print("error")

    mylist = [i for i in range(100_000_000)]
    del mylist


def download_image(image_url):
    print(
        f"Downloading image from {image_url} in thread {threading.current_thread().name}"
    )
    response = requests.get(image_url)
    with open("image.jpg", "wb") as f:
        f.write(response.content)


def using_threads():

    thread_one = threading.Thread(target=encrypt_file, args=("rockyou.txt",))
    thread_two = threading.Thread(
        target=download_image,
        args=("https://media.gettyimages.com/id/583910668/photo/film-hard-target-by-john-woo.jpg?s=1024x1024&w=gi&k=20&c=XWXPE9W1wdGwxHb2BAV2QlMfPfMy3a5lJdJZrzSNwGY=",),
    )

    point_1 = time.perf_counter()
    thread_one.start()

    point_2 = time.perf_counter()
    thread_two.start()

    thread_one.join()
    fin_point_1 = time.perf_counter()

    thread_two.join()
    fin_point_2 = time.perf_counter()

    encryption_counter = fin_point_1 - point_1
    download_counter = fin_point_2 - point_2
    total = time.perf_counter() - start

    print(
        f"Time taken for encryption task: {encryption_counter}, I/O-bound task: {download_counter}, Total: {total} seconds"
    )


try:
    start = time.perf_counter()

    using_threads()

except Exception as e:
    print(f"Error occurred: {e}")
