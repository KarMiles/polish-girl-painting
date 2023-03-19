"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import unittest

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from blog.forms import PostForm


class TestPostForm(unittest.TestCase):
    '''
    This class is for testing Post form
    '''
    # TESTS SETUP

    @classmethod
    def setUpClass(cls):
        '''
        Set up test data used
        for all tests in TestViews class
        '''
        print('\nBlog test_forms starting')

    @classmethod
    def tearDownClass(cls):
        '''
        Delete test data used
        for all tests in TestViews class
        '''
        print('\ncomplete')

    # TESTS

    def test_post_title_is_required(self):
        '''
        Tests if the field 'title' is required.
        Checks:
        1. form is not valid if title is blank
        2. there is an error message when field is empty
        3. default comment shows

        '''
        form = PostForm({
            'title': '',
            'slug': 'ttitle',
            'author': 'tauthor',
            'content': 'tcontent',
            'highlight': False,
            'live': True,
        })

        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_post_content_is_required_filled(self):
        '''
        Tests if form with field 'title' containing characters
        is valid.
        Checks:
        1. form is valid if title contains characters
        '''
        form = PostForm({
            'title': 'Ttitle',
            'content': '',
            'highlight': 'thighlight',
            'live': True,
            'featured_image': 'test.jpg',
        })

        self.assertFalse(form.is_valid())

    def test_featured_image_is_not_required(self):
        '''
        Tests that field 'featured_image' is not required.
        Checks:
        1. form is valid if 'featured_image' field is left blank
        '''
        form = PostForm({
            'title': 'Ttitle',
            'slug': 'ttitle',
            'author': 'tauthor',
            'content': 'tcontent',
            'featured_image': '',
        })

        self.assertTrue(form.is_valid())

    def test_postform_fields_are_explicit_in_form_metaclass(self):
        """
        Tests that only fields in Meta class desplay in form.
        Checks:
        1. Fields listed in Meta class
        """
        form = PostForm()

        self.assertEqual(form.Meta.fields, (
            'title',
            'content',
            'highlight',
            'live',
            'featured_image'
        ))
