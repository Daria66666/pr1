import threading
import time
import random

from datetime import datetime

def api():
    time.sleep(3)
    return random.randint(1, 100)


def five():
    start = datetime.now()
    result=0
    for x in range(5):
        result += api()
    execution_time = datetime.now() - start
    print("Время работы: " + str(execution_time.total_seconds()) + ' секунд')
    return result

five()

def potok():
    start = datetime.now()
    threads = []
    for i in range(5):
        t = threading.Thread(target=api)
        t.start()
        threads.append(t)
    thread_number = 1
    summa = 0
    for thread in threads:
        thread.join()
        print("Поток " + str(thread_number) + ' вернул ')
        thread_number = thread_number + 1
    execution_time = datetime.now() - start
    print("Время работы: " + str(execution_time.total_seconds()) + ' секунд')
    return summa

potok()