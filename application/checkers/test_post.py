import unittest
from .post import post_params_check


class PostCheckTest(unittest.TestCase):
    def test(self):
        self.assertEqual(post_params_check(None), ("ok", True))


if __name__ == '__main__':
    unittest.main()
