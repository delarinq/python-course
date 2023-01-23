import threading
import time

class CountdownThread(threading.Thread):
    instNumber = 0
    number = 0
    def __init__(self):
        super().__init__()
        self.daemon = True
        CountdownThread.instNumber+=1
        self.number = CountdownThread.instNumber

    def run(self):
        print(f'Поток {self.number} запущен')
        for i in range(10, 0, -1) :
            print(f'Поток {self.number}: {i}')
            time.sleep(1)
        print(f'Поток {self.number} завершил работу')
        
t1 = CountdownThread();
t2 = CountdownThread();
t1.start()
t2.start()
t1.join()
t2.join()