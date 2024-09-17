import sys
import os
from datetime import datetime


if "-d" in sys.argv and "-f" not in sys.argv:
    d_index = sys.argv.index("-d") + 1
    path = os.path.join(*sys.argv[d_index:])
    os.makedirs(path, exist_ok=True)

if "-f" in sys.argv and "-d" not in sys.argv:
    now = datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")

    with open("file.txt", "a") as file:
        file.write(formatted_time + "\n")
        lines = 0
        while True:
            lines += 1
            Enter = input("Enter content line:")
            if Enter == "stop":
                break
            file.write(str(lines) + " " + Enter + "\n")


if "-d" in sys.argv and "-f" in sys.argv:
    dir1 = sys.argv[2]
    dir2 = sys.argv[3]
    path = os.path.join(dir1, dir2)
    os.makedirs(path, exist_ok=True)

    file_path = os.path.join(path, "file.txt")
    now = datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    with open(file_path, "a") as file:
        file.write(formatted_time + "\n")
        lines = 0
        while True:
            lines += 1
            Enter = input("Enter content line:")
            if Enter == "stop":
                break
            file.write(str(lines) + " " + Enter + "\n")
