from django.db import models

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.username, filename)

# Create your models here.
class Account(models.Model):
    username = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=20)
    email = models.EmailField()
    img = models.ImageField(upload_to=user_directory_path)
    bio = models.TextField(max_length=500)

    def __str__(self):
        return self.username