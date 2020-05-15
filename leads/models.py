from django.db import models

class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

class Project(models.Model):
  project_name = models.CharField(max_length=100)
  description = models.CharField(max_length=500)
  created_at = models.DateTimeField(auto_now_add=True)