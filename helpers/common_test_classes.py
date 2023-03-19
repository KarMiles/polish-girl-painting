"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.test import Client
from django.contrib.auth import get_user_model

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestCommon():
    # USER SETUP
    User = get_user_model()
    client = Client()

    username_customer = 'test_user_customer'
    username_staff = 'test_user_staff'
    password = '1qazcde3'

    # TEST SETUP

    def setUp(self):
        '''
        Create test data
        '''
        # Create test user
        self.user = User(
            username='TestUser',
            email='test@mail.com',
            password='1qazcde3',
            is_staff='True',
        )

    def login_customer():
        '''
        Login test user (customer)
        '''
        client = Client()
        User = get_user_model()
        username_customer = 'test_user_customer'
        username_staff = 'test_user_staff'
        password = '1qazcde3'

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
