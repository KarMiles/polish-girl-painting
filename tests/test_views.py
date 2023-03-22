"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import unittest
import tempfile
from django.test import Client
from django.contrib.messages import get_messages
from django.contrib.auth import get_user_model
from django.urls import reverse

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from blog.models import Post
from blog.views import PostList
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


class TestViews(unittest.TestCase):
    '''
    Test view to show blog page
    '''

    # --- Tests setup ---

    @classmethod
    def setUpClass(cls):
        '''
        Set up test data used
        for all tests in TestViews class
        '''
        print('\nBlog test_views starting')
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

        # Create test Post
        if not Post.objects.filter(title='Ttitle').exists():
            Post.objects.create(
                title='Ttitle',
                slug='ttitle',
                author=user_staff,
                content='tcontent',
                live=True,
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
        Post.objects.filter(slug='ttitle').delete()
        print('\ncomplete')

    def assertTemplateUsed(self, response, template_name):
        """
        Asserts that the template with the given name
        was used in rendering the response.
        Function for use in further tests.
        Checks:
        1. indicated template is used
        """
        self.assertIn(
            template_name,
            [t.name for t in response.templates if t.name is not None]
        )

    # --- Tests ---

    def test_user_can_login(self):
        """
        Tests that user can login.
        Checks:
        1. that the client session is in allauth registry.
        """
        login_customer()
        self.assertIn('_auth_user_id', client.session)
        logout()

    # TEST LOADING PAGES

    def test_get_homepage(self):
        '''
        Test to check that Home page displays.
        Checks:
        1. status code is 200 (success)
        and correct template is used.
        '''
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')

    def test_get_post_detail_page(self):
        '''
        Test to check that Post Details page displays.
        Checks:
        1. status code is 200 (success)
        and correct template is used
        '''
        post_detail_url = reverse('post_detail', args=['ttitle'])
        response = client.get(post_detail_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            'blog/post_detail.html')

    def test_get_post_edit_page_staff(self):
        '''
        Test to check that Edit Post page displays
        for authorized user.
        Checks:
        1. status code is 200 (success)
        and correct template is used
        for authorized user.
        '''
        login_staff()
        post_detail_url = reverse('post_edit', args=['ttitle'])
        response = client.get(post_detail_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            'blog/post_edit.html')

    def test_get_post_edit_page_customer(self):
        '''
        Test to check that Edit Post page displays
        for authorized user.
        Checks:
        1. status code is 200 (success)
        and correct template is used
        for authorized user.
        '''
        login_customer()
        post_detail_url = reverse('post_edit', args=['ttitle'])
        response = client.get(post_detail_url)

        self.assertNotEqual(response.status_code, 200)

    def test_login_page(self):
        '''
        Test to check that Login page displays.
        Checks:
        1. status code is 200 (success)
        2. correct template is used.
        '''
        logout()
        response = client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            'account/login.html')

    def test_contact_page(self):
        '''
        Test to check that Contact page displays.
        Checks:
        1. status code is 200 (success)
        2. correct template is used.
        '''
        response = client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            'django_contact_form/contact_form.html')

    def test_add_blog_post_page(self):
        '''
        Test to check that blog page displays correctly.
        Checks:
        1. status code is 200 (success) in case of authorized user
        2. correct template is used
        for authorized user.
        3. status code is not 200 in case of customer
        4.  status code is not 200 in case of non-logged in user
        '''
        # Blog page loads for staff user
        login_staff()
        response = client.get('/blog/post')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            'blog/post_add.html')
        logout()

        # Blog page does not load for customer user
        logout()
        login_customer()
        response = client.get('/blog/post')
        self.assertNotEqual(response.status_code, 200)
        logout()

        # Blog page does not load for non-logged in user
        logout()
        response = client.get('/blog/post')
        self.assertNotEqual(response.status_code, 200)
        logout()


class TestBagViews(unittest.TestCase):
    '''
    Test view to show bag page
    '''

    # TESTS SETUP

    @classmethod
    def setUpClass(cls):
        '''
        Set up test data used
        for all tests in TestBagViews class
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
                is_unique=False,
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

    # --- Tests ---

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
        item_id = str(product.id)
        response = client.post(
            f'/bag/add/{product.id}/',
            {"quantity": 1, 'item_id': item_id, "redirect_url": "view_bag"})
        bag = client.session['bag']

        self.assertEqual(list(bag.keys())[0], item_id)

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Added "Ttitle" to your bag')

    def test_adjust_bag_quantity_to_two(self):
        """
        This test reduces the bag from 1 item to 2 items
        Checks:
        1. correct item is adjusted
        """
        product = Product.objects.get(title='Ttitle')
        item_id = str(product.id)
        bag = client.session['bag']

        # Check that correct item is adjusted in bag
        response = client.post(
            f'/bag/adjust/{product.id}/',
            {
                "quantity": 2,
                'item_id': item_id,
                "redirect_url": "adjust_bag"
                })

        self.assertEqual(list(bag.keys())[0], item_id)

    def test_adjust_bag_quantity_message(self):
        """
        This verifies redirect after item quantity is adjusted in bag
        Checks:
        1. correct redirect applied
        2. confirmation message 
        """
        product = Product.objects.get(title='Ttitle')
        item_id = str(product.id)
        bag = client.session['bag']

        # Check correct redirect after item adjusted
        response = client.post(
            f'/bag/adjust/{product.id}/', 
            {
                'quantity': 1,
                'item_id': item_id,
                'redirect_url': "view_bag",
                },
            follow=True)
        last_url, status_code = response.redirect_chain[-1]
        self.assertEqual(last_url, '/bag/')

        # Check correct confirmation message produced
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[1]), 'Updated "Ttitle" quantity to 1')

    def test_remove_product_from_bag(self):
        """
        This test removes a product from the bag
        Checks:
        1. correct item removed
        2. remove successful
        3. confirmation message 
        """
        product = Product.objects.get(title='Ttitle')
        item_id = str(product.id)
        bag = client.session['bag']
        response = client.post(
            f'/bag/remove/{product.id}/',
            {
                "quantity": 1,
                'item_id': item_id,
                "redirect_url": "view_bag"})
        self.assertEqual(list(bag.keys())[0], item_id)

        response = client.post(f'/bag/remove/{product.id}/')
        bag = client.session['bag']
        self.assertEqual(bag, {})

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Removed "Ttitle" from your bag')


if __name__ == '__main__':
    unittest.main()
