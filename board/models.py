from django.db import models
from account.models import UserProfile


class Board(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    share = models.BooleanField(default=False)
    description = models.TextField(null=True)
    cover_img = models.ImageField(upload_to="board/covers", null=True)

    # pins = models.ManyToManyField('Pin')
    # categories = models.ManyToManyField('Category')
    collaborators = models.ManyToManyField('Collaborator')
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    """
        Other Relations:
        1. section: 1 to many (sections) // to be done in sections
        2. note: 1 to many (notes) // to be done in note
    """


class Collaborator(models.Model):
    user = models.ManyToManyField(UserProfile)
    is_super = models.BooleanField(default=False)
    can_invite = models.BooleanField(default=False)
