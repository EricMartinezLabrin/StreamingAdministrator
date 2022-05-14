from django.test import TestCase

class IndexTest(TestCase):

    def test_login_with_email_or_password_wrong(self):
        """
        When login with username or password wrong it show Tu Email o Contraseña son incorrectos, porfavor vuelve a intentarlo.
        """
