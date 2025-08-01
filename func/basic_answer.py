#!/usr/bin/env python

def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def exp(base, pow):
    return base ** pow


def square(base):
    return exp(base, 2)


def greet(이름="낯선자", 나이=20):
    인사 = ""

    if (나이 >= 40):
        인사 = "안녕하십니까"
    elif (나이 >= 20):
        인사 = "안녕하신가"
    else:
        인사 = "안녕"

    return 인사 + f" {이름}!"
