import textwrap
from datetime import timedelta

# Create a super user to use the admin site.
from django.contrib.auth.models import User
from discourz_app.models import Account, PollTopic

username = "discourz404"
password = "discourz404"
email = "admin@326.edu"
adminuser = User.objects.create_user(username, email, password)
adminuser.save()
adminuser.is_superuser = True
adminuser.is_staff = True
adminuser.save()

admin = Account.objects.all()

polls = [
    PollTopic(title="Example Poll 1", options="option1,option2,option3", votes="0,0,0", owner=admin[0]),
    PollTopic(title="What is the best dining common in UMass?", options="Worcester,Franklin,Hampshire,Berkshire", votes="0,0,0,0", owner=admin[0], img="static/img/umass.jpg"),
    PollTopic(title="Which is the most difficult CompSci course?", options="220,230,240,250", votes="0,0,0,0", owner=admin[0], img="static/img/school.jpg"),
]

for poll in polls:
  poll.save()


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
