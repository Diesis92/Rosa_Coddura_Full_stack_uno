# shop/tests.py

# from django.test import TestCase
# from .models import Prodotto

# class ProdottoTestCase(TestCase):

#     def setUp(self):
#         Prodotto.objects.create(nome="Mouse", prezzo=29.99)

#     def test_disponibile(self):
#         mouse = Prodotto.objects.get(nome="Mouse")
#         self.assertTrue(mouse.disponibile)


from django.test import TestCase
from .models import Prodotto

class ProdottoTestCase(TestCase):

    def setUp(self):
        Prodotto.objects.create(nome="Mouse", prezzo=29.99)

    def test_sconto(self):
        p = Prodotto.objects.create(nome="Mouse", prezzo=100)
        self.assertEqual(p.prezzo_scontato(), 80)
