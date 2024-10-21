import threading

def print_numbers():
    for i in range(1,6):
        print(i)

thread = threading.Thread(target=print_numbers)

thread.start()

thread.join()

print("thread finishe")