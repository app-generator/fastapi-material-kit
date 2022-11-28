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
3. You will be redirected back to the specificed url (likely localhost:8000/).
4. You should now have your access code

<!-- NOTE TO THE DEVELOPER -->

Step 4 is where things don't go as planned. I have written out the issue int he auth_routes.py file (lines 38+), commented out.

I'm following those docs. I cant't make a post request. 
https://docs.github.com/en/developers/apps/building-oauth-apps/authorizing-oauth-apps

This what we should recieve after a successful post request. Write this as a cookie upon redirect and we're all set. It's the same procedure as our previous project. Upon logout, clear the cookies.

Should be response (example data):
access_token=gho_16C7e42F292c6912E7710c838347Ae178B4a&scope=repo%2Cgist&token_type=bearer


