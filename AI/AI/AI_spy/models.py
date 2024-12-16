from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


FILE_TYPE_CHOICES = [
    ('asm', 'ASM File'),
    ('c', 'C Source File'),
    ('python', 'Python Script'),
    ('txt', 'Text Document'),
]
# Create your models here.
class WebShellcode(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    file_type = models.CharField(max_length=10, choices=FILE_TYPE_CHOICES)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    analysis_result = models.TextField(null=True, blank=True) #####설명본 추가

    class Meta:
        db_table = 'web'

class LinuxShellcode(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    file_type = models.CharField(max_length=10, choices=FILE_TYPE_CHOICES)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    analysis_result = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'linux'

class WindowsShellcode(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    file_type = models.CharField(max_length=10, choices=FILE_TYPE_CHOICES)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    analysis_result = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'windows'