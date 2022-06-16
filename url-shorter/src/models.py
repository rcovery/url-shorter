from django.db import models

class Users(models.Model):
    email = models.CharField(max_length = 200, null = False, blank = False)
    username = models.CharField(max_length = 30, null = False, blank = False)
    password = models.CharField(max_length = 255, null = False, blank = False)

    object = models.Manager()

class Url(models.Model):
    url = models.CharField(max_length = 200, null = False, blank = False)
    short_url = models.CharField(max_length = 100, null = False, blank = False)
    user = models.ForeignKey(Users, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    object = models.Manager()