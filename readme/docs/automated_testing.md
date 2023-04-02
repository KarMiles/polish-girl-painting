# Automated testing

[Click here for Readme file](/README.md#user-story-testing)

All tests have been placed in folder **tests** in files:
- test_models.py
- test_views.py
- test_forms.py

Most of the testing were concentrated on e-commerce - related functionality. 
The following unit tests were run on models, views and forms:

<br>

___
## 1. Testing models

**test_create_post**

Tests that post can be created using Post model.
Checks:
1. test post is an instance of Post model.

**test_create_post_str_representation**

Tests string representation for Post model.
Checks:
1. string representation is equal to post title.

**test_post_save_method**

This tests the post str method
Checks:
1. post saves with correct slug

**test_post_highlight_defaults_to_false**

Tests that when no highlight status is chosen defaults to false

**test_post_live_defaults_to_true**

Tests that when no live status is chosen defaults to true

**test_create_order_str_representation**

Tests string representation for Order model
Checks:
1. string representation is equal to order number

**test_create_order**

Tests that order can be created using Order model
Checks:
1. test order in checkout is an instance of Order model

**test_create_product_str_representation**

Tests string representation for Product model
Checks:
1. string representation is equal to product title

**test_create_product**

Tests that product can be created using Product model
Checks:
1. test product is an instance of Product model

**test_create_category_str_representation**

Tests string representation for Category model
Checks:
1. string representation is equal to category name

**test_create_category**

Tests that category can be created using Category model
Checks:
1. test category is an instance of Category model

<br>

___
## 2. Testing views

**test_user_can_login**

Tests that user can login.
Checks:
1. that the client session is in allauth registry.

**test_get_homepage**

Test to check that Home page displays.
Checks:
1. status code is 200 (success)
and correct template is used.

**test_get_post_detail_page**

Test to check that Post Details page displays.
Checks:
1. status code is 200 (success)
and correct template is used.

**test_get_post_edit_page_staff**

Test to check that Edit Post page displays
for authorized user.
Checks:
1. status code is 200 (success)
and correct template is used
for authorized user.

**test_get_post_edit_page_customer**

Test to check that Edit Post page displays
for authorized user.
Checks:
1. status code is 200 (success) and correct template is used for authorized user.

**test_login_page**

Test to check that Login page displays.
Checks:
1. status code is 200 (success)
2. correct template is used.

**test_contact_page**

Test to check that Contact page displays.
Checks:
1. status code is 200 (success).
2. correct template is used.

**test_add_blog_post_page**

Test to check that blog page displays correctly.
Checks:
1. status code is 200 (success) in case of authorized user
2. correct template is used
for authorized user.
3. status code is not 200 in case of customer
4.  status code is not 200 in case of non-logged in user

**test_get_bagpage**

Test to check that bag page displays.
Checks:
1. status code is 200 (success)
2. correct template is used.

**test_add_to_empty_bag**

This test adds a product to an empty bag
Checks:
1. item with correct item id is added to bag
2. correct message is displayed after item is added to bag

**test_adjust_bag_quantity_to_two**

This test reduces the bag from 1 item to 2 items
Checks:
1. correct item is adjusted

**test_adjust_bag_quantity_message**

This verifies redirect after item quantity is adjusted in bag
Checks:
1. correct redirect applied
2. confirmation message 

**test_remove_product_from_bag**

This test removes a product from the bag
Checks:
1. correct item removed
2. remove successful
3. confirmation message 

<br>

___
## 3. Testing forms

**test_post_title_is_required**

Tests if the field 'title' is required.
Checks:
1. form is not valid if title is blank.
2. there is an error message when field is empty.
3. default comment shows.

**test_post_content_is_required**

Tests if form with field 'title' containing characters 
is valid.
Checks:
1. form is valid if title contains characters.

**test_featured_image_is_not_required**

Tests that field 'featured_image' is not required.
Checks:
1. form is valid if 'featured_image' field is left blank

**test_excerpt_is_not_required**

Tests that field 'excerpt' is not required.
Checks:
1. form is valid if 'excerpt' field is left blank.

**test_postform_fields_are_explicit_in_form_metaclass**

Tests that only fields in Meta class display in form.
Checks:
1. Fields listed in Meta class.

**test_add_order_form_is_valid**

This test tests the order form object

**test_product_form_is_valid**

Tests the product form object
Checks:
1. product form is valid

**test_product_title_is_required**

Tests if the field 'title' is required.
Checks:
1. form is not valid if title is blank
2. there is an error message when field is empty
3. default message shows

**test_product_description_is_required**

Tests if the field 'description' is required.
Checks:
1. form is not valid if title is blank
2. there is an error message when field is empty
3. default message shows

<br>

___

Automated tests results screenshot:

![Automated testing results](/readme/docs/images/testing/auto_tests_results.jpg)