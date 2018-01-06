import unittest
import cn_function
import hr_function

class TestCv(unittest.TestCase):

    # for HR:
    def test_editstatus(self):
        self.assertEqual(hr_function.editstatus("529285890", '0'), True)
        self.assertEqual(hr_function.editstatus("529285890", '2'), True)
        self.assertEqual(hr_function.editstatus("529285890", '3'), True)
        self.assertEqual(hr_function.editstatus("529285890", '1'), True)
        self.assertEqual(hr_function.editstatus("529285890", '0'), True)
        self.assertEqual(hr_function.editstatus("000000000", '1'), False)

    def test_printall(self):
        self.assertEqual(hr_function.printall(), True)

    def test_printid(self):
        self.assertEqual(hr_function.printid("529285890"), True)
        self.assertEqual(hr_function.printid("000000000"), False)

    def test_searchpro(self):
        self.assertEqual(hr_function.searchpro("id"), True)
        self.assertEqual(hr_function.searchpro("xxxxxxx"), False)
        self.assertEqual(hr_function.searchpro(" "), True)

    def test_editnotes(self):
        self.assertEqual(hr_function.editnotes("529285890", '0'), True)
        self.assertEqual(hr_function.editstatus("529285890", '2'), True)
        self.assertEqual(hr_function.editstatus("529285890", '0'), True)
        self.assertEqual(hr_function.editstatus("000000000", '1'), False)

    # for CV:
    def test_login(self):
        self.assertEqual(cn_function.login("cn529285890", "cn529285890"), True)
        self.assertEqual(cn_function.login("529285890", "cn529285890"), False)
        self.assertEqual(cn_function.login("000000000", "cn000000000"), False)

    def test_delete_cv(self):
        self.assertEqual(cn_function.delete_cv("529285890"), False)
        self.assertEqual(cn_function.delete_cv("00000000"), False)

    def test_change_mail(self):
        self.assertEqual(cn_function.change_mail("529285890", "new_mail"), True)
        self.assertEqual(cn_function.change_mail("529285890", "xxxxxx"), True)
        self.assertEqual(cn_function.change_mail("000000000", "-----"), False)

    def test_mobile(self):
        self.assertEqual(cn_function.change_mobile("529285890", "new_mobile"), True)
        self.assertEqual(cn_function.change_mobile("529285890", "xxxxxxxx"), True)
        self.assertEqual(cn_function.change_mobile("000000000", "-------"), False)

if __name__ == '__main__':
    unittest.main()