from django.db import models
from django.contrib.auth.models import AbstractUser, Group

class User(AbstractUser):
    email = models.EmailField(unique=True)
    # Add more fields if needed

    class Meta:
        # Any meta options you need
        pass

    groups = models.ManyToManyField(
        Group,  # Make sure to import Group from django.contrib.auth.models
        verbose_name='groups',
        blank=True,
        related_name='custom_user_set',  # Change this related_name
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='custom_user_set',  # Change this related_name
        related_query_name='user',
    )

class Story(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # Add more fields if needed

class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}: {self.message}'