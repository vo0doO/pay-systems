from psa import psa

import os
import unittest

class AppTestCase(unittest.TestCase):

   def test_root_text(self):
        tester = psa.test_client(self)
        response = tester.get('/')
        assert 'Hello world!' in response.data


if __name__ == '__main__':
    unittest.main()
