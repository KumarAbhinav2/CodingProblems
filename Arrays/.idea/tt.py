from multiprocessing import Process
from multiprocessing import current_process
import os


def process_task(x1, x2, x2, k1, k2):
    print("{0} has pid: {1} with parent pid: {2}".format(current_process().name, os.getpid(), os.getppid()))
    print("Recieved Arguments..{0}".format(x1, x2, x3))

if __name__ == "__main__":
    process = [0] * 3

    for i in range(0, 3):
        process[i] = Process(target=process_task, name="process-{0}".format(i))
        process[i].start()

    for i in range(0, 3):
        process[i].join()

    print("{0} has pid: {1} ".format(current_process().name, os.getpid()))