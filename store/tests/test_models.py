from django.test import TestCase
from django.contrib.auth.models import User

from store.models import Category, Product


class TestCategoriesModel(TestCase):

    def setUp(self):
        User.objects.create(username='admin')
        self.data1 = Category.objects.create(name='django1', slug='django1')
        self.data2 = Product.objects.create(category_id=1, name='django beginners', created_by_id=1,
                                            slug='django-beginners', price=10990, image='django', desc='blablabla')

    def test_category_model_entry(self):
        """
        Test Category model data insertion/type/fields attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_category_model_name(self):
        """
        Test Category model default name
        """
        data = self.data1
        self.assertEqual(str(data), 'django1')

    def test_product_model_name(self):
        """
        Test Product model default name
        """
        data = self.data2
        self.assertEqual(str(data), 'django beginners')
