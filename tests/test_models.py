"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import unittest
from django.contrib.auth import get_user_model

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from blog.models import Post
from checkout.models import Order
from products.models import Product, Category

User = get_user_model()


class TestPostModels(unittest.TestCase):
    '''
    Test Post model
    '''

    # --- Tests setup ---

    @classmethod
    def setUpClass(cls):
        '''
        Class method used for operations carried
        before all tests
        '''
        print('\nBlog test_models starting')

    @classmethod
    def tearDownClass(cls):
        '''
        Class method used for operations carried
        after all tests
        '''
        print('\ncomplete')

    def setUp(self):
        '''
        Create test data
        '''
        # Create test user
        self.user = User(
            username='TestUser',
            email='test@mail.com',
            password='1qazcde3',
            is_staff='True'
        )

        # Create test post
        self.post = Post(
            title='Ttitle',
            slug='ttitle',
            author=self.user,
            content='tcontent',
        )


    # --- Tests ---

    def test_create_post(self):
        '''
        Tests that post can be created using Post model
        Checks:
        1. test post is an instance of Post model
        '''
        self.assertIsInstance(self.post, Post)

    def test_create_post_str_representation(self):
        '''
        Tests string representation for Post model
        Checks:
        1. string representation is equal to post title
        '''
        self.assertEquals(str(self.post), 'Ttitle')

    def test_post_highlight_defaults_to_false(self):
        '''
        Tests that when no highlight status is chosen defaults to false
        '''
        self.assertEqual(self.post.highlight, False)

    def test_post_live_defaults_to_true(self):
        '''
        Tests that when no live status is chosen defaults to true
        '''
        self.assertEqual(self.post.live, True)


class TestCheckoutModels(unittest.TestCase):
    """
    A class for testing checkout models
    """

    # --- Tests setup ---
    
    @classmethod
    def setUpClass(cls):
        '''
        Class method used for operations carried
        before all tests
        '''
        print('\nCheckout test_models starting')

    @classmethod
    def tearDownClass(cls):
        '''
        Class method used for operations carried
        after all tests
        '''
        print('\ncomplete')

    def setUp(self):
        """
        Create a test product and order
        """
        Order.objects.create(
            full_name='Test Name',
            email='user@test.com',
            phone_number='123456789',
            street_address1='Test Street',
            town_or_city='Test City',
            country='GB',
        )

    def tearDown(self):
        """
        Delete test products and orders
        """
        # Order.objects.all().delete()
        Order.objects.filter(full_name='Test Name').delete()

    # --- Tests ---

    def test_create_order_str_representation(self):
        '''
        Tests string representation for Order model
        Checks:
        1. string representation is equal to order number
        '''
        order = Order.objects.get(email='user@test.com')
        self.assertEqual(str(order), order.order_number)

    def test_create_order(self):
        '''
        Tests that order can be created using Order model
        Checks:
        1. test order in checkout is an instance of Order model
        '''
        order = Order.objects.get(email='user@test.com')
        self.assertIsInstance(order, Order)


class TestProductModels(unittest.TestCase):
    """
    A class for testing product models
    """

    # --- Tests setup ---
    
    @classmethod
    def setUpClass(cls):
        '''
        Class method used for operations carried
        before all tests
        '''
        print('\nProduct test_models starting')

    @classmethod
    def tearDownClass(cls):
        '''
        Class method used for operations carried
        after all tests
        '''
        print('\ncomplete')

    def setUp(self):
        """
        Create a test product and category
        """
        product = Product.objects.create(
            title='Test Title',
            excerpt="Test excerpt",
            description="Test description",
            price=100,
        )

        category = Category.objects.create(
            name='test-category',
            friendly_name='Test Category',
        )

    def tearDown(self):
        """
        Delete test products, categories and orders
        """
        Product.objects.filter(title='Test Title').delete()
        Category.objects.filter(name='test-category').delete()
        Order.objects.filter(full_name='Test Name').delete()

    # --- Tests ---

    def test_create_product_str_representation(self):
        '''
        Tests string representation for Product model
        Checks:
        1. string representation is equal to product title
        '''
        product = Product.objects.get(title='Test Title')
        self.assertEqual(str(product), product.title)

    def test_create_product(self):
        '''
        Tests that product can be created using Product model
        Checks:
        1. test product is an instance of Product model
        '''
        product = Product.objects.get(title='Test Title')
        self.assertIsInstance(product, Product)

    def test_create_category_str_representation(self):
        '''
        Tests string representation for Category model
        Checks:
        1. string representation is equal to category name
        '''
        category = Category.objects.get(name='test-category')
        self.assertEqual(str(category), category.name)

    def test_create_category(self):
        '''
        Tests that category can be created using Category model
        Checks:
        1. test category is an instance of Category model
        '''
        category = Category.objects.get(name='test-category')
        self.assertIsInstance(category, Category)


if __name__ == '__main__':
    unittest.main()