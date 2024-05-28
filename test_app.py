'''
Date: 2024-05-28 08:44:20
LastEditors: 牛智超
LastEditTime: 2024-05-28 08:44:41
FilePath: \自动化脚本\test_app.py
'''
import unittest
from app import hello_world

class TestApp(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_world(), "Hello, World!")

if __name__ == '__main__':
    unittest.main()
