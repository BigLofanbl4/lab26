#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta


class Triad:
    def __init__(self, num_1, num_2, num_3):
        self.num_1 = num_1
        self.num_2 = num_2
        self.num_3 = num_3

    def increment_num_1(self):
        self.num_1 += 1

    def increment_num_2(self):
        self.num_2 += 1

    def increment_num_3(self):
        self.num_3 += 1

    def __repr__(self):
        return f"({self.num_1}, {self.num_2}, {self.num_3})"


class Date(Triad):
    def __init__(self, year, month, day):
        super().__init__(year, month, day)

    # увеличение года на 1
    def increment_num_1(self):
        self.num_1 += 1

    # увеличение месяца на 1
    def increment_num_2(self):
        self.num_2 += 1
        if self.num_2 > 12:
            self.num_2 = 1
            self.increment_num_1()

    # увеличение дней на 1
    def increment_num_3(self):
        self.add_days(1)

    # увеличение на n дней
    def add_days(self, n):
        new_date = datetime(self.num_1, self.num_2, self.num_3) + timedelta(
            days=n
        )
        self.num_1 = new_date.year
        self.num_2 = new_date.month
        self.num_3 = new_date.day


if __name__ == "__main__":
    a = Date(2020, 12, 10)
    a.increment_num_1()
    a.increment_num_2()
    a.increment_num_3()
    print(a)
    a.add_days(5)
    print(a)
