import time, random, queue, threading

file_list = [
    "image_0001.jpg",
    "image_0002.jpg",
    "image_0003.jpg",
    "image_0004.jpg",
    "image_0005.jpg",
    "image_0006.jpg",
    "image_0007.jpg",
    "image_0008.jpg",
    "image_0009.jpg",
    "image_0010.jpg",
    "image_0011.jpg",
    "image_0012.jpg",
    "image_0013.jpg",
    "image_0014.jpg",
    "image_0015.jpg",
]

# add files to job_queue
job_queue = queue.Queue()
for i in file_list:
    job_queue.put(i)


def image_converter():
    while not job_queue.empty():
        image = job_queue.get()

        print(f"Converting {image}...")
        time.sleep(random.randint(3, 10))
        print(f"Convert finished: {image}")

        job_queue.task_done()

for _ in range(16):
    t = threading.Thread(target=image_converter)
    t.start()