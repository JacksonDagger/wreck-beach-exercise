import unittest
import wreckBeach
import ISexception

class TestWreck(unittest.TestCase):
    def test_01(self):
        thrown = False
        stamina = 1
        stair = [1]
        try:
            finstam = wreckBeach.wreckMain(stair, stamina)
        except ISexception.InsufficientStaminaException:
            thrown = True
        assert thrown

    def test_02(self):
        thrown = False
        stamina = 2
        stair = [1,1]
        try:
            finstam = wreckBeach.wreckMain(stair, stamina)
        except ISexception.InsufficientStaminaException:
            thrown = True
        assert thrown

    def test_03(self):
        thrown = False
        stamina = 2
        stair = [1, 1, 1]
        try:
            finstam = wreckBeach.wreckMain(stair, stamina)
        except ISexception.InsufficientStaminaException:
            thrown = True
        assert thrown

    def test_04(self):
        thrown = False
        stamina = 4
        stair = [1,1,1]
        try:
            finstam = wreckBeach.wreckMain(stair, stamina)
        except ISexception.InsufficientStaminaException:
            thrown = True
        self.assertFalse(thrown)
        self.assertEqual(finstam, 1)

    def test_05(self):
        thrown = False
        stamina = 1
        stair = [0]
        try:
            finstam = wreckBeach.wreckMain(stair, stamina)
        except ISexception.InsufficientStaminaException:
            thrown = True
        self.assertFalse(thrown)
        self.assertEqual(finstam, 1)

    def test_06(self):
        thrown = False
        stamina = 10
        stair = [0,2,0,2,0,3,1,4]
        try:
            finstam = wreckBeach.wreckMain(stair, stamina)
        except ISexception.InsufficientStaminaException:
            thrown = True
        self.assertFalse(thrown)
        self.assertEqual(finstam, 5)

    def test_07(self):
        thrown = False
        stamina = 9
        stair = [0, 100, 0, 0, 0, 999, 0, 0, 0, 0, 0, 999, 0, 0, 5, 5]
        try:
            finstam = wreckBeach.wreckMain(stair, stamina)
        except ISexception.InsufficientStaminaException:
            thrown = True
        self.assertFalse(thrown)
        self.assertEqual(finstam, 4)

    def test_08(self):
        thrown = False
        stamina = 12
        stair = [0, 100, 0, 0, 0, 999, 0, 0, 0, 0, 0, 999, 0, 0, 5, 5]
        try:
            finstam = wreckBeach.wreckMain(stair, stamina)
        except ISexception.InsufficientStaminaException:
            thrown = True
        self.assertFalse(thrown)
        self.assertEqual(finstam, 7)

    def test_09(self):
        thrown = False
        stamina = 12
        stair = [0, 100, 0, 0, 0, 999, 0, 0, 0, 0, 0, 999, 0, 0, 5, 5, 7, 7, 7]
        try:
            finstam = wreckBeach.wreckMain(stair, stamina)
        except ISexception.InsufficientStaminaException:
            thrown = True
        self.assertTrue(thrown)

    def test_10(self):
        thrown = False
        stamina = 12
        stair = [0, 1, 2, 3, 0, 1, 2, 3, 0, 1]
        try:
            finstam = wreckBeach.wreckMain(stair, stamina)
        except ISexception.InsufficientStaminaException:
            thrown = True
        self.assertFalse(thrown)
        self.assertEqual(finstam, 5)

    def test_11(self):
        thrown = False
        stamina = 12
        stair = [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2]
        try:
            finstam = wreckBeach.wreckMain(stair, stamina)
        except ISexception.InsufficientStaminaException:
            thrown = True
        self.assertTrue(thrown)

    def test_12(self):
        thrown = False
        stamina = 12
        stair = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        try:
            finstam = wreckBeach.wreckMain(stair, stamina)
        except ISexception.InsufficientStaminaException:
            thrown = True
        self.assertFalse(thrown)
        self.assertEqual(finstam, 1)

    def test_13(self):
        thrown = False
        stamina = 12
        stair = [1, 1, 1, 1, 1, 50, 1, 1, 1, 1, 1]
        try:
            finstam = wreckBeach.wreckMain(stair, stamina)
        except ISexception.InsufficientStaminaException:
            thrown = True
        self.assertFalse(thrown)
        self.assertEqual(finstam, 1)



if __name__ == '__main__':
    unittest.main()


