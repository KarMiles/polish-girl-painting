"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import unittest
from django.test import Client
from django.contrib.auth import get_user_model
from django.urls import reverse

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from blog.models import Post
from blog.views import PostList


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

    # TESTS SETUP

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
        Test to check that Booking page displays correctly.
        Checks:
        1. status code is 200 (success) in case of authorized user
        2. correct template is used
        for authorized user.
        3. status code is not 200 in case of non-authorized user
        '''
        # Booking page loads for staff user
        login_staff()
        response = client.get('/blog/post')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            'blog/post_add.html')
        logout()

        # Booking page does not load for unauthorized user
        logout()
        response = client.get('/blog/post')
        self.assertNotEqual(response.status_code, 200)
        logout()


if __name__ == '__main__':
    unittest.main()
