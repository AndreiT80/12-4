# Домашнее задание по теме "Логирование"  tests_12_4.py

from runner import Runner, Tournament
import logging
import unittest


first = Runner('Вося', 10)
second = Runner('Илья', 5)
third = Runner('Арсен', 10)

tour = Tournament(101, first, second)
print(tour.start())


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            obj1 = Runner('Вася', -3)
            for i in range(10):
                obj1.walk()
            self.assertEqual(obj1.distance, 100)
            logging.INFO("'test_walk' выполнен успешно")
        except ValueError as err:
            logging.WARNING("Неверная скорость для Runner", exc_info=True)


    def test_run(self):
        try:
            obj2 = Runner(222, 10)
            for i in range(10):
                obj2.run()
            self.assertEqual(obj2.distance, 100)
            logging.INFO("'test_run' выполнен успешно'")
        except TypeError as err:
            logging.WARNING("Неверный тип данных для объекта Runner", exc_info=True)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log",
                    encoding="utf-8", format="%(asctime)s | %(levelname)s | %(message)s")

#    python -m unittest -v test_12_4.py