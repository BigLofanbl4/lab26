# #!/usr/bin/env python
# # -*- coding: utf-8 -*-

from abc import ABC, abstractmethod


class Series(ABC):
    @abstractmethod
    def get_element(self, n):
        pass

    @abstractmethod
    def get_sum(self, n):
        pass


class Linear(Series):
    def __init__(self, a1, d):
        self.a1 = a1
        self.d = d

    def get_element(self, n):
        return self.a1 + (n - 1) * self.d

    def get_sum(self, n):
        return n * (self.a1 + self.get_element(n)) / 2


class Exponential(Series):
    def __init__(self, a1, q):
        self.a1 = a1
        self.q = q

    def get_element(self, n):
        return self.a1 * (self.q ** (n - 1))

    def get_sum(self, n):
        if self.q == 1:
            return n * self.a1
        else:
            return self.a1 * (1 - self.q**n) / (1 - self.q)


if __name__ == "__main__":
    linear = Linear(1, 5)
    print(linear.get_element(4))
    print(linear.get_sum(10))

    exponential = Exponential(2, 3)
    print(exponential.get_element(4))
    print(exponential.get_sum(10))
