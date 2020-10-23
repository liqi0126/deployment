import unittest
from .reply import reply_post_params_check


class ReplyCheckTest(unittest.TestCase):
    def test(self):
        self.assertEqual(reply_post_params_check(None), ("ok", True))


if __name__ == '__main__':
    unittest.main()
