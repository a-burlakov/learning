import threading
import time
import random

def worker(number):
    sleep = random.randrange(1,5)
    time.sleep(sleep)
    print(f"Я работник {str(number)}, я спал {sleep} секунд!")

for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    t.start()

print("Ну вот и все, ждем наши треды!")

main_thread = threading.main_thread()
for t in threading.enumerate():
    if t is main_thread:
        continue
    t.join()

print('Все кончилось')