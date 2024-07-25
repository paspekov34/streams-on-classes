import time
from threading import Thread


class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.knight_fight = 100
        self.days = 0


    def run(self):
        print(f'{self.name}, на нас напали!')
        while self.knight_fight > 0:
            self.knight_fight -= self.power
            self.days += 1
            time.sleep(1)
            print(f'{self.name} сражается {self.days} день(дня)..., осталось {self.knight_fight} воинов."')

        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")


# Создание рыцарей
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

# Запуск потоков
first_knight.start()
second_knight.start()

# Ожидание завершения потоков
first_knight.join()
second_knight.join()

print("Все битвы закончились!")
