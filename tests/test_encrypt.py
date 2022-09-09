from .testing_utils import *
from ..Enc.AEH import AE as ae
from unittest import TestCase


class TestEncrypt(TestCase):

    def setUp(self) -> None:
        self.test_cases = [
                    ('Lorem here and lorem there lorem lorem everywhere ' * 9,"my_password_123"),
                    ("123567", 'lt77ma@345'),
                    ('123456789','123456789'),
                    ('aaaa' * 100,"my_pass_is_my_pass@123")
        ]

    def test_Encrypt(self):
        for txt, key in self.test_cases:
            encrypted = ae.Encrypt(txt,key)
            self.assertNotEqual(encrypted, txt)

    def test_Decrypt(self):
        for txt, key in self.test_cases:
            encrypted = ae.Encrypt(txt,key)
            decrypted = ae.Decrypt(encrypted,key)
            self.assertEqual(decrypted, txt)



        