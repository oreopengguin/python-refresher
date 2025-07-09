import unittest
from bank_account import BankAccount


class TestBankAccount(unittest.TestCase):
    def test_withdraw(self):
        self.EricAcnt = BankAccount(100.00, "Eric", 1)
        self.EricAcnt.withdraw(1000.00)
        self.assertAlmostEqual(self.EricAcnt.balance, -900)
        self.EricAcnt.withdraw(40)
        self.assertAlmostEqual(self.EricAcnt.balance, -940)
        with self.assertRaises(TypeError):
            self.EricAcnt.withdraw(-1000000.00)
        with self.assertRaises(TypeError):
            self.EricAcnt.withdraw("meow")
    
    def test_deposit(self):
        self.IsaAcnt = BankAccount(2.73, "Isa", 2)
        self.IsaAcnt.deposit(2.49)
        self.assertAlmostEqual(self.IsaAcnt.balance, 5.22)
        self.IsaAcnt.deposit(3)
        self.assertAlmostEqual(self.IsaAcnt.balance, 8.22)
        with self.assertRaises(TypeError):
            self.IsaAcnt.deposit(-1000)
        with self.assertRaises(TypeError):
            self.IsaAcnt.deposit("meow")
    
    def test_display(self):
        self.EricAcnt = BankAccount(-940, "Eric", 1)
        self.IsaAcnt = BankAccount(8.22, "Isa", 2)
        self.assertEqual(self.EricAcnt.display(), "Eric's account has a balance of $-940")
        self.assertEqual(self.IsaAcnt.display(), "Isa's account has a balance of $8.22")
        