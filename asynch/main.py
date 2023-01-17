import multiprocessing
import time
import random

def worker(number):
    sleep = random.randrange(1,5)
    time.sleep(sleep)
    print(f"Я работник {str(number)}, я спал {sleep} секунд!")


if __name__ == '__main__':

    procs = []
    for i in range(5):
        proc = multiprocessing.Process(target=worker, args=(i,))
        proc.start()
        procs.append(proc)

    print("Ну вот и все, ждем наши процессы!")

    for proc in procs:
        proc.join()

    print('Все кончилось')