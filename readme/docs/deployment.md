# Deployment

[Click here for Readme file](/README.md#deployment)

Creation of the functioning application was carried in stages:
- coding on [Gitpod](https://www.gitpod.io/) and Microsoft [Visual Studio Code](https://code.visualstudio.com/), with [GitHub](https://github.com/) repository,
- deployment on [Heroku](https://www.heroku.com/), PostresSQL-as-a-service - based cloud platform, 
- creation of external PostgreSQL database on [ElephantSQL](https://www.elephantsql.com/),
- setting up hosting for the static and media files with [Amazon Web Services](https://aws.amazon.com/)  S3 (Simple Storage Service).

## GitHub

The site was built using GitHub repository. GitHub clone and GitHub branch methods could be used although were not needed for this project.

Repository may be forked in the following steps:
1. Go to GitHub repository,
2. Click Fork button (top right).

Steps for cloning repository:
1. Go to GitHub repository,
2. Click Code button (top right above files list),
3. Select cloning method option: HTTPS, SSH or GitHub CLI and click Copy button (right side of the text box) to copy URL to clipboard,
4. Open Git Bash (Git Bash can be downloaded from https://git-scm.com/downloads),
5. In Git Bash change working directory to the desired destination for the clone,
6. Type "git clone", paste URL for SSH method from the clipboard and press Enter.

During part of production process both [GitPod](https://gitpod.io/) and the program [Visual Studio Code](https://code.visualstudio.com) were used. The latter was not strictly necessary but provided smoother production in times of poor Internet connection and provided extra level of assurance in form of local copy of all files.


## ElephantSQL

Instantiation of PostgreSQL databases required the following steps:

1. Create an account on [ElephantSQL](https://www.elephantsql.com/) and click "Create a managed database today.

    <details>
    <summary>Click here to see screenshot</summary>

    ![screenshot](./images/deployment/elephantsql/elephantsql_1_create_account.jpg)
    </details>

2. Select TINY TURTLE database plan by clicking "Try now for FREE" button.

    <details>
    <summary>Click here to see screenshot</summary>

    ![screenshot](./images/deployment/elephantsql/elephantsql_2_select_plan.jpg)
    </details>

3. Select “Sign in with GitHub” and authorize ElephantSQL with your selected GitHub account.

    <details>
    <summary>Click here to see screenshot</summary>

    ![screenshot](./images/deployment/elephantsql/elephantsql_3_sign_in.jpg)
    </details>

4. Select “Sign in with GitHub” and authorize ElephantSQL with your selected GitHub account. Verification by code sent by email may be required.

    <details>
    <summary>Click here to see screenshot</summary>

    ![screenshot](./images/deployment/elephantsql/elephantsql_4_sign_in.jpg)
    </details>

5. In "Create new instance" section setup details of your account:
    - Select a plan and name,
    - Select region,
    - confirm.

    <details>
    <summary>Click here to see screenshots</summary>

    Select a plan and name:

    ![screenshot](./images/deployment/elephantsql/elephantsql_5_setup_name.jpg)

    Select region:

    ![screenshot](./images/deployment/elephantsql/elephantsql_5a_region.jpg)

    Confirm:

    ![screenshot](./images/deployment/elephantsql/elephantsql_5b_confirm.jpg)
    </details>

6. After creation of the instance it is shown on the list of available instances. Clicking on the name redirects user to details, returning to editing the instance is possible after clicking on Edit button.

    <details>
    <summary>Click here to see screenshot</summary>

    ![screenshot](./images/deployment/elephantsql/elephantsql_6_list.jpg)
    </details>

7. In Details section information like URL and API key necessary for setting up the connection can be found.

    <details>
    <summary>Click here to see screenshot</summary>

    ![screenshot](./images/deployment/elephantsql/elephantsql_7_details.jpg)
    </details>

## Project preparation for Gitpod

With:
- the database instantiated in ElephantSQL and 
- app created on Heroku 

it was possible to set up this project to:
- connect to the ElephantSQL database, 
- create database tables by running migrations, 
- add shops fixtures, and 
- confirm that it all works by creating a superuser.

**Gitpod**

While in Gitpod the bellow steps were followed:

1. In the terminal, install dj_database_url and psycopg2, both of these are needed to connect to the external database (`pip` instead of `pip3` is used on [VSCode](https://code.visualstudio.com/)):
    ```
    pip3 install dj_database_url==0.5.0 psycopg2
    ```
2. Update  requirements.txt file with the newly installed packages:
    ```
    pip3 freeze > requirements.txt
    ```
3. In settings.py file, import dj_database_url underneath the import for os:
    ```
    import os
    import dj_database_url
    ```
4. Update the DATABASES to the following code, so that the original connection to sqlite3 is commented out and we connect to the new ElephantSQL database instead. Paste in your ElephantSQL database URL in the position indicated
    ```
    # DATABASES = {
    #     'default': {
    #         'ENGINE': 'django.db.backends.sqlite3',
    #         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    #     }
    # }
            
    DATABASES = {
        'default': dj_database_url.parse('database-url-here')
    }
    ```

    The settings.py file was not committed with this database string in the code to avoid leaving database URL in version control. It was a temporary solution so that I could connect to the new database and make migrations. This setting was removed thereafter.

5. In the terminal, run the showmigrations command to confirm you are connected to the external database:
    ```
    python3 manage.py showmigrations
    ```
    If you are, a list of all migrations should appear, but none of them checked off.

6. Migrate your database models to your new database
    ```
    python3 manage.py migrate
    ```
7. Load in the fixtures. The order is very important here. Categories need to be loaded first, only then products.
    ```
    python3 manage.py loaddata categories
    python3 manage.py loaddata products
    ```
8. Create a superuser for the new database
    ```
    python3 manage.py createsuperuser
    ```
9.  To prevent exposing the database when pushing to GitHub, delete it again from the settings.py file. The temporary setting for the database is as below. The eventual setting for the database is as described in the Configuration variables section of this document.
    ```
     DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
    ```

**ElephantSQL**

Confirming migrations

Next step was to confirm that the data in my database on ElephantSQL has been created. This was done in the following steps:

1. On the ElephantSQL page for the chosen database (shown on top of the page), in the left side navigation, select BROWSER.

    <details>
    <summary>Click here to see screenshot</summary>

    ![screenshot](./images/deployment/elephantsql/elephantsql_8_browser.jpg)
    </details>

2. Click the Table queries button, select auth_user.

    <details>
    <summary>Click here to see screenshot</summary>

    ![screenshot](./images/deployment/elephantsql/elephantsql_9_auth_user.jpg)
    </details>

3. When clicked “Execute”, newly created superuser details displayed (and other users if this is done in further stages of the project). This confirms the tables have been created and you can add data to your database.

    Execute:
    <details>
    <summary>Click here to see screenshot</summary>

    ![screenshot](./images/deployment/elephantsql/elephantsql_10_execute.jpg)
    </details>

    Result:
    <details>
    <summary>Click here to see screenshot</summary>

    ![screenshot](./images/deployment/elephantsql/elephantsql_11_success.jpg)
    </details>


## Heroku

**Heroku**

This application is deployed from GitHub using Heroku in following steps:

1. Create an account at [Heroku](https://id.heroku.com/).

    <details>
    <summary>Click here to see screenshot</summary>

    ![screenshot](./images/deployment/heroku/heroku_signup.jpg)
    </details>

2. Create new app by clicking "New" and then "Create new app".

    <details>
    <summary>Click here to see screenshot</summary>

    ![screenshot](./images/deployment/heroku/heroku_create_new_app.jpg)
    </details>

3. Add app name and region and click on "Create app".

    <details>
    <summary>Click here to see screenshot</summary>

    ![screenshot](./images/deployment/heroku/heroku_create_name_region.jpg)
    </details>

4. Choose "Settings".

    <details>
    <summary>Click here to see screenshot</summary>

    ![screenshot](./images/deployment/heroku/heroku_settings.jpg)
    </details>

5. Under "Config Vars" add credentials, e.g. creds.json, secret key.

    <details>
    <summary>Click here to see screenshot</summary>

    ![screenshot](./images/deployment/heroku/heroku_config_vars.jpg)
    </details>

6. Set buildpacks by selecting "Add buildpacks" (I then chose "Python") and "Save changes".

    <details>
    <summary>Click here to see screenshot</summary>

    ![screenshot](./images/deployment/heroku/heroku_buildpacks.jpg)
    </details>

7. Go to "Deploy", at "Deployment method" click "Connect to GitHub" and confirm.

    <details>
    <summary>Click here to see screenshot</summary>

    ![screenshot](./images/deployment/heroku/heroku_deploy.jpg)
    </details>

8. Enter repository name, click on it when it appears below.

    <details>
    <summary>Click here to see screenshot</summary>

    ![screenshot](./images/deployment/heroku/heroku_connect_repo.jpg)
    </details>

9. Select the branch for building the app.

    <details>
    <summary>Click here to see screenshot</summary>

    ![screenshot](./images/deployment/heroku/heroku_branch.jpg)
    </details>

10. Clicking "Enable Automatic Deploys" will keep the app updated with GitHub repository. This feature was used for this project.

    <details>
    <summary>Click here to see screenshot</summary>

    ![screenshot](./images/deployment/heroku/heroku_automatic.jpg)
    </details>

**Gitpod**

The following setup was made in Gitpod:

1. In settings.py file the following configuration allows for automatic use of appropriate database on Heroku (where DATABASE_URL variable is present) and outside of it:

    ```
    if 'DATABASE_URL' in os.environ:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        }
    ```
2. Install [gunicorn](https://gunicorn.org/) which is a Python WSGI HTTP Server for UNIX and update the requirements.txt file:
    ```
    pip3 install gunicorn
    pip3 freeze > requirements.txt
    ```
3. Create Procfile in the main directory, with the content as cited below. This tells Heroku to create a web dyno which will run gunicorn and serve our Django app:
    ```
    web: gunicorn pgp_project.wsgi:application
    ```
4. Temporarily disable COLLECTSTATIC on Heroku, it can be done by logging in to Heroku with `heroku login` command in Gitpod Terminal. This prevents Heroku from collecting static files when we deploy.
    ```
    heroku config:set DISABLE_COLLECTSTATIC=1 --app heroku-pgp-project
    ```
    note: "heroku-pgp-project" is my app on Heroku for this project.
5. Add host name of the Heroku app in settings.py:
    ```
    ALLOWED_HOSTS = ['heroku-pgp-project.herokuapp.com', 'localhost', '127.0.0.1']
    ```
    In this case the first host is for Heroku, second for Gitpod and third for VSCode.
6. Pushing to Github and Heroku should complete the deployment to Heroku. Pushing to Heroku can be done with commands below, automatic deploys are also possible if this option is activated on Heroku. 
    ```
    git add .
    git commit -m "Commit text"
    heroku git:remote -a heroku-pgp-project
    git push heroku main
7. Secure connections with secret keys:
    - Generate secret keys for Github and Heroku to be used only on this project. In this case [Mini Web Tool](https://miniwebtool.com/django-secret-key-generator/) was used. 
    - Add a secret key to Config Vars in Heroku
        ![screenshot](./images/deployment/heroku/heroku_secret_key.jpg)
    - Add a secret key to env.py:
        ```
        os.environ["SECRET_KEY"] = '<secret key>'
        ```
    - Address the secret key sitting in env.py in settings.py:
      ```
      SECRET_KEY = os.environ.get('SECRET_KEY', '')
      ```
8. Set DEBUG in settings.py so it only is True if the DEBUG variable is in environment.  
    ```
    DEBUG = os.environ.get('DEBUG', '1') == '1'
    ```




## Configuration variables

Config Vars and coresponding keys in project files for this project:

| Config Vars in Heroku                         | env.py                                            | settings.py                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| --------------------------------------------- | ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *General*                                       |                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| DEBUG = 0                                     | os.environ["DEBUG"] = "1"                         | DEBUG = os.environ.get('DEBUG', '1') == '1'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                               | os.environ["DEVELOPMENT"] = "1"                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| SECRET_KEY = \<access key>                     | os.environ["SECRET_KEY"] = '<secret key>'         | SECRET_KEY = os.environ.get('SECRET_KEY', '')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| *Databases*                                     |                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| DATABASE_URL = postgres://…                   | os.environ["DATABASE_URL"] = 'postgres://...'     | DATABASES = {<br>    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))<br>}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| HEROKU_POSTGRESQL_MAROON_URL = postgres://... |                                                   |
| AWS_ACCESS_KEY_ID = \<access key>              |                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| AWS_SECRET_ACCESS_KEY = \<access key>          |                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| USE_AWS = True                                |                                                   | if 'USE_AWS' in os.environ:<br>    # Cache control<br>    AWS_S3_OBJECT_PARAMETERS = {<br>        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',<br>        'CacheControl': 'max-age=94608000',<br>    }<br><br>    # Bucket Config<br>    AWS_STORAGE_BUCKET_NAME = 'aws-pgp-project'<br>    AWS_S3_REGION_NAME = 'eu-west-1'<br>    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')<br>    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')<br>    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'<br><br>    # Static and media files<br>    STATICFILES_STORAGE = 'custom_storages.StaticStorage'<br>    STATICFILES_LOCATION = 'static'<br>    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'<br>    MEDIAFILES_LOCATION = 'media'<br><br>    # Override static and media URLs in production<br>    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'<br>    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/' |
| *E-commerce*                                    |                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| STRIPE_PUBLIC_KEY = pk_test_...               | os.environ["STRIPE_PUBLIC_KEY"] = 'pk_test_...'   | STRIPE_PUBLIC_KEY = os.environ.get('STRIPE_PUBLIC_KEY', '')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| STRIPE_SECRET_KEY = sk_test_...               | os.environ["STRIPE_SECRET_KEY"] = 'sk_test_...'   | STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY', '')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| STRIPE_WH_SECRET = whsec_...                  | os.environ["STRIPE_WH_SECRET"] = 'whsec_...'      | STRIPE_WH_SECRET = os.environ.get('STRIPE_WH_SECRET', '')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| *Email*                                         |                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| EMAIL_HOST_PASSWORD = \<password>              | os.environ["EMAIL_HOST_PASSWORD"] = "\<password>"  | if 'DEVELOPMENT' in os.environ:<br>    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'<br>    DEFAULT_FROM_EMAIL = 'monikacurtofuentes@monikaexample.com'<br>else:<br>    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'<br>    EMAIL_USE_TLS = True<br>    EMAIL_PORT = 587<br>    EMAIL_HOST = 'smtp.gmail.com'<br>    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')<br>    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')<br>    DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| EMAIL_HOST_USER = \<email address>             | os.environ["EMAIL_HOST_USER"] = "\<email address>" |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| DEFAULT_FROM_EMAIL = \<email address>          |                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
