import textwrap
from datetime import timedelta

# Create a super user to use the admin site.
from django.contrib.auth.models import User
from discourz_app.models import Account

#accounts = [
#  Account(username="alexsun", password="12345", email="alexsun@umass.edu", bio="alex's bio"),
#  Account(username="psaetang", password="12345", email="psaetang@umass.edu", bio="prakrit's bio")
#]


# Save the genres to the database
#for account in accounts:
#    account.save()

username = "discourz404"
password = "discourz404"
email = "admin@326.edu"
adminuser = User.objects.create_user(username, email, password)
adminuser.save()
adminuser.is_superuser = True
adminuser.is_staff = True
adminuser.save()
message = f"""
====================================================================
The database has been setup with the following credentials:

  username: {username}
  password: {password}
  email: {email}

You will need to use the username {username} and password {password}
to login to the administrative webapp in Django.

Please visit http://localhost:8080/admin to login to the admin app.
Run the django server with:

  $ python3 manage.py runserver 0.0.0.0:8080"
====================================================================
"""
print(message)
