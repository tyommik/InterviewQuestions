"""
Задача: написать функцию, которая проверяет, все ли символы в строке встречаются один раз.
"""

import unittest

def func (inputString: str) -> bool:
    hashMap = {}
    if inputString != "":
        for letter in inputString:
            if letter not in hashMap:
                hashMap[letter] = 1
            else:
                return False
    else:
        return False
    return True


tc = unittest.TestCase()
tc.assertEqual(func('abcdefg '), True)
tc.assertEqual(func('abcafg'), False)
tc.assertEqual(func(' Try   '), False)
tc.assertEqual(func(' '), True)
tc.assertEqual(func(''), False)