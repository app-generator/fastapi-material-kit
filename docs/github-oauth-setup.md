## Stripe OAuth Setup


👉First, we need to `create an oauth app` in github, then get `2 particular credentials` from Github, and lastly configure the app with our homepage url and login url. 
1. create an oauth appliaction > https://github.com/settings/apps
2. client_id
3. create a secret key, copy it for use later (it will be inaccessible after so-many minutes, make sure to copy it at the first chance)
4. Fill in the homepage url (http://localhost:8000/), and the authorizaton callback url (http:localhost:8000) in the form field.


👉Second, we need to set our environment variables to use our github credentials. Open the .env file that you should have created during the initial setup (README.md for details) and set the appropriate variables.


👉 Third, now both the app and github are setup. You can now register via Github oauth.


👉 Fourth, run the application (refer to README.md). You can now do the following: 

1. Visit the page `/auth/github_login`.
2. You will be redirected to Github, login (! note that this step is automatically skipped if you've recently loggd into github).
3. After logging in, you will be redirected back to the specificed url (likely localhost:8000/).
4. You will now have your access code stored as a cookie named `github-Account`.
5. You will now be able to access your user data by visiting `/auth/user`, which will return a json object.
6. Log out by visiting `auth/logout`.


