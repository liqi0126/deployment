import unittest
from .user import register_params_check


class UserCheckTest(unittest.TestCase):
    def test(self):
        self.assertEqual(register_params_check(None), ("ok", True))


if __name__ == '__main__':
    unittest.main()
