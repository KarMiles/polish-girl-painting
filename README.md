# PolishGirlPainting

![screenshot of Responsive Image](readme/docs/images/am_i_responsive.jpg)

View the live site [here](https://heroku-pgp-project.herokuapp.com/).

Users for testing:

- customer (role: customer)
- staff_user (role: staff)
- admin (owner)

Users passwords are supplied in assessment submission  form.

<br>

# Table of Contents <a name='home'></a>

1. [User Experience (UX)](#ux)<br>
    i.  [User Stories](#user-stories)<br>
    ii. [Scope](#scope)<br>
    iii. [Structure](#Structure)<br>
    iv. [Skeleton and technical design](#skeleton)<br>
    v. [Surface](#surface)<br>
      
2. [Features](#features)<br>
    i. [Current Features](#features-current)<br>
    ii. [Potential features](#features-next)<br>

3. [Marketing Strategy](#marketing-strategy)<br>

4. [Testing](#testing)<br>
    i. [User Story / feature testing](#user-story-testing)<br>
    ii.  [Automated testing](#automated-testing)<br>
    iii.  [Known issues during development and testing](#known-issues)<br>
    iv. [Validation testing](#validation-testing)<br>

5. [Deployment](#deployment)<br>

6. [Technologies Used](#technology-used)<br>
    i. [Agile Methodology](#agile-methodology)<br>
    ii. [Languages](#languages)<br>
    iii. [Frameworks and Libraries](#frameworks-and-libraries)<br>

7. [Credits](#credits)<br>

8. [Acknowledgements](#acknowledgements)<br>


## Introduction
**The project concept**

PolishGirlPainting is the webpage for an artist Monika Curto Fuentes showcasing her work on the web and selling her paintings online. 
Apart from allowing the Owner present her art for sale, the webpage also helps in developing her clientbase by building a community of people interested in her art.

This is an educational project with a possibility of moving the project into the real world application.

___

# 1. User Experience (UX) <a name='ux'></a> 
### **Project goals**
The main goal of the project is to provide a platform for selling the Artist's paintings and supporting this goal by engaging prospective and current clients interested in acquiring the paintings. This should be achieved through several sub-goals:
-	To enable owner (Artist) to post, edit, read and delete textual and graphical content directly related to her offering.
-	To enable the owner to post in her personal blog.
-	To provide functionality for commercial transactions related to the items for sale.
-	To enable users to view pictures and details on specific art pieces.
-	To enable all users to view the Artist's blog.
-   To enable registered users to share their testimony about their interactions with the Artist or experiences with her art.
-	To enable all visitors to subscribe to email newsletter.
-	To enable all users to contact the Artist using a form in the Contact section.


### **Site owner goals**
-	To ensure the offering is broadcast in a consumer-friendly and appealing way.
-	To have commercial transactions processed in accurate and time-efficient manner.
-	To increase prospective and current customers' interest in the offering.
-	To maximise customers' retainment.
-	To promote knowledge on benefits of art appreciation.
-	To receive requests for custom art creation.
-	To enable customer - Artist correspondence.
-	To build customer database.
-	To assure access to the website on different kinds of devices.


### **User goals**
All users
-	To be able to use service intuitively and with ease.
-	To be able to view content without sharing any details.
-	To view the Artist's collection and find details on each item.
-	To be able to enter contact details and carry out a complete purchase transaction.
-	To be able to contact the Artist.
-   To share their experience in a Testimony.
-	To open and then access account for easier future transactions.
-	To have an aesthetically pleasing and functionally easy experience while using the webpage.


Registered users
-	To log in and log out as needed.
-	To log in with a chosen user name to maintain privacy.
-	To have user details remembered for smooth future transactions.

To achieving the project goals lead addressing the User Stories grouped in Epics (1.i [User Stories]((#user-stories))) which went through the sieve of strategic Scope analysis (1.ii [Scope]((#scope))) in conjunction with implementation of the Marketing Strategy (3 [Marketing Strategy](#marketing-strategy)).

---

## 1.i. User Stories <a name='user-stories'></a>

### **1. Epic: Account management**

1.1 As a **site user** I can **access site without logging in** so that I can **view content of the webpage**.

1.2 As a **site user** I can **register** so that **I can reuse once entered information**.

1.3 As a **site user** I can **log in using my username and password** so that I can **reuse once entered personal information**.

1.4 As a **site user** I can **log out of my account** so that I know **my information stays confidential**.

1.5 As a **site user** I can **easily see my current login status** so that **I can control my status for privacy protection**.

1.6 As a **site user** I receive **confirmation of logging in and logging out visible on webpage** so that I **instantly know if the operation was successful**.

1.7 As a **site user** I can **reset my password** so that I can **safely remain the website's registered user**.

1.8 As a **site user** I can **read webpage's privacy policy** so that I can **know if my personal information is safe**.


### **2. Epic: Navigation**

2.1 As a **site user** I can **navigate the service intuitively** so that I can **utilize all of its content**.

2.2 As a **site user** I can easily **browse through available items** so I can **decide which ones are most appropriate to me**.

2.3 As a **site user** I can **navigate the site on all kinds of screens** so that **I am not limited to any kind of device**.

2.4 As a **site user** I can **find links to Artist's social media wherever I am on the webpage** so that **I can use alternative means of getting the content**.

2.5 As a **site user** I can **easily go back to home page** so I can **restart my experience**.


### **3. Epic: Customer engagement**

3.1 As a **site user** I can **locate convenient routes of communication with owner, including company's social media accounts** so I can **stay in contact through alternative means**.


3.2 As a **site user** I can **subscribe to a newsletter** so I can **stay engaged and stay up do date with the Artist's offering and creative process**.

3.3 As a **registered site user** I can **use website without having to re-enter my details** so that **my activity on the site requires minimum afford from my side**.

3.4 As a **site user** I can **see immediately information about newest content** so I can **go directly to that content should I wish to do so**.

3.5 As a **site user** I can **change the language of the site by an automatic translator** so that I can **read the content in a different language**.

3.6 As a **site user** I can **share my experiences in Testimony** so that **I feel that I contribute to the community gathered around the Artist**.

3.7 As a **site owner** I can **present a basic personal introduction** so that **I know potential and current customers have a chance to build a personal connection with me as an artist**.


### **4. Epic: Offer**

4.1 As a **site user** I can **quickly get a general idea about items on offer** so that I can **decide which content to get acquainted with more thoroughly**.

4.2 As a **site user** I can **read details about a chosen item** so that I can **make the best decision about the purchase based on technical information (e.g. size) and my personal preferences**.

4.3 As a **site owner** I can **create, update and delete item entries** so that I can **inform visitors on pieces on offer and pieces sold**.

4.4 As a **site owner** I can **prioritize which items are shown first on the site** so that I can **influence demand on offering of my choice**.


### **5. Epic: Blog**

5.1 As a **site user** I can **read Artist's blog** so that I can **stay up to date with the Artist's developments**.

5.2 As a **site owner** I can **create, update and delete blog entries** so that I can **share content of my choice and build a sense of connection with my audience and prospective buyers**.

5.3 As a **site owner** I can **hide and unhide blog** so that I can **control visibility of the entire blog section of the site at any time**.


### **6. Epic: Checkout**

7.1 As a **site user** I can **smoothly go through purchase process** so that I can **acquire a chosen item**.

7.2 As a **site owner** I can **monitor transaction's status** so I can **ensure process of purchase and delivery is successfully completed**.

7.3 As a **site user** I can **receive a confirmation email after a transaction** so I can **be assured about the status of my order**.

### **7. Epic: Admin site**

8.1 As a **site admin** I can **create, update and delete user profiles in admin page** so that **all users have appropriate access to website functionality**.

8.2 As a **site admin** I can **create, update and delete items in admin page** so I can assure that **only content in line with my ethos and up to date is available on the website**.

8.3 As a **site admin** I can **create, update and delete blog entries** so that **blog entries as means of communication and user engagement are used according to their purpose**.


[Table of Contents](#home)

---

## 1.ii. Scope <a name='scope'></a>

### Strategy trade-offs

Features were evaluated on a scale from 1 to 5 in terms of importance (how important a feature is for the project in current release) and viability (how feasible the implementation of the feature is in current release).

Features with high and medium score between 8 and 25 points on scale 1-25 have been included in production. Features with lower score were left outside the scope of this project.

<details>
<summary>Click here for strategy trade-offs</summary>

![screenshot of strategy trade-offs](readme/docs/images/strategy_tradeoffs.jpg)
</details>

<br>

[Table of Contents](#home)

---

## 1.iii. Structure <a name='structure'></a>

## Website templates

Templates are structured in folders named templates. Base template is used for the entire site for consistency and ease in user experience.
Templates common for entire site, including base, allauth, error pages and includes are placed in the folder templates in the main directory. App-specific templates are placed in folders called templates within the appropriate apps. 

<details>
<summary>Click here to view table with templates, part 1</summary>

![screenshot of folder with templates](readme/docs/images/templates-screenshots/website_templates1.jpg)

</details>

<details>
<summary>Click here to view table with templates, part 2</summary>

![screenshot of folder with templates](readme/docs/images/templates-screenshots/website_templates2.jpg)
</details>

<details>
<summary>Click here to view table with templates, part 3</summary>

![screenshot of folder with templates](readme/docs/images/templates-screenshots/website_templates3.jpg)
</details>

<details>
<summary>Click here to view table with templates, part 4</summary>

![screenshot of folder with templates](readme/docs/images/templates-screenshots/website_templates4.jpg)
</details>

<details>
<summary>Click here to view table with templates, part 5</summary>

![screenshot of folder with templates](readme/docs/images/templates-screenshots/website_templates5.jpg)
</details>

<details>
<summary>Click here to view table with templates, part 6</summary>

![screenshot of folder with templates](readme/docs/images/templates-screenshots/website_templates6.jpg)
</details>

<details>
<summary>Click here to view table with templates, part 7</summary>

![screenshot of folder with templates](readme/docs/images/templates-screenshots/website_templates7.jpg)
</details>


<br>

[Table of Contents](#home)

---

### Code structure

Code is built with utilization of Django framework into apps, files and folders listed below.

### Apps
- bag - functionality for managing the shopping bag.
- blog - functionality for managing the owner's blog.
- contact - contact form for direct messages from users to owner.
- checkout - functionality for managing the e-commerce transactions for the site with real-life email confirmations.
- home - functionality for managing the home page.
- products - functionality for managing the gallery containing products available for sale or only exposed for the visitors' viewing.
- profiles - functionality for managing user profiles.
- testimonials - functionality for managing feedback posts from users, combined with About section. Both Testimonial entries, entered by visitors, and About entries, entered by the owner, share the same page and functionality but are graphically separated. 


### Files
Files for running specific apps:
- admin.py - for displaying, creating, modifying and deleting information structured in models with the utilization of native Django admin panel.
- apps.py - includes application configuration for the accounts app.
- forms.py - for preparing and restructuring data, creating forms for the data and receiving and processing submitted forms and data from the user.
- models.py - contain details on every model and attributes.
- urls.py - top level website urls.
- views.py - files holding website's logic, Python functions and classes receiving requests and returning web responses.
- test_models.py - automated testing for models. 
- test_views.py - automated testing for views.
- test_forms.py - automated testing for forms.

Common files:
- manage.py - is a command-line utility for executing Django-specific tasks, e.g. starting a new app within the project or running the development server.
- Procfile - used to declare application's process types and entry points, required by Heroku.
- requirements.txt - lists Python libraries installed for the project to work.
- settings.py - settings.
- db.sqlite3 - database used in development.
- custom_storages.py - contains settings for production-phase storage.
- robots.txt - file to tell search engine crawlers which URLs the crawler can access on the site
- sitemap.xml - file to provide information about the pages, images, and other files on this site, and the relationships between them. Search engines read this file to crawl the site more efficiently.
- README.md - project's documentation.

### Folders
- pgp_project - main project for the website.
- app folders: bag, blog, checkout, home, products, testimonials.
- helpers - features not being core of the website, contains views for rendering 403, 404 and 500 error pages.
- readme - contains files necessary for Readme document to show all of its intended content.
- static - contains all static files, e.g. style.css, in one place for easy access and management.
- media - contains dynamic media files.
- templates - contain html and txt files both supplied with apps and custom-made.

## Data schema

**Database**

A relational database was used for this project. 

During development process SQLite DB and Postgres technologies were used. For deployment the data was migrated to Heroku Postgres. 

[Amazon Web Services (AWS)](https://aws.amazon.com/) service was used for storing static and media files. 

**Data schema diagram**

![screenshot of data schema](readme/docs/images/database/data_schema.jpg)

---

## Models
The following models represent the database structure for the website.

### Model: User
- This model represents a user and is based on Django allauth library.
- This model contains the following fields: username, first_name, last_name, email, password, tel, is_staff, is_active, is_superuser.

Relationships
- It has one-to-one relationship with UserProfile model (one User can be related to one UserProfile).
- It has one-to-many relationship with Post model (one user can be related to many posts and many likes).
- It has one-to-many relationship with Testimonial model (one user can be related to many testimonials).

***App: profiles***

### Model: UserProfile
- Part of profiles app.
- This model one-to-one relationship with user model and represents the user's default contact details, applied mainly for shipment.
- This model contains the following fields: user, default_phone_number, default_street_address1, default_street_address2, default_town_or_city, default_county, default_postcode, default_country.

<details>
<summary>Click here to view UserProfile model</summary>

![screenshot of Post model part 1](readme/docs/images/database/profiles_model1.jpg)

![screenshot of Post model part 1](readme/docs/images/database/profiles_model2_receiver.jpg)
</details>
<br>

***App: blog***

### Model: Post
- Part of blog app.
- This model represents posts in blog run by the owner.
- This model contains the following fields: title, slug, author, content, fetured_image, highlight, live, created_on, updated_on.

Relationships
- It has one-to-many relationship with User model (one user can be related to many posts).

<details>
<summary>Click here to view Post model</summary>

![screenshot of Post model part 1](readme/docs/images/database/post_model.jpg)
</details>
<br>

### Model: BlogSettings
- Part of blog app.
- This model is created to contain settings for the blog and has no relationships with other models.

<details>
<summary>Click here to view BlogSettings model</summary>

![screenshot of Post model part 2](readme/docs/images/database/blogsettings_model.jpg)
</details>

<br>

***App: contact***

### Model: Contact 

- Represents messages recorded by visitors on the webpage, viewable by owner on the Admin page in section Contact / Messages.
- This model contains the following fields: name, contact_name, email, subject, body, created_on.

Relationships
- It has one-to-many relationship with User (one user can send many messages).

<details>
<summary>Click here to view the model</summary>

![screenshot of HomeSettings model](readme/docs/images/database/contact_model.jpg)
</details>
<br>

***App: checkout***

### Model: Order
- Part of checkout app.
- This model represents orders made by users.
- This model contains the following fields: order_number, user_profile, full_name, email, phone_number, country, postcode, town_or_city, street_address1, street_address2, county, date, delivery_cost, order_total, grand_total, original_bag, stripe_pid.

Relationships
- It has one-to-many relationship with UserPrifile model (one user / UserProfile can be related with many orders).
- It has one-to-many relationship with OrderLineItem model (one order can be related with many line items).

<details>
<summary>Click here to view the model (part 1)</summary>

![screenshot of Post model part 1](readme/docs/images/database/order_model1.jpg)
</details>

<details>
<summary>Click here to view the model (part 2)</summary>

![screenshot of Post model part 2](readme/docs/images/database/order_model2.jpg)
</details>
<br>

### Model: OrderLineItem
- Part of checkout app.
- This model represents items in an order made by user.
- This model contains the following fields: order, product, quantity, lineitem_total.

Relationships
- It has one-to-many relationship with Order model (one order can be related with many line items).
- It has one-to-one relationship with Product model (one line item can be related with one product).

<details>
<summary>Click here to view the model</summary>

![screenshot of Post model part 1](readme/docs/images/database/orderlineitem_model.jpg)
</details>
<br>

### Model: CheckoutSettings
- Part of checkout app.
- This model represents settings for commercial transactions, alterable by owner in Admin page.
- This model contains the following fields: live, free_delivery_threshold, standard_delivery_percentage, delivery_min_charge.

Relationships
- It has no relations with other models.

<details>
<summary>Click here to view the model</summary>

![screenshot of CheckoutSettings model](readme/docs/images/database/checkoutsettings_model.jpg)
</details>
<br>


***App: home***

### Model: HomeSettings 

- Part of home app.
- Represents settings for the home app, alterable  by owner on the Admin page. With this setting the owner can change the default background image used for the welcome page.
- This model contains the following field: background_image.

Relationships
- It has no relations with other models.

<details>
<summary>Click here to view the model</summary>

![screenshot of HomeSettings model](readme/docs/images/database/homesettings_model.jpg)
</details>
<br>


***App: products***

### Model: Product

- Part of products app.
- Represents all pieces of art in the gallery, both the ones available for sale and not available.
- This model contains the following fields: title, sku, excerpt, description, price, image, category, orientation, is_unique, priority, highlight, available, live, created_on, updated_on.

Relationships
- It has one-to-many relationship with Category model (one category can be related with many products).
- It has one-to-many relationship with OrderLineItem model (one product can be related with many line items).

<details>
<summary>Click here to view Product model</summary>

![screenshot of Product model](readme/docs/images/database/product_model.jpg)
</details>

<br>

### Model: Category

- Part of products app.
- Represents categories of the pieces of art in the gallery. Categories are shown in sub-menu when user is in Gallery and serve as filters for the art pieces shown in the Gallery. List of categories can be edited by owner on the admin page.
- This model contains the following fields: name, friendly_name.

Relationships
- It has one-to-many relationship with Product model (one category can be related with many products).

<details>
<summary>Click here to view Category model</summary>

![screenshot of the model](readme/docs/images/database/category_model.jpg)
</details>
<br>


***App: testimonials***

### Model: Testimonial

- Part of testimonials app.
- Represents entries shown on the About page. Entries made by registered users need to be approved by owner and only after approval are shown in the Testimonials / Feedback section. Entries made by owner and marked as "About" (about_me option checked in the form) are shown on the same page in the About section.
- This model contains the following fields: title, author, content, craeted_on, updated_on, priority, about_me, live.

Relationships
- It has one-to-many relationship with User model (one user can be related with many entries).

<details>
<summary>Click here to view Testimonial model</summary>

![screenshot of Testimonial model](readme/docs/images/database/testimonial_model.jpg)
</details>

<br>

### Definitions

- ManyToManyField - class used for many-to-many relationships, when a model needs to reference multiple instances of a different model. In an example of blog app, in Post model, a post can be liked by many users and a user can like many posts.
- ForeignKey - class used for one-to-many relationships. ForeignKey is a Django ORM (Object-Relational Mapper) field-to-column mapping for creating and working with relationships between tables in relational databases.
- cascade used on on_delete - means that rows in the child table will be deleted when rows in the parent table are deleted.
- CharField - class used for small- to large-sized strings, can have max_length (maximum length) specified. 
- SlugField - class used for creating a slug, which is a short label for something, containing only letters, numbers, underscores or hyphens, generally used in URLs. SlugField can also have Max_length specified.
- unique - when equal True it sets requirement that given key has unique value. In case of slug this is to prevent repeated values hindering post addressing. 
- related_name - is used when one record of a model is related to exactly one record of another model. E.g. author field in the Post model is the same as the ForeignKey it's been given (User model).
- blank - when True this allows field to be left blank, when False field is required to be filled.
- auto_now_add - when True allows to automatically fill the DateTimeField with current date and time.
- BooleanField - allows for true / false statements.
- Meta - class allowing for changing behaviour of the model fields, e.g. setting order in which data is presented.
- verbose_name - allows to alter label accompanying a form field.
- verbose_name_plural - allows to alter plural for a field, represented in Admin page.
- `__str__(self)` -  allows to return an object converted into a string which can be used for the admin page and other purposes. 
- reverse_lazy - is an implementation of the reverse URL resolver, unlike the tradditional reverse function, reverse_lazy won't execute until the value is needed. It is useful because it prevents 'Reverse Not Found' exceptions when working with URLs that may not be immediately known, which - in this project - is the case in CreatePost class.

___
## 1.iv. Skeleton <a name='skeleton'></a>

Layout of the interface, navigation and information design for different screen sizes were planned with utilization of wireframes created in Balsamiq. 

Minor changes were applied since drafting the wireframes created in the beginning of the project. E.g. some elements were centred rather than justified as this suited better to the art-centric representation of the art pieces. 

<details>
<summary>Wireframe: Home page</summary>

![image](readme/docs/images/wireframes/home.png)
</details>

<details>
<summary>Wireframe: Gallery</summary>

![image](readme/docs/images/wireframes/products.png)
</details>

<details>
<summary>Wireframe: Product details</summary>

![image](readme/docs/images/wireframes/product_detail.png)
</details>

<details>
<summary>Wireframe: Blog</summary>

![image](readme/docs/images/wireframes/blog.png)
</details>

<details>
<summary>Wireframe: About</summary>

![image](readme/docs/images/wireframes/about_me_testimony.png)
</details>

<details>
<summary>Wireframe: Contact</summary>

![image](readme/docs/images/wireframes/contact.png)
</details>

<details>
<summary>Wireframe: Account - login</summary>

![image](readme/docs/images/wireframes/account_login.png)
</details>

<details>
<summary>Wireframe: Account - logout</summary>

![image](readme/docs/images/wireframes/account_logout.png)
</details>

<details>
<summary>Wireframe: Account - signup</summary>

![image](readme/docs/images/wireframes/account_signup.png)
</details>

<details>
<summary>Wireframe: Account - password reset</summary>

![image](readme/docs/images/wireframes/account_pass_reset.png)
</details>

<br>

___
## Business logic

Flow of information and decisions the website operates on are represented in the flowchart below.

<details>
<summary>Click here to view business logic flowcharts</summary>
Main chart

![image](readme/docs/images/business-logic/flowchart_main.jpg)

About / Testimonials

![image](readme/docs/images/business-logic/flowchart_about.jpg)

Account management / logins

![image](readme/docs/images/business-logic/account_management.jpg)
</details>

<br>

## 1.v. Surface <a name='surface'></a>
One of the goals behind building the webpage for the Artist is exposition of the Artist's items. Usage of colour is minimised to leave space to the art itself. This is reflected in the webpage surface.

### **Colour Palette**
Colour palette reflects the simplicity of an art gallery. For this purpose pastel colours are used, mainly blue and red with light shades of beige. Blue brings cleanliness and lightness to mind and red is commonly associated with health care while light beige binds them together in a subtle, friendly environment.

Screenshot of colour palette:

![screenshot of colour palette](readme/docs/images/surface/coolors_palette.jpg)

### **Typography**

Fonts chosen for the site had to be light, simple and easy to read to be coherent with the rest of the graphic design. For this purpose I chose fonts: 
- PT Serif for the content with fall-back font Source Serif Pro. 
- Josefin Sans for functional areas of the site: navigation, confirmations and alerts and footer.
- Tenor Sans for text input areas.

All fonts are available from Google Fonts service.

<details>
<summary>Screenshots of used fonts</summary>

![image](readme/docs/images/surface/font_pt_serif.jpg)
![image](readme/docs/images/surface/font_source_serif_pro.jpg)
![image](readme/docs/images/surface/font_josefin_sans.jpg)
![image](readme/docs/images/surface/font_tenor_sans.jpg)
</details>

<br>

### **Imagery**


Graphics for the site were chosen with the intention of maintaining the theme of a minimalistic environment of an art gallery where it is the art itself that takes priority. 

The design is dominated by Black and White with some Jet (very dark grey) and Gainsboro (very light grey) with addition of scant usage of colours Indigo Dye and Ming. Colours were chosen by the artist herself. 

The only image used outside the product list is the background for the home page. The default image is the piece painted and selected for this purpose by the artist herself and can be overwritten in the Admin page.

<details>
<summary>Click here to view image</summary>

![image 1](readme/docs/images/surface/home.jpg)
</details>

<br>

[Table of Contents](#home)

___

# 2. Features <a name='features'></a>

## 2.i. Current features <a name='features-current'></a>

<br>

### **Feature 1. Navigation bar**

Navigation bar is present on top of the screen on all pages of the site. Aim of this feature is that the user always has access to easy navigation across the site without the need to use browser navigation features, e.g. 'back' button.
The navigation bar consists of two parts: the main navigation bar and secondary bar below. The main bar contains links to Home page, search bar, My Account and Bag with submenu with links to the sections of the site: Gallery, Blog and About. The secondary bar contains a link to the highlights and in case user chooses Galleryin the main navigation bar it lists categories of products. The list of categories works as an additional navigation bar, allowing the user to filter through the products shown in the Gallery. List of categories can be edited by owner in Admin page.

**Responsive design**

Navigation bar is responsive to screen size, all buttons are visible on large screens, while on small screens navigation menu is available from the hamburger button. The artist's name serving as a logo also serves as a 'home' button and is visible on small to medium screens and is replaced by Home link in the hamburger menu on small screens. 

Navigation menu is minimized to hamburger button on small screens:
<details>
<summary>Click here to view image </summary>

![screenshot of navbar](readme/docs/images/testing/features/navbar_small.jpg)
</details>
<br>

Navigation menu pulled down from the hamburger menu:
<br>
<details>
<summary>Click here to view image </summary>

![screenshot of navbar](readme/docs/images/testing/features/navbar_small_pulled.jpg)
</details>
<br>

Navigation menu stretched on a larger screen:
<br>
<details>
<summary>Click here to view image </summary>

![screenshot of navbar](readme/docs/images/testing/features/navbar_large.jpg)
</details>
<br>

**Authorization - dependent navigation**

Navigation menu is dependent on current user profile. This is reflected in options available under the icon My Account:

- Without logging in users are presented with the simplest menu: Register, Login. 
- Customer users after logging in have access to options: Share my experience, My Profile, Logout.
- Staff users have access to Product, Blog and About/Testimonials Management. 

Registered clients have a possibility of checking and updating user information and adding their testimony.

Staff users' authorisation is expanded by reading, adding, editing and deleting information related to products, blogs and testimonies. This is supported by appropriate links throughout the website.

After logging in the expression My Account is replaced by the user's first name or username if the former is not available. This gives the user a clear indication about their login status.

My Account - unregistered user:
<details>
<summary>Click here to view image </summary>

![screenshot of navbar](readme/docs/images/testing/features/navbar_basic.jpg)
</details>
<br>

My Account - registered user:
<details>
<summary>Click here to view image </summary>

![screenshot of navbar](readme/docs/images/testing/features/navbar_registered.jpg)
</details>
<br>

My Account - staff:
<details>
<summary>Click here to view image </summary>

![screenshot of navbar](readme/docs/images/testing/features/navbar_staff.jpg)
</details>
<br>

Access to navbar features:

| No. | Feature                            | Not logged in | Logged in client | Staff | Admin |
| --- | ---------------------------------- | ------------- | ---------------- | ----- | ----- |
| 1   | Navigation bar                     | yes           | yes              | yes   | yes   |
| 2   | Gallery, Blog, About               | yes           | yes              | yes   | yes   |
| 3   | Login / Logout                     | yes           | yes              | yes   | yes   |
| 4   | My Profile                         | no            | yes              | yes   | yes   |
| 5   | Product Management                 | no            | no               | yes   | yes   |
| 6   | Blog / Highlights Management       | no            | no               | yes   | yes   |
| 7   | About / Testimonials Management    | no            | no               | yes   | yes   |
| 8   | Admin screen                       | no            | no               | no    | yes   |

<br>

#### **Related user stories**

1.2 As a **site user** I can **register** so that **I can reuse once entered information**.

1.3 As a **site user** I can **log in using my username and password** so that I can **reuse once entered personal information**.

1.4 As a **site user** I can **log out of my account** so that I know **my information stays confidential**.

1.5 As a **site user** I can **easily see my current login status** so that **I can control my status for privacy protection**.

1.6 As a **site user** I receive **confirmation of logging in and logging out visible on webpage** so that I **instantly know if the operation was successful**.

1.7 As a **site user** I can **reset my password** so that I can **safely remain the website's registered user**.

2.1 As a **site user** I can **navigate the service intuitively** so that I can **utilize all of its content**.

2.2 As a **site user** I can easily **browse through available items** so I can **decide which ones are most appropriate to me**.

2.3 As a **site user** I can **navigate the site on all kinds of screens** so that **I am not limited to any kind of device**.

2.5 As a **site user** I can **easily go back to home page** so I can **restart my experience**.

<br>

### **Feature 2: Footer**
The footer is displayed below all other content. Short information about the project and links to company's social media are placed there. Links are available to all users, open in a different tab for easy navigation and contain: 
- Facebook.
- Instagram,
- YouTube,

<br>
Click to view image:
<details>
<summary>Footer</summary>

![screenshot of image](readme/docs/images/testing/features/footer.jpg)
</details>
<br>

#### **Related user stories**

1.8 As a **site user** I can **read webpage's privacy policy** so that I can **know if my personal information is safe**.

2.4 As a **site user** I can **find links to Artist's social media wherever I am on the webpage** so that **I can use alternative means of getting the content**.

<br>

[Table of Contents](#home)

---

### **Feature 3. Home page**

On home page user is welcomed with a hero picture whose goal is to draw attention and set a scene and mood of the site. In the middle of the hero page is a semi-transparent section with titles of blog entries the owner marked as highlights. Also, on small screens the logo-styled artist's name is moved here from the top navigation bar. To continue on to the content user can either click one of the links on the navigation bar or click one of the highlighted post titles in the welcome box.  Scrolling down will result in showing the footer. 

<br>

<details>
<summary>Home screen on large screen </summary>

![screenshot of image](readme/docs/images/surface/home.jpg)
</details>

<details>
<summary>Home screen on small screen </summary>

![screenshot of image](readme/docs/images/surface/home_small_scr.jpg)
</details>
<br>

#### **Related user stories**

3.1 As a **site user** I can **locate convenient routes of communication with owner, including company's social media accounts** so I can **stay in contact through alternative means**.

3.2 As a **site user** I can **subscribe to a newsletter** so I can **stay engaged and stay up do date with the Artist's offering and creative process**.

3.4 As a **site user** I can **see immediately information about newest content** so I can **go directly to that content should I wish to do so**.

<br>

[Table of Contents](#home)

---
### **Feature 4. Account management**
This functionality allows user to register an account, login an logout of the account and change password. 

Click to view image:
<details>
<summary>Sign in </summary>

![screenshot of image](readme/docs/images/testing/features/acc_mgt_login.jpg)
</details>
<br>

Users without account may open account online:
<details>
<summary>Sign up </summary>

![screenshot of image](readme/docs/images/testing/features/acc_mgt_signup.jpg)
</details>
<br>

In case of a failed login attempt an information about incorrect login credentials is shown on page and user can try to login again.
<details>
<summary>Failed login </summary>

![screenshot of image](readme/docs/images/testing/features/acc_mgt_login_fail.jpg)
</details>
<br>

User can reset password online:
<details>
<summary>Password reset </summary>

User enters email address:
![screenshot of image](readme/docs/images/testing/features/acc_mgt_reset.jpg)

Example email user receives to reset password:
![screenshot of image](readme/docs/images/testing/features/password_reset_email.jpg)
</details>
<br>

On successful login user is redirected to the main page and shown a temporary confirmation message:
<details>
<summary>Successful login </summary>

![screenshot of image](readme/docs/images/testing/features/acc_mgt_login_success.jpg)
</details>
<br>

When logged in user has easy access to information about their profile:
<details>
<summary>Profile information</summary>

![screenshot of image](readme/docs/images/testing/features/acc_mgt_profile_info.jpg)
</details>

<br>

Logged in user can sign out. After signout user is redirected to the main page and temporary confirmation message is shown:
<details>
<summary>Sign out question </summary>

![screenshot of image](readme/docs/images/testing/features/acc_mgt_signout_q.jpg)
</details>

<details>
<summary>Sign out confirmation </summary>

![screenshot of image](readme/docs/images/testing/features/acc_mgt_signout_success.jpg)
</details>
<br>

**Error pages**

In case a problem occurs when a user tries to access a page an error page is shown:

<details>
<summary> Error 403 (Access forbidden) </summary>

![screenshot of image](readme/docs/images/testing/features/error403.jpg)
</details>

<details>
<summary> Error 404 (Page does not exist) </summary>

![screenshot of image](readme/docs/images/testing/features/error404.jpg)
</details>

<details>
<summary> Error 500 (Server error) </summary>

![screenshot of image](readme/docs/images/testing/features/error500.jpg)
</details>

<br>

### Access to account management features
| No. | Feature                 | Not logged in | Logged in client | Staff | Admin |
| --- | ----------------------- | ------------- | ---------------- | ----- | ----- |
| 2   | Sign in                 | yes           | no               | yes   | yes   |
| 3   | Sign out                | no            | yes              | yes   | yes   |
| 4   | Sign up                 | yes           | no               | yes   | no    |
| 6   | Reset password          | yes           | no               | yes   | no    |
| 1   | User account management | no            | no               | no    | yes   |

#### **Related user stories**

1.1 As a **site user** I can **access site without logging in** so that I can **read information about available products**.

1.2 As a **site user** I can **register** so that **I have access to personalized service**.

1.3 As a **site user** I can **log in using my username and password** so that I can **access site's enhanced functionality**.

1.4 As a **site user** I can **log out of my account** so that I know **my information stays confidential**.

1.5 As a **site user** I can **easily see my current login status** so that **I know I'm in control of access to my enhanced service on currently used device**.

1.6 As a **site user** I receive **confirmation of logging in and logging out visible on webpage** so that I **instantly know if the operation was successful**.

1.7 As a **staff site user** I can **access enhanced functionality** so that I can **add, edit and delete content on webpage**.

3.3 As a **registered site user** I can **use website without having to re-enter my details** so that **my activity on the site requires minimum afford from my side**.

<br>

[Table of Contents](#home)

---

### **Feature 5. Products**

Products page on this website is created with an intent to provide an easy and convenient way to present visitors with the artist's creations. Products can have their status checked as 'live' and only those are visible to non-staff users.  Items on display include the ones available and not available for sale. Only products with status 'available' can be added to bag and purchased. Staff users can edit and delete products by clicking option 'Edit' or 'Delete' under the product description. These options are only visible to staff users. Adding new products can be done by choosing option 'Product Management' under 'My Account'.

Items are shown in order of priority and date of creation. 

Each product consists of:
- graphic illustration
- title
- excerpt
- price
- description - visible on product detail page.

<details>
<summary>Products, main page</summary>

![screenshot of image](readme/docs/images/testing/features/products.jpg)
</details>

<details>
<summary>Product search</summary>
On top of the page user can perform a search on products by entering a phrase in a search box. 
As a result of the page information on number of found products is shown together with a list of products adequate to the search criteria.

![screenshot of image](readme/docs/images/testing/features/product_search.jpg)

</details>

<details>
<summary>Product filtering by category</summary>
On Gallerypage the announcements bar changes to a secondary navigation bar which visitor can use to filter products by category. Each name of category is a button which triggers filtering products shown on the page. 

![screenshot of image](readme/docs/images/testing/features/products_filter_bar.jpg)

</details>

<details>
<summary>Product filtering by availability</summary>
An additional way for the user to filter products is availability. This functionality is triggered by buttons "Show available" and "Show unavailable" at the bottom of the Gallery.

![screenshot of image](readme/docs/images/testing/features/products_filter_availability.jpg)

</details>

<details>
<summary>Product details</summary>
On product detail page user can see full description of the product and can add the product to a bag.

![screenshot of image](readme/docs/images/testing/features/product_details.jpg)

</details>

<details>
<summary>Product edit</summary>

Product edit is only available to staff users, after clicking on Edit button.

![screenshot of image](readme/docs/images/testing/features/product_edit_1.jpg)

![screenshot of image](readme/docs/images/testing/features/product_edit_2.jpg)

![screenshot of image](readme/docs/images/testing/features/product_edit_3.jpg)
</details>

<br>

### Access to products features

| No. | Feature                       | Not logged in | Logged in client | Staff | Admin |
| --- | ----------------------------- | ------------- | ---------------- | ----- | ----- |
| 1   | View products                 | yes           | yes              | yes   | yes   |
| 2   | Create, Edit, Delete products | no            | no               | yes   | yes   |
| 3   | Search, filter products       | yes           | yes              | yes   | yes   |

<br>

#### **Related user stories**

4.1 As a **site user** I can **quickly get a general idea about items on offer** so that I can **decide which content to get acquainted with more thoroughly**.

4.2 As a **site user** I can **read details about a chosen item** so that I can **make the best decision about the purchase based on technical information (e.g. size) and my personal preferences**.

4.3 As a **site owner** I can **create, update and delete item entries** so that I can **inform visitors on pieces on offer and pieces sold**.

4.4 As a **site owner** I can **prioritize which items are shown first on the site** so that I can **influence demand on offering of my choice**.

<br>

[Table of Contents](#home)

---

### **Feature 6. Blog**

In the blog app standard mechanisms of a blog are employed. Posts can be created, edited and deleted by users with staff status including admin. Adding a new post can be done by choosing a link Blog/Highlights under My Account or in admin page. Editing and deleting posts can be done on the webpage after choosing appropriate button under a post (only visible to staff users) or on admin page by the administrator of the webpage. Users who are not logged in or are logged in as non-staff can see posts with status "live". Staff users can see both "live" and "draft" posts.

**Blog**

All users can view a list of posts with "live" status.
<details>
<summary>Blog - guest </summary>

![screenshot of image](readme/docs/images/testing/features/posts_guest.jpg)
</details>

<details>
<summary>Post - shortened version</summary>

![screenshot of image](readme/docs/images/testing/features/post_cut.jpg)
</details>
<br>

Staff users can see both "live" and non-live / draft posts and can add new, edit and delete posts. 
<details>
<summary>Post add / edit</summary>

![screenshot of image](readme/docs/images/testing/features/post_edit.jpg)
</details>
<br>

**Post details**

To maintain seamless flow of blog posts on the blog page long posts are cut and show Read More button at the bottom. The button leads to a detail page presenting full content of the post.

Each post consists of:
- title
- date of creation
- optional graphic illustration
- content

<details>
<summary>Post details</summary>

![screenshot of image](readme/docs/images/testing/features/post_details.jpg)
</details>
<br>

Blog visibility is controlled in admin site in section Blog - Settings.

### Access to blog features

| No. | Feature     | Not logged in | Logged in client | Staff | Admin |
| --- | ----------- | ------------- | ---------------- | ----- | ----- |
| 1   | Create post | no            | no               | yes   | yes   |
| 2   | Edit post   | no            | no               | yes   | yes   |
| 3   | Delete post | no            | no               | yes   | yes   |
| 4   | Read post   | yes           | yes              | yes   | yes   |
| 5   | Hide blog   | no            | no               | no    | yes   |

#### **Related user stories**

5.1 As a **site user** I can **read Artist's blog** so that I can **stay up to date with the Artist's developments**.

5.2 As a **site owner** I can **create, update and delete blog entries** so that I can **share content of my choice and build a sense of connection with my audience and prospective buyers**.

5.3 As a **site owner** I can **hide and unhide blog** so that I can **control visibility of the entire blog section of the site at any time**.

<br>

[Table of Contents](#home)

---

### **Feature 7. About**

About page consists of two parts:
- Personal note - introduction and general information about the artist.
- Testimonials - feedback gained from users who already interacted with the artist.

Both parts utilize functionality of the same testimonials app. Entries in the Personal note section have 'about_me' key checked and can only be created by the staff user while entries in the Testimonials section have the 'about_me' key unchecked and can be created by any logged in user. In practice they will probably always be the customers. All entries need to have their key 'live' checked by the staff user to be visible to all visitors.  

<details>
<summary>About</summary>

![screenshot of image](readme/docs/images/testing/features/about_me.jpg)
</details>
<br>

#### **Personal Information**

This feature is available for viewing to all users. Only staff users can create and edit posts in this section.

#### **Testimonials**

This feature is available for viewing to all users. By default new testimonials are added with their key 'live' unchecked and become visible only after a staff user checks the key 'live'. Until that time the posts are only visible to staff users with a note "Awaiting approval". Only registered users can create posts in this section.

Users can add their testimonials by entering the testimonial content and - optionally - the title.
<details>
<summary>Testimonial form - user</summary>

![screenshot of image](readme/docs/images/testing/features/testimonial_add_user.jpg)
</details>
<br>

Staff can add entries which will be shown in Testimonials section (with key 'about_me' unchecked) or in Personal Note section (with key 'about_me' checked). Staff users can enter or edit title, content, priority, 'About' option (which moves an entry to the Personal Note section), and 'live' option (which enables the entry's visibility to all users).
<details>
<summary>Testimonial form - staff</summary>

![screenshot of image](readme/docs/images/testing/features/testimonial_add_staff.jpg)
</details>

<br>

### Access to About features

| No. | Feature                    | Not logged in | Logged in client | Staff | Admin |
| --- | -------------------------- | ------------- | ---------------- | ----- | ----- |
| 1   | Create Personal Note       | no            | no               | yes   | yes   |
| 2   | Edit, delete Personal Note | no            | no               | yes   | yes   |
| 3   | Create Testimonial         | no            | yes              | yes   | yes   |
| 4   | Edit, delete Testimonial   | no            | no               | yes   | yes   |

#### **User Stories related to feature 7**

3.6 As a **site user** I can **share my experiences in Testimony** so that **I feel that I contribute to the community gathered around the Artist**.

3.7 As a **site owner** I can **present a basic personal introduction** so that **I know potential and current customers have a chance to build a personal connection with me as an artist**.
<br>

[Table of Contents](#home)

---

### **Feature 8. Contact**

Contact page contains a simple contact form given to user's disposal should they wish to contact the page owner directly.

Login is not required to use its functionality, albeit for logged in users the user name and email address details are automatically prefilled. Owner has access to the messages on the Admin page. 

<details>
<summary>Contact</summary>

![screenshot of image](readme/docs/images/testing/features/contact.jpg)
</details>

<br>

### Access to Contact features

| No. | Feature                    | Not logged in | Logged in client | Staff | Admin |
| --- | -------------------------- | ------------- | ---------------- | ----- | ----- |
| 1   | Send direct message        | yes           | yes              | yes   | yes   |
| 1   | Read direct message        | no            | no               | no    | yes   |

#### **User Stories related to feature 8**

3.1 As a **site user** I can **locate convenient routes of communication with owner, including company's social media accounts** so I can **stay in contact through alternative means**.

3.3 As a **registered site user** I can **use website without having to re-enter my details** so that **my activity on the site requires minimum afford from my side**.

---

### **Feature 9. E-Commerce**

In the Gallery section user is presented with a list of products with basic information about each item. There, after clicking on item image, item description, or a link 'Show details' the user is directed to product detail page. On the product detail page the user has the opportunity to add a product to a bag by clicking on a button 'Add to Bag'. 

**Bag**

<details>
<summary>Product details - add to bag</summary>

![screenshot of image](readme/docs/images/testing/features/ecommerce_add_to_bag.jpg)
</details>
<br>

After adding a product to the bag user is presented with a temporary confirmation in form of the toast in the top right corner of the screen.
<details>
<summary>Add to bag confirmation</summary>

![screenshot of image](readme/docs/images/testing/features/ecommerce_add_to_bag_toast.jpg)
</details>
<br>

As a general rule products presented in the Gallery are unique art items. This is the reason why when such a unique product is already in the bag then button 'Add to Bag' is no longer available and a short information 'Item is in your bag' is presented in its place. Exceptions to this were taken into consideration and if an item is not unique (key 'is_unique' is unchecked in product details), then the 'Add to Bag button' will still appear, allowing the customer to add more than one item of the same product.

<details>
<summary>Product details - item in bag</summary>

![screenshot of image](readme/docs/images/testing/features/ecommerce_add_to_bag_na.jpg)
</details>

<details>
<summary>Bag page</summary>

![screenshot of image](readme/docs/images/testing/features/ecommerce_bag.jpg)
</details>
<br>

**Checkout**

The checkout page consists of the following main parts:
- User details
- Delivery information
- Order summary
- Payment information

For the checkout page information about the user is preloaded, if available. The information can be altered by the user and saved by checking the option 'Save this delivery information to my profile'. 

Before completing the order user can adjust details or adjust items in the bag by clicking 'Adjust Bag' button. When satisfied user can click 'Complete Order' button. 

<details>
<summary>Checkout page</summary>

![screenshot of image](readme/docs/images/testing/features/ecommerce_checkout.jpg)
</details>
<br>

After confirming the purchase a confirmation page is shown with the summary of the transaction.
<details>
<summary>Checkout confirmation</summary>

![screenshot of image](readme/docs/images/testing/features/ecommerce_checkout_confirmation.jpg)
</details>
<br>

Every unique item changes its status to not available after sale. In place of price a note is presented under the item description 'Item is not available for sale' and no more transactions are possible for this item. It is still presented in the Gallery until the owner decides otherwise.

<details>
<summary>Item not available for sale</summary>

![screenshot of image](readme/docs/images/testing/features/ecommerce_item_unavailable.jpg)
</details>

<details>
<summary>Email confirmation after purchase</summary>

![screenshot of image](readme/docs/images/testing/features/ecommerce_confirmation_email.jpg)
</details>
<br>

### Access to e-commerce features

| No. | Feature                          | Not logged in | Logged in client | Staff | Admin |
| --- | -------------------------------- | ------------- | ---------------- | ----- | ----- |
| 1   | Add and remove products to bag   | yes           | yes              | yes   | yes   |
| 2   | Purchase items                   | yes           | yes              | yes   | yes   |
| 3   | Save and edit saved user details | no            | yes              | yes   | yes   |

After user completes checkout the transaction is processed by Stripe system. 

<br>

#### **Related user stories**

7.1 As a **site user** I can **smoothly go through purchase process** so that I can **acquire a chosen item**.

7.2 As a **site owner** I can **monitor transaction's status** so I can **ensure process of purchase and delivery is successfully completed**.

7.3 As a **site user** I can **receive a confirmation email after a transaction** so I can **be assured about the status of my order**.

<br>

[Table of Contents](#home)

---

## 2.ii. Potential features <a name='features-next'></a>
Features 
 - Wider array of ways to signup and login, e.g. via social media, Google,
 - Emails sent to users automatically on new blog entry.
 - Menu with choice of languages for the website to appear incorporated into the site.

# 3. Marketing Strategy <a name='marketing-strategy'></a>

**Marketing introduction**

When deciding on marketing strategy for this project the following information and assumptions were taken into account:

- The Business model is an online store operating within these types of activities:
    - *Business - to - Customer* (businesses may also be making purchases but are not the main target market at this stage) - this influences priorities for this project:
        - an easy and clear payment gateway process,
        - simple yet secure authentication system,
        - high quality images of products,
        - clear and simple item descriptions,
        - users' personal engagement. 
    - *Supplying physical products* (mostly paintings and drawings) - which calls especially for: 
        - creating a shopping bag mechanism where user's choices may be remembered,
        - clear descriptions with high quality representations,
    - *Receiving single payments* (no subscriptions) - as the store's products are mostly unique by their nature.
- Main target groups are:
    - young European aspiring professional adults,
    - mature European adults with stable material situation, especially appreciating niche art.
- Online platforms utilized by the users are mostly:
    - Instagram (mostly the younger audience),
    - Facebook,
    - YouTube.
- Social media used by the users in the target market:
    - Instagram (younger audience),
    - Facebook (more mature audience),
    - LinkedIn.
- Users' need which the website owner may target:
    - Love for art and beauty - which can be addressed by selling art to them,
    - Interest in artistic expression - which can be addressed by: 
        - providing them with blog and video content related to creative process, 
        - opportunity to express their interest and experiences on the website in the Testimonials section,
    - Aspirational needs (showing interest in arts in social circles) - which can be addressed by selling art and providing with opportunities - via blog and newsletter - to engage in cultural life via taking part in exhibitions and other artistic events.
- Owner may want to run promotional activities. Tools for communication for running them with the help of the website include: 
    - newsletter, 
    - blog,
    - highlights on welcome page (where a link to chosen art pieces is placed on secondary navigation bar and titles of highlighted blog entries take prominent space of the welcome box). 
- Owner's goals related with the website:
    - Selling her art,
    - Sharing artistic process,
    - Connecting with art-loving audience.
- It is assumed that the owner focuses on organic growth of this activity and no significant  marketing budget is planned. The main resource dedicated to the project is a limited amount of the artist's time focused on creation of custom content and building engagement with potential buyers.


## 3.i Search Engine Optimisation

**Keywords**

One of the marketing methods applied for the project is signalling a set of keywords for search engines. Keywords are the tool for helping potential users find the webpage. The aim is to select keywords with relatively high volume of searches and low competition in search results. In that process a tool [Google Keyword Planner](https://ads.google.com/home/tools/keyword-planner/) was used.

The chosen keywords are implemented in the site content where possible, e.g. as a slogan "The Polish Artist in Germany" situated under the links to highlighted blog posts on the welcome page, or in the About section.

<details>
<summary>Keywords research</summary>

![screenshot of image](readme/docs/images/marketing/google_keyword_planner_table.jpg)
</details>
<br>

Short-tail keywords chosen:
- polish artist, paintings online, polish painter, craft contemporary
 
Long-tail keywords chosen:
- polish female artist, contemporary art exhibitions, gallery of contemporary art, flower paintings for sale, modern art and contemporary art, landscape art for sale, European art painting

Owner-specific keywords:
- monika curto fuentes, polish girl painting

**Semantic HTML Elements**

Standard semantic HTML elements were used in the project, used according to their intended purpose and in separation from content and presentation. This should help in the site's Search Engine Optimisation. The elements include:

- textual meaning `<h1>`, `<strong>`, `<em>`
- document structure `<header>`, `<footer>`, `<main>`, `<nav>`, `<aside>`, `<article>`
- correlation tags `<ul>`

Instructions for search engines**

**Links**

Links not useful in respect of search engine analytics have been equipped with anchor tag nofollow (in respect of SEO) and noopener (in respect of safety of the site).

Links to outside sites potentially valuable from search engine optimisation standpoint were added in About section. 

**Meta Tags**

Meta tags description and keywords have been added in the base page for the benefit of search engine optimisation.

Base template has been equipped with canonical link for search engine recognition of the original site.

**Crawlers management**

For directing search engines on the site two files were created:
- sitemap.xml
- robots.txt

Inclusion protocol

For enabling search engines to index the website Sitemaps was used. Sitemaps is a protocol in XML format meant for a webmaster to inform search engines about URLs on a website that are available for web crawling. For this purpose the file sitemap.xml was crated on the site [XML-Sitemaps](https://www.xml-sitemaps.com/) and placed in root folder. 

Exclusion protocol

To direct search engines to the sitemap and exclude chosen areas of the webpage from crawlers a file robots.txt is added in root folder. The files tells search robots to exclude folders: accounts, bag and checkout.  

Registering sitemap

Next step, not included in this project, would be creating a DNS certificate and deployment to a custom domain. Registering the sitemap can be done in [Google Search Console](https://search.google.com/search-console/welcome). 

Testing robots file

The following step would be testing the robots.txt file. This can be done using [Google Testing Tool found](https://www.google.com/webmasters/tools/robots-testing-tool), following the steps below:
- add the property, 
- download a HTML verification file, 
- upload the file to the site tested,
- confirm successful upload by visiting the uploaded file in the browser,
- verify by clicking the link supplied on the Testing Tool page.

## 3.ii Content Marketing

**Content**

While keywords help users find the website, content is what will keep them. It has been an intention during the creating content for this project that it is:
- useful, 
- well informed, 
- trustworthy for the user. 

Maintaining those properties should positively influence search engines rankings for the site.

Apart from AI a webpage may be rated by Google Raters. The content was also created with Google Raters guidelines in mind. In this respect a site is ranked high quality when it is:
- expert,
- authoritative,
- trustworthy.

For this reason the site in this project:
- is upfront about what it represents,
- is clear about the information and its sources,
- cites sources to other trustworthy sites.

More details can be found in the [Rater Guidelines](https://static.googleusercontent.com/media/guidelines.raterhub.com/en//searchqualityevaluatorguidelines.pdf). 

Content ranking

- CTR (Click Through Rate) - measures how often users click the link to the site on search result list,
- Bounce Rate - rate by which users click return button after landing on the site,
- Dwell Time - measures how long users stay on the site before returning to search results,
- Session Time - measures how long the users stay on the site,
- Pages per Session - reflects how many pages within the site users visit during a session.

**Site modules**

Content on the website in this project is managed via three main modules:
1. Gallery - where the artists' creations are represented,
2. Blog - where post may contain text, images, embedded video links and links to other materials on the web.
3. About - this module is based on one app and is divided into two sections:
    - Personal Note - where the owner can share her content,
    - Testimonials - where visitors can share their experiences related to the topic of the webpage.

All three modules complement each other in terms of content and have the potential of engaging users and encouraging them to come back to the website.

**Social media marketing**

Footer always present at the bottom of the website encourages users to engage in alternative means of contact via social media (Instagram, YouTube and Facebook). 

<details>
<summary>Links to social media in Footer</summary>

![screenshot of Facebook account 1](readme/docs/images/marketing/footer_social.jpg)
</details>
<br>

*Facebook*

Because of Facebook's reach and amount of users it can be a valuable marketing tool for this project. An example business Facebook account has been open and is available under this [link](https://www.facebook.com/profile.php?id=100090875239254) at the time of writing this document. Below screenshots from this account can be found. 

Main page lets the owner to present information to a wide audience and utilize Facebook's paid marketing tools if such decision arises.
<details>
<summary>Main page</summary>

![screenshot of Facebook account 1](readme/docs/images/marketing/fb_main.jpg)
</details>
<br>

In the Professional dashboard the page's performance can be closely monitored. Information like number of followers, reach and engagement of a post and new likes can be seen here. 
<details>
<summary>Professional dashboard</summary>

Dashboard general information
![screenshot of Facebook account 2](readme/docs/images/marketing/fb_pro_dashboard.jpg)

Dashboard details example
![screenshot of Facebook account 3](readme/docs/images/marketing/fb_pro_dashboard_details.jpg)
</details>

<details>
<summary>Page details</summary>

![screenshot of Facebook account 4](readme/docs/images/marketing/fb_intro.jpg)
</details>

<details>
<summary>First post</summary>

![screenshot of Facebook account 5](readme/docs/images/marketing/fb_post.jpg)
</details>
<br>

Note: While the artist's Facebook account presented above was created as part of the Marketing Strategy in this project, the Footer on this site also refers to the original artist's Instagram profile. The Instagram profile is not part of this project and was not contributed to by the author of this document. 

**Email marketing**

Also in the footer a short form giving users a possibility to subscribe to a newsletter has been placed. This provides the owner with additional marketing tools at her disposal, e.g. letting users know about new items in the Gallery, important events or promotions via email and ongoing analysis of newsletter signups. Newsletter subscription is managed via [MailChimp](https://mailchimp.com/) service. 

<details>
<summary>Newsletter form</summary>

![screenshot of newsletter subcription1](readme/docs/images/marketing/footer_newsletter_form.jpg)
</details>

<details>
<summary>Subscription confirmation</summary>

![screenshot of newsletter subcription1](readme/docs/images/marketing/newsletter_subcription_confirmation_page.jpg)
</details>

<details>
<summary>Insight into audience</summary>

![screenshot of newsletter subcription2](readme/docs/images/marketing/mailchimp_audience.jpg)
</details>

<details>
<summary>Mailchimp analytics (sample data)</summary>

![screenshot of newsletter subcription3](readme/docs/images/marketing/mailchimp_analytics.jpg)
</details>



<br>

**Other marketing options**

Other marketing options, not included in the scope of this project: 


- Influencer marketing: The owner's reach of the target market can be enhanced through paid engagement of people with large followings and authority in the field.  

- Affiliate marketing: extending the traffic to the website through paid recommendations from other parties.

- Paid advertising and analytics: The website's appearance in text and geographical search results can be boosted in the form of paid advertising like ones below:
    - [Google My Business](https://www.google.com/business/) - usage of this service, which is free to register but paid for services, brings benefits mentioned below. The benefits need to be considered in line with potential risks such as negative reviews from users, unflattering photos.  
        - additional way to connect to the market
        - improved SEO
        - strengthen reputation
        - alerts on user interactions
        - advanced analytics 

    - [Google Ads](https://ads.google.com/) - promotional activities include ads in search results, ads in Google Shopping and display ads in form of a banner. Benefits for using Google Ads include:
        - specific targeting
        - results faster than in organic growth, using SEO alone
        - access to [Google Keyword Planner](https://ads.google.com/home/tools/keyword-planner/) providing detailed insights into SEO keyword volume, competition and pricing.
        - detailed analytics of success rate on promotional activity

    - [Google Analytics](https://analytics.google.com/) 
        - free to set up, highly customizable service providing detailed insights into metrics impacting the business's sales and measuring efficiency of web marketing strategies. Google Analytics can be combined with Google Ads. 
        - this complex tool requires adding specific code to the webpage (which must be GDPR compliant) and may take time for meaningful analysis to be available. This code is equipped with appropriate GDPR compliance mechanism provided by [Privacy Policy Generator](https://www.privacypolicygenerator.info/). 

**GDPR Compliance**

Website built in this project collects user data and as such needs to comply with General Data Protection Regulation (GDPR). The full list of standards related to this regulation can be found under this [link](https://gdpr.eu/). At the bottom of every page, in the footer, a link is available to all users to view the page's Privacy Policy. This ensures transparency in informing users about how their data is being collected and processed. 

The Privacy Policy is set up under the assumption that cookies are not used on this webpage. In case of a change in this area, e.g. when using Google Analytics, Facebook Pixel or Hotjar the Privacy Policy would need to be accordingly updated.


<details>
<summary>click to see screenshots</summary>
Link to Privacy Policy document:

![screenshot](readme/docs/images/marketing/footer_gdpr_link.jpg)
Fragment of custom Privacy Policy document:

![screenshot](readme/docs/images/marketing/gdpr_privacy_policy.jpg)
</details>

<br>

___

# 4. Testing <a name='testing'></a> 

**Browser compatibility**

The website was tested on browsers:
- Google Chrome
- Microsoft Edge
- Opera
- Mozilla Firefox

The choice of browsers to test were influenced by their market share according to [StatCounter](https://gs.statcounter.com/browser-market-share) as in March 2023.

## 4.i. User story testing  <a name="user-story-testing"></a>

User stories were tested with current features and passed the tests.

[Click here for User story testing](readme/docs/user_story_testing.md)

## 4.ii. Automated testing

[Click here for automated testing](readme/docs/automated_testing.md)

## 4.iii. Known issues during development and testing <a name="known-issues"></a>

**Unfixed and potential issues**

There are no observed unfixed issues and bugs.

Checks for compatibility with Apple devices were minimal due to a limited access to such devices for the author at the time of testing.

**Fixed issues and changes to original design**

*Visual appearance*

Minor changes to visual appearance were introduced after creation of first wireframes, e.g. cetering elements rather than justifying. This is believed to reflect more elegant and art-centric approach. 

*Contact*

A simple mechanism for direct messages was added to the original draft. This is believed to be in line of the Marketing Strategy where in Business-to-Customer model a strong emphasis on customers with various technical background should be made. Direct messages on the webpage should be an easy and simple solution, especially for less technically inclined users. 

*Testing redirect*

When producing automatic tests for bag page it was not possible to utilize assertRedirects test on response with post method. To perform the test assertEqual was used instead:

    last_url, status_code = response.redirect_chain[-1]
    self.assertEqual(last_url, '/bag/')

## 4.iv. Validation testing:<a name="validation-testing"></a>
[Click here for Validation testing](readme/docs/validation_testing.md)

<br>

___
# 5. Deployment <a name="deployment"></a> 
[Click here for Deployment file](readme/docs/deployment.md)
<br>

___
# 6. Technologies used <a name="technology-used"></a>

## 6.i. Agile Methodology <a name="agile-methodology"></a>

For development of this webpage elements of Agile software development methodology have been used, including:

- User stories (described in User Stories section).
- Iterative and incremental development, utilizing cyclical flow of work in the areas mentioned below. An example of this might be adding a blog app after rough implementation and evaluating of products functionality, and then building on the above adding testimonials app. This flexible approach allowed to built on experience of building previous modules and avoid building unnecessary code. The process involves iterating through:
    - requirements
    - analysis and design
    - implementation
    - testing
    - evaluation
    - requirements
- Build, Measure, Learn approach.
- Utilizing Issues on GitHub. This mechanism was used to manage PBIs (Product Backlog Items) related to User stories, Ideas/Epics, Suggestions and Defects occurring all through the project life cycle. For managing work flow every PBI was given a label using MoSCoW technique:
    - Must-Have (for items which must be done within given iteration)
    - Should-Have (items preferably done but with lesser priority)
    - Could-Have (items only done as contingency or left for next iterations)
    - Won't-Have (items consciously abandoned)

    <details>
    <summary>Example Issues table used in this project</summary>
    General view
    
    ![screenshot](readme/docs/images/agile_kaizen.jpg)

    Issue label

    ![screenshot](readme/docs/images/agile_label.jpg)
    </details>

    Kanban for this project can also be found [here](https://github.com/users/KarMiles/projects/6/views/1).

## 6.ii. Languages <a name="languages"></a>

- HTML (https://www.w3schools.com/html/)
    - The main language this webpage's front-end is running on is HTML (HyperText Markup Language).
- CSS (https://www.w3.org/Style/CSS/)
    - For custom-made styling CSS (Cascading Style Sheets) language was used. This was along usage of CSS framework [Bootstrap](https://getbootstrap.com/).
- JavaScript (https://www.javascript.com/)
    - A limited use of custom-made JavaScript / JQuery has been employed to enhance functionality of the website.
- Python (https://www.python.org/) - within the Django framework Python 3 is the main language used to run its back-end logic. 

## 6.iii Frameworks and Libraries <a name="frameworks-and-libraries"></a>

### Frameworks and modules
- Django (https://www.djangoproject.com/)
    - This project was built with Django framework.
    - For testing Django unit test was utilized.

- Python packages

    The following packages are used for the project. Modules can be found in requirements.txt file:
    - asgiref==3.6.0
    - async-timeout==4.0.2
    - boto3==1.26.54
    - botocore==1.29.54
    - cloudinary==1.30.0
    - dj-database-url==0.5.0
    - Django==3.2
    - django-allauth==0.41.0
    - django-constance==2.9.1
    - django-contact-form==2.0.1
    - django-countries==7.5
    - django-crispy-forms==1.14.0
    - django-storages==1.13.2
    - django-summernote==0.8.20.0
    - gunicorn==20.1.0
    - jmespath==1.0.1
    - oauthlib==3.2.2
    - Pillow==9.3.0
    - psycopg2==2.9.5
    - python3-openid==3.2.0
    - pytz==2022.7
    - redis==4.5.1
    - requests-oauthlib==1.3.1
    - s3transfer==0.6.0
    - sqlparse==0.4.3
    - stripe==5.0.0
    - tzdata==2022.7


- Bootstrap (https://getbootstrap.com/) - used for consistent layout and responsiveness across all the website.

### Version management and deployment
- GitPod (https://gitpod.io/) - used as IDE and the tool for version control in the project.
- VSCode (https://code.visualstudio.com/) - interchangeably with Gitpod for local copy, speed on slow Internet connections and convenience in terms of managing files.
- GitHub (https://github.com/) - used to maintain repository of the project.
- Heroku (https://www.heroku.com) - used for deployment of the application.
- Stripe (https://stripe.com/docs) - used for management of e-commerce transactions

### Data storage
- SQLite (https://www.sqlite.org/) - used as a local database.
- Postgres (https://www.postgresql.org/) - the deployed project on Heroku uses the Postgres database on [ElephantSQL](https://www.elephantsql.com/) cloud service.
- AWS Amazon (https://aws.amazon.com/) - service added to deployment for hosting static and dynamic files.

### Design stages
- Lucidchart (www.lucidchart.com/) - used to create flowcharts.
- Balsamiq Wireframes(https://balsamiq.com/) - used to create wireframes in the UX design stage.
- SQL DRAW (https://drawsql.app/) – used to create database diagrams.
- Multi Device Website Mockup Generator (https://techsini.com/multi-mockup/) - Mockup Generator was used to create the Mock up image for this README document.
- [Ignore X-Frame headers](https://chrome.google.com/webstore/detail/ignore-x-frame-headers/gleekbfjekiniecknbkamfmkohkpodhe) Google Chrome Addon from [chrome web store](https://chrome.google.com/webstore/category/extensions) - to enable the Mockup Generator tool deal with X-Frame content security policy preventing the website from loading inside an iframe, embed or object of another website.

- Google Fonts (https://fonts.google.com/) - for selecting fonts and using them in the project.
- Font Awesome (https://fontawesome.com/) - all the icons throughout the website are derived from this service.
- Coolors.co (https://coolors.co/) - for generating colour palette for the website.
- SmallPDF (https://smallpdf.com/) - PDF to jpg file conversion.

### Validation
- HTML Markup Validation Service (https://validator.w3.org/) - for validating HTML code.
- CSS Validation Service (https://jigsaw.w3.org/css-validator/) - for validating CSS code.
- JSHint (https://jshint.com/) - for validating JavaScript code.
- CI Python Linter (https://pep8ci.herokuapp.com/) - for validating Python code.
- Unittest (https://docs.djangoproject.com/en/3.2/topics/testing/overview/) - for Python unit testing
- Google Chrome Developer Tools - built-in developer tools used to inspect page elements and help debug issues with the website functionality and layout.

### Marketing and SEO
- [Google Keyword Planner](https://ads.google.com/home/tools/keyword-planner/) - for selecting keywords.
- XML-Sitemaps (https://www.xml-sitemaps.com/) - for creating sitemaps.xml file.
- [Google Search Central](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap) - information on building and submitting a sitemap.
- [Search Console Central](https://support.google.com/webmasters/answer/7451001) - on managing a sitemap using the Sitemaps report.

### Python libraries
Third-party libraries were used for this project:
- request
    - request and response objects are used in Django to pass state through the system.
    - When a page is requested, Django creates an HttpRequest object that contains metadata about the request. Then Django loads the appropriate view, passing the HttpRequest as the first argument to the view function. Each view is responsible for returning an HttpResponse object.
- django
    - from django.apps import AppConfig - AppConfig represents an app for a Django project, including metadata such as name, label and path.
    - from django.contrib import admin - for managing functionality of the admin page.
    - from django import forms - used for Django forms
    - from django.contrib import messages - used for temporary on-screen messages.
    - from django.contrib.auth.models import User - for utilizing Django built-in User model functionality.
    - from django.db import models - for utilizing model structure.
    - from django.shortcuts import render - for rendering a page as a result of running a function.
    - from django.http import HttpResponseRedirect - for redirecting to a page in the process of running a function or a class.
    - from django.shortcuts import redirect - while in case of HttpResponseRedirect the first argument can only be a url, redirect can accept a model, view, or url as it's "to" argument. redirect will ultimately return a HttpResponseRedirect.
    - from django.shortcuts import get_object_or_404 - calls get() on a given model manager, but it raises Http404 instead of the model’s DoesNotExist exception.
    - from django.views import generic, View - generic class-based views designed to display data, in this project posts representing products.
    - from django.urls import path - returns an element for inclusion in urlpatterns.
    - from django.urls import include - function that takes a full Python import path to another URLconf module that should be “included” in this place. 
    - from django.urls import reverse_lazy, reverse - the reverse function allows to retrieve url details from urls.py files through the name provided in the path. reverse_lazy is useful for when there is a need to use a URL reversal before your project’s URLConf is loaded (success_url is then used).
    - from django.utils.text import slugify - used for utilizing slug functionality, slug is a short label for something, containing only letters, numbers, underscores or hyphens. They're generally used in URLs, as in this project. 
    - from django.views.generic import TemplateView - for rendering a given template, with the context containing parameters captured in the URL.
    - from django.conf.locale.en import formats as en_formats - for setting date and time formats where local format is not set.
    - from django_contact_form.views import ContactFormView - when utilizing a custom form class, used to manually set up URLs to tell django-contact-form about the form class.

Class-based views (CBV) provide a way to implement views as Python objects rather than functions.
CBV are predominantly, but not exclusively, used in this project for the following reasons:
- Code reusability - a view class can be inherited by another view class and modified in a different use case.
- DRY, which stands for 'don't repeat yourself' - CBV helps to reduce code duplication
- Code extendibility - CBV can be extended to include more functionalities using Mixins
- Code structuring - class based view helps to respond to different http request with different class instance methods instead of conditional branching statements inside a single function based view.
- Usage of built-in generic class-based views.

<br>

___
# 7. Credits <a name="credits"></a>

### Coding ideas, examples and tutorials
- [Code Institute](https://codeinstitute.net/) - this project was strongly enspired by the Institute's educational materials, especially Boutique Ado project.
- [Djangocentral](https://djangocentral.com/building-a-blog-application-with-django/) - blog setup ideas
- [Stackoverflow](https://stackoverflow.com/questions/13304149/what-the-difference-between-using-django-redirect-and-httpresponseredirect) - redirect, HttpResponseRedirect and as resource for addressing coding challenges during production process.
- [Stackoverflow](https://stackoverflow.com/questions/71886688/getting-attributeerror-testcase-object-has-no-attribute-asserttemplateused) - assertTemplateUsed for unittest.
- [Stackoverflow](https://stackoverflow.com/questions/224602/how-do-you-make-div-elements-display-inline/224626#224626) - inline version of div in html, by [Darryl Hein](https://stackoverflow.com/users/5441/darryl-hein)
- [Fullstackpython](https://www.fullstackpython.com/django-apps-config-appconfig-examples.html) - AppConfig description and other more general Python knowledge.
- [Djangoproject](https://docs.djangoproject.com/en/4.0/ref/models/fields/#field-types) - choices for priority levels.
- [Vegibit](https://vegibit.com/how-to-use-httpresponseredirect-in-django) - HttpResponse description.
- [Stackoverflow](https://stackoverflow.com/questions/22728763/how-to-provide-canonical-url-with-django-httpresponseredirect) - for best canonical link solution.
- [Stackoverflow](https://stackoverflow.com/questions/8852765/jshint-and-jquery-is-not-defined) - for JavaScript /JQuery false positives in [JSHint](https://jshint.com/). 

### Knowledge
- [Wikipedia](https://en.wikipedia.org/wiki/Sitemaps) - general information on sitemaps.

### Graphical content
- [Monika Curto Fuentes](https://www.instagram.com/polishgirlpainting/) - graphical representations of original art collection used for building this site.

    Note: Footer on this site is referring to the original artist's Instagram profile. This profile is not part of this project. 
- [Nicepng](https://www.nicepng.com) - favicon.
- [Coolors](https://coolors.co) - colour palette creation.
- [Font Awesome](https://fontawesome.com/) - sourcing icons.

### Other tools
- [Table to Markdown](https://tabletomarkdown.com/) - table conversion to Markdown.
- [TableConvert](https://tableconvert.com/excel-to-markdown) - table conversion to Markdown.
- [Mini Web Tool](https://miniwebtool.com/django-secret-key-generator/) - for generating secret keys

## Acknowledgements
I would like to thank everyone who contributed to development of this project, especially:
- The artist Monika Curto Fuentes for letting me use representations of her art collection and her very warm cooperation in carrying this project to its successful completion.
- My mentor Mo Shami for his invaluable guidance and advice.
- Educational Team at [Code Institute](https://codeinstitute.net/) for all educational materials and Tutor support which made this project possible. 
- All visual artists and coders who make products of their work available to others online.