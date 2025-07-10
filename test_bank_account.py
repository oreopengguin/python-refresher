import unittest
from bank_account import BankAccount


class TestBankAccount(unittest.TestCase):
    def test_withdraw(self):
        self.EricAcnt = BankAccount(100.00, "Eric", 1)
        self.EricAcnt.withdraw(10.00)
        self.assertAlmostEqual(self.EricAcnt.balance, 90)
        self.assertNotAlmostEqual(self.EricAcnt.balance, 32)
        self.EricAcnt.withdraw(40)
        self.assertAlmostEqual(self.EricAcnt.balance, 50)
        self.assertNotAlmostEqual(self.EricAcnt.balance, 49)
        self.assertEqual(self.EricAcnt.withdraw(-100000.00), False)
        self.assertAlmostEqual(self.EricAcnt.balance, 50)
        self.assertEqual(self.EricAcnt.withdraw("meow"), False)
        self.assertAlmostEqual(self.EricAcnt.balance, 50)

        """
        with self.assertRaises(TypeError):
            self.EricAcnt.withdraw(-1000000.00)
        with self.assertRaises(TypeError):
            self.EricAcnt.withdraw("meow")
        """
    
    def test_deposit(self):
        self.IsaAcnt = BankAccount(2.73, "Isa", 2)
        self.IsaAcnt.deposit(2.49)
        self.assertAlmostEqual(self.IsaAcnt.balance, 5.22)
        self.assertNotAlmostEqual(self.IsaAcnt.balance, 5.23)
        self.IsaAcnt.deposit(3)
        self.assertAlmostEqual(self.IsaAcnt.balance, 8.22)
        self.assertNotAlmostEqual(self.IsaAcnt.balance, 8.21)
        self.assertEqual(self.IsaAcnt.deposit(-1000), False)
        self.assertAlmostEqual(self.IsaAcnt.balance, 8.22)
        self.assertEqual(self.IsaAcnt.deposit("meow"), False)
        self.assertAlmostEqual(self.IsaAcnt.balance, 8.22)
        # with self.assertRaises(TypeError):
        #     self.IsaAcnt.deposit(-1000)
        # with self.assertRaises(TypeError):
        #     self.IsaAcnt.deposit("meow")
    
    def test_display(self):
        self.EricAcnt = BankAccount(-940, "Eric", 1)
        self.IsaAcnt = BankAccount(8.22, "Isa", 2)
        self.assertEqual(self.EricAcnt.display(), "Eric's account has a balance of $-940")
        self.assertEqual(self.IsaAcnt.display(), "Isa's account has a balance of $8.22")
        self.assertNotEqual(self.EricAcnt.display(), "meow meow meow")
        self.assertNotEqual(self.IsaAcnt.display(), "meow meow meow")