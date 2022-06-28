from django.db import models

class Users(models.Model):
    email = models.CharField(max_length = 200, null = False, blank = False)
    username = models.CharField(max_length = 30, null = False, blank = False)
    password = models.CharField(max_length = 255, null = False, blank = False)

    objects = models.Manager()

class Urls(models.Model):
    url = models.CharField(max_length = 200, null = False, blank = False)
    name = models.CharField(max_length = 100, null = False, blank = False, primary_key = True)
    user = models.ForeignKey(Users, on_delete = models.CASCADE, null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = models.Manager()