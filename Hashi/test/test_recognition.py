import unittest
from Hashi.recognize import *


class TestRecognize(unittest.TestCase):
    def test_recognize_txt_small(self):
        list_x = [350, 250, 250, 350]
        list_y = [50, 150, 250, 350]
        list_circle = recognize_txt("../generated_boards/plansza.txt")
        for i in range(4):
            self.assertEqual(list_circle[i].x, list_x[i])
            self.assertEqual(list_circle[i].y, list_y[i])

    def test_recognize_txt_big(self):
        list_x = [275, 275, 125, 500]
        list_y = [50, 121, 192, 192]
        list_circle = recognize_txt("../generated_boards/plansza1.txt")
        for i in range(4):
            self.assertEqual(list_circle[i].x, list_x[i])
            self.assertEqual(list_circle[i].y, list_y[i])

    def test_recognize_png(self):
        list_x = [50, 550, 250, 550]
        list_y = [150, 150, 250, 250]
        list_circle = recognize("../generated_boards/83492.png")
        for i in range(4):
            print(list_circle[i].x, list_circle[i].y)
            self.assertEqual(list_circle[i].x, list_x[i])
            self.assertEqual(list_circle[i].y, list_y[i])


suite = unittest.TestLoader().loadTestsFromTestCase(TestRecognize)
print(unittest.TextTestRunner(verbosity=3).run(suite))
