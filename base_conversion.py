"""
https://www.codewars.com/kata/526a569ca578d7e6e300034e
"""

def bin2dec(data: str) -> str:
    dec = 0
    for i, d in enumerate(data[::-1]):
        dec += int(d) * (2**i)
    return str(dec)

def dec2bin(data: str) -> str:
    arr = []
    data = int(data)
    while True:
        quotient = data // 2
        remainder = data % 2
        arr.append(str(remainder))
        if quotient == 0:
            break
        data = quotient
    return "".join(arr[::-1])

# from typing import Union
from enum import Enum

class ConversionBase(str, Enum):
    bin      = '01'
    oct      = '01234567'
    dec      = '0123456789'
    hex      = '0123456789abcdef'
    allow    = 'abcdefghijklmnopqrstuvwxyz'
    allup    = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alpha    = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphanum = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def __str__(self) -> str:
        return self.value
    
    # def get_map(cls) -> dict[int, str]:
    #     _map = {
    #         i: char 
    #         for i, char in enumerate(cls.)
    #     }
    #     return _map

def char2value(base: str):
    _map = {
        char: i 
        for i, char in enumerate(base)
    }
    return _map

def value2char(base: str):
    _map = {
        i: char 
        for i, char in enumerate(base)
    }
    return _map

# print(ConversionBase.bin.value)
# print(ConversionBase.hex)


def dec2any(data: str, target: ConversionBase) -> str:
    print(f"{data=}, {target=}")

    _map = value2char(target)
    print(f"{_map=}")

    denominator = len(target)
    print(f"{denominator=}")

    arr = []
    data = int(data)
    while True:
        quotient = data // denominator
        remainder = data % denominator
        print(f"{quotient=}, {remainder=}")
        arr.append(_map.get(remainder))
        if quotient == 0:
            break
        data = quotient
    print(f"{arr=}")
    return "".join(arr[::-1])


def any2dec(data: str, source: ConversionBase) -> str:
    print(f"{data=}, {source=}")

    _map = char2value(source)
    print(f"{_map=}")

    base_value = len(source)
    print(f"{base_value=}")

    output = 0
    for i, d in enumerate(data[::-1]):
        print(f"{i=}, {d=}, {(base_value**i)=}")
        output += _map.get(d) * (base_value**i)
    return str(output)


def convert(input, source, target):
    if source == target:
        return input
    
    dec = any2dec(input, source)
    print(f"convert: {dec=}")
    res = dec2any(dec, target)
    return res


def main():
    print(bin2dec("1111"))
    print(dec2bin("15"))

    a = dec2bin("123")
    b = bin2dec(a)
    print(a,b)
    print()

    test_cases = [
        ("15", ConversionBase.dec, ConversionBase.bin),
        ("15", ConversionBase.dec, ConversionBase.oct),
        ("1010", ConversionBase.bin, ConversionBase.dec),
        ("1010", ConversionBase.bin, ConversionBase.hex),
        ("0", ConversionBase.dec, ConversionBase.alpha),
        ("27", ConversionBase.dec, ConversionBase.allow),
        ("hello", ConversionBase.allow, ConversionBase.hex),
        ("SAME", ConversionBase.allup, ConversionBase.allup),
    ]
    for case in test_cases:
        print(convert(*case))
        print()

main()
