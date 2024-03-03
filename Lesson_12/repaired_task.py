import multiprocessing
import os
import threading
import time

import requests


def encrypt_file(path: str):
    try:
        _ = open(path)
        print(f"Processing file from {path} in process {os.getpid()}\n")
    except FileNotFoundError:
        print("error")

    mylist = [i for i in range(100_000_000)]
    del mylist


def download_image(image_url, name):
    print(f"Downloading image from {image_url} in {name}\n")
    response = requests.get(image_url)
    with open("media/image_01.jpg", "wb") as f:
        f.write(response.content)


def using_threads():

    thread_one = threading.Thread(target=encrypt_file, args=("media/rockyou.txt",))
    thread_two = threading.Thread(
        target=download_image,
        args=(
            "https://media.gettyimages.com/id/535978976/photo/actor-jean-claude-van-damme-at-gym.jpg?s=1024x1024&w=gi&k=20&c=kNL4L3IN2YMYlP665VbBGDD97L4Y5bg1J2P26Dw7PcU=",
            threading.current_thread().name,
        ),
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
        f"When using threads, time taken for encryption task: {encryption_counter}, I/O-bound task: {download_counter}, Total: {total} seconds"
    )


def using_processes():

    process_one = multiprocessing.Process(target=encrypt_file, args=("media/rockyou.txt",))
    process_two = multiprocessing.Process(
        target=download_image,
        args=(
            "https://media.gettyimages.com/id/583910668/photo/film-hard-target-by-john-woo.jpg?s=1024x1024&w=gi&k=20&c=XWXPE9W1wdGwxHb2BAV2QlMfPfMy3a5lJdJZrzSNwGY=",
            multiprocessing.current_process().name,
        ),
    )

    point_1 = time.perf_counter()
    process_one.start()

    point_2 = time.perf_counter()
    process_two.start()

    process_one.join()
    fin_point_1 = time.perf_counter()

    process_two.join()
    fin_point_2 = time.perf_counter()

    encryption_counter = fin_point_1 - point_1
    download_counter = fin_point_2 - point_2
    total = time.perf_counter() - start

    print(
        f"When using processes, time taken for encryption task: {encryption_counter}, I/O-bound task: {download_counter}, Total: {total} seconds"
    )


if __name__ == "__main__":
    start = time.perf_counter()

    using_threads()
    # using_processes()
