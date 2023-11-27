from django.db import models

#-カスタムユーザモデルの作成------------------------------------------------
from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser):
    pass