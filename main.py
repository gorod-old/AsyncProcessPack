# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from time import sleep

from AsyncProcessPack import AsyncProcess


def test_func(num):
    print(f'stream {num} is run')


def end():
    print('end process')


class Test:
    def __init__(self):
        super(Test, self).__init__()
        self.process = AsyncProcess('async process from Test class', self.class_async_func, 2, (self, 'end'))

    @classmethod
    def class_name(cls):
        return cls.__name__

    def class_async_func(self, num):
        print(f'class: {self.class_name()}, stream {num}, is run')

    def end(self):
        print(f'class: {self.class_name()}, end async process')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    process_1 = AsyncProcess('async process test', test_func, 2, (None, end))
    sleep(3)
    process_2 = Test()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
