from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from store.models import Category, Product


class TestBasketView(TestCase):
    def setUp(self):
        User.objects.create(username='admin')
        Category.objects.create(name='django', slug='django')
        Product.objects.create(category_id=1, name='django beginners', created_by_id=1, slug='django-beginners',
                               price=9990, image='django', desc='blablabla1')
        Product.objects.create(category_id=1, name='django intermediate', created_by_id=1, slug='django-intermediate',
                               price=10990, image='django', desc='blablabla2')
        Product.objects.create(category_id=1, name='django pros', created_by_id=1, slug='django-pros',
                               price=12990, image='django', desc='blablabla3')
        self.client.post(
            reverse('basket:basket_add'), {"productid": 1, "productqty": 1, "action": "post"}, xhr=True
        )
        self.client.post(
            reverse('basket:basket_add'), {"productid": 2, "productqty": 2, "action": "post"}, xhr=True
        )
        

    def test_basket_url(self):
        """
        Test homepage response status
        """
        response = self.client.get(reverse('basket:basket_summary'))
        self.assertEqual(response.status_code, 200)

    def test_basket_add(self):
        """
        Test adding item to the basket
        """
        response = self.client.post(
            reverse('basket:basket_add'), {"productid": 3, "productqty": 1, "action": "post"}, xhr=True
        )
        self.assertEqual(response.json(), {'basket_qty': 4})
        response = self.client.post(
            reverse('basket:basket_add'), {"productid": 2, "productqty": 4, "action": "post"}, xhr=True
        )
        self.assertEqual(response.json(), {'basket_qty': 6})

    def test_basket_delete(self):
        """
        Test deleting item from the basket
        """
        response = self.client.post(
            reverse('basket:basket_delete'), {"productid": 2, "action": "post"}, xhr=True
        )
        self.assertEqual(response.json(), {'basket_qty': 1, 'subtotal': 9990})
        response = self.client.post(
            reverse('basket:basket_delete'), {"productid": 1, "action": "post"}, xhr=True
        )
        self.assertEqual(response.json(), {'basket_qty': 0, 'subtotal': 0})

    def test_basket_update(self):
        """
        Test updating item from the basket
        """
        response = self.client.post(
            reverse('basket:basket_update'), {"productid": 1, "productqty": 3, "action": "post"}, xhr=True
        )
        self.assertEqual(response.json(), {'basket_qty': 5, 'subtotal': 51950})
        response = self.client.post(
            reverse('basket:basket_update'), {"productid": 2, "productqty": 1, "action": "post"}, xhr=True
        )
        self.assertEqual(response.json(), {'basket_qty': 4, 'subtotal': 40960})
    