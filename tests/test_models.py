"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import unittest
from django.contrib.auth import get_user_model

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from blog.models import Post

User = get_user_model()


class TestBlogModels(unittest.TestCase):
    '''
    Test Post model
    '''

    # TESTS SETUP

    @classmethod
    def setUpClass(cls):
        '''
        Class method used for operations carried
        before all tests
        '''
        print('\nTest_models starting')

    @classmethod
    def tearDownClass(cls):
        '''
        Class method used for operations carried
        after all tests
        '''
        print('\nTest_models complete')

    def setUp(self):
        '''
        Create test data
        '''
        # Create test user
        self.user = User(
            username='TestUser',
            email='test@mail.com',
            password='1qaz3edc',
            is_staff='True'
        )

        # Create test post
        self.post = Post(
            title='Test Title',
            slug='test-title',
            author=self.user,
            content='tcontent',
        )


    # TESTS

    # blog

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
        self.assertEquals(str(self.post), 'Test Title')

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
