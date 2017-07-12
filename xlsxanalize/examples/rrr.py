#!/usr/bin/env python3
import sys


class Water:
    def get_something(self):
        print('Вот налили воды')
class Sand:
    def get_something(self):
        print('Вот насыпали песку')
class Stone:
    def get_something(self, theme: str):
        print('Отломили кусок камня')

class Something:

    def __init__(self, store_type):

        self.store_name = store_type

    def get_something(self):
        return getattr(sys.modules[__name__], self.store_name)

if __name__ == "__main__":
    print("Начинаем !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    p = Something('water')
    p.get_something()
    p = Something('stone')
    p.get_something()
    p = Something('sand')
    p.get_something()