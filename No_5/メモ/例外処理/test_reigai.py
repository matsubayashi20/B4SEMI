from unittest import TestCase
from reigai import cnt



class TestCnt(TestCase):
    def setUp(self):
        print("begin")

    def tearDown(self):
        print("end")

    def test_cnt(self):
        self.assertEqual(10, cnt(1))
        self.assertEqual(None, cnt(-1))
        self.assertIsInstance(cnt(100),ValueError)
        with self.assertRaises(TypeError):
            cnt(101)
        # self.assertEqual(10, cnt(101))


if __name__ == "__main__":
    unittest.main()
