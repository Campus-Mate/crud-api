from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):
    board_id = models.CharField(max_length=15, unique=True)
    title = models.CharField(max_length=30)
    content = models.IntegerField()