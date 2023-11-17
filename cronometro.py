import time
import os

class Cronometro:
    def __init__(self, seg = 0, minu = 0, horas = 0):
        self.seg = seg
        self.minu = minu
        self.horas = horas

    def __repr__(self):
        return f'{self.horas:02d}:{self.minu:02d}:{self.seg:02d}'
        
    def incremento(self):
        self.seg += 1
        if self.seg >= 60:
            self.seg = 0
            self.minu += 1
        if self.minu >= 60:
            self.minu = 0
            self.horas += 1

    def start(self):
        while True:
            os.system('cls')
            print(self)
            self.incremento()
            time.sleep(1)

cronometro1 = Cronometro()

cronometro1.start()


