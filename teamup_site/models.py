from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils import timezone

from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail

from datetime import date
# Create your models here.

class Gender(models.TextChoices):
    MAN     = 'Man'
    WOMEN   = 'Women'
    OTHER   = 'Other'

class Work(models.TextChoices):
    SOFTWARE_ENGINEER       = 'Software Engineer'
    DESIGNER                = 'Designer'
    PLANNER                 = 'Planer'
    INFRASTRUCTURE_ENGINNER = 'Infrastructure Engineer'
    DATA_ENGINNER           = 'Data Engineer'

class CustomUser(AbstractUser, PermissionsMixin):
    username        = models.CharField(max_length=25)
    WORK_CHOICES    =[(w.value, w.name) for w in Work]
    your_job        = models.CharField(max_length=25, choices=WORK_CHOICES, default=Work.SOFTWARE_ENGINEER)
    GENDER_CHOICES  = [(g.value, g.name) for g in Gender]
    your_gender     = models.CharField(max_length=25, choices=GENDER_CHOICES, default=Gender.OTHER)
    birth_date      = models.DateField(blank=True, null=True,)

    def age(self):
        today = date.today()
        age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return age
    
    def __str__(self):
        return self.username
    
class workTag(models.Model):
    TagName = models.CharField(max_length=100)

class ProjectTags(models.Model):
    Ptags = models.CharField('tag', max_length=100)

    def __str__(self):
        return self.Ptags

class PostProject(models.Model):
    PPtitle = models.CharField(max_length=50) #プロジェクトタイトル
    PPcontext = models.TextField(max_length=2000) #プロジェクトコンテキスト
    PPimg = models.ImageField(upload_to='static/images') #プロジェクトイメージ
    PPuser = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True) #投稿ユーザー
    #like = models.ManyToManyField(User, related_name='', blank=True) #いいね
    PCworktag   = models.ManyToManyField(ProjectTags, verbose_name='tag') #プロジェクトタグ
    #PPviewCount = models.PositiveIntegerField(default=0) #閲覧数カウント
    created_at = models.DateTimeField(auto_now_add=True,) #投稿時刻

    def __str__(self):
        return self.PPtitle
