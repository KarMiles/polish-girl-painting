"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import unittest
import tempfile
from django.test import Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.contrib.messages import get_messages

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from products.models import Product


# --- SETUP ---

# USER SETUP
User = get_user_model()
client = Client()

username_customer = 'test_user_customer'
username_staff = 'test_user_staff'
password = '1qazcde3'


def login_customer():
    '''
    Login test user (customer)
    '''
    client.force_login(
        User.objects.get_or_create(
            username=username_customer,
            password=password,
            is_staff='False'
            )[0])


def login_staff():
    '''
    Login test user (staff)
    '''
    client.force_login(
        User.objects.get_or_create(
            username=username_staff,
            password=password,
            is_staff='True'
            )[0])


def logout():
    '''
    Logout test user
    '''
    client.logout()


class TestBagViews(unittest.TestCase):
    '''
    Test view to show bag page
    '''

    # TESTS SETUP

    @classmethod
    def setUpClass(cls):
        '''
        Set up test data used
        for all tests in TestViews class
        '''
        print('\nBag test_views starting')
        # Create test user (customer)
        if not User.objects.filter(username=username_customer).exists():
            user_customer = User.objects.create(
                username=username_customer,
                password=password,
                is_staff='False'
            )
        else:
            user_customer = User.objects.filter(username=username_customer)[0]

        # Create test user (staff)
        if not User.objects.filter(username=username_staff).exists():
            user_staff = User.objects.create(
                username=username_staff,
                password=password,
                is_staff='True'
            )
        else:
            user_staff = User.objects.filter(username=username_staff)[0]

        # Create test product
        if not Product.objects.filter(title='Ttitle').exists():
            product = Product.objects.create(
                title='Ttitle',
                sku='test-sku',
                description='test-description',
                price=100,
                image=tempfile.NamedTemporaryFile(suffix=".jpg").name,
                available=True,
                live=False,
                )

    @classmethod
    def tearDownClass(cls):
        '''
        Delete test data used
        for all tests in TestViews class
        '''
        # Delete test data
        User.objects.filter(username=username_customer).delete()
        User.objects.filter(username=username_staff).delete()
        Product.objects.filter(title='Ttitle').delete()
        print('\ncomplete')

    # Function for checking if indicated template is used
    def assertTemplateUsed(self, response, template_name):
        """
        Asserts that the template with the given name
        was used in rendering the response.
        """
        self.assertIn(
            template_name,
            [t.name for t in response.templates if t.name is not None]
        )

    # --- TESTS ---

    # Test loading pages

    def test_get_bagpage(self):
        '''
        Test to check that bag page displays.
        Checks:
        1. status code is 200 (success)
        2. correct template is used.
        '''
        response = client.get('/bag/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')

    def test_add_to_empty_bag(self):
        """
        This test adds a product to an empty bag
        Checks:
        1. item with correct item id is added to bag
        2. correct message is displayed after item is added to bag
        """
        product = Product.objects.get(title='Ttitle')
        Product.objects.get(sku='test-sku')
        item_id = str(product.id)
        response = client.post(
            f'/bag/add/{product.id}/',
            {"quantity": 1, 'sku': 'test-sku', "redirect_url": "view_bag"})
        bag = client.session['bag']

        self.assertEqual(list(bag.keys())[0], item_id)

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Added "Ttitle" to your bag')




if __name__ == '__main__':
    unittest.main()
