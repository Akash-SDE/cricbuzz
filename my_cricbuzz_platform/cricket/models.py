from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _
from django.conf import settings
# Create your models here.

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    class Meta:
        db_table = 'auth_user'
        swappable = 'AUTH_USER_MODEL'
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='cricket_user_set',  # Change this to avoid clash
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='cricket_user_set',  # Change this to avoid clash
        related_query_name='user',
    )

class Team(models.Model):
    name = models.CharField(max_length=64, unique=True)
    logo_url = models.ImageField(upload_to='images/teams/')
    club_state = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class Player(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    image_url = models.ImageField(upload_to='images/players/', default='images/players/default_image.png')
    player_jersey_no = models.SmallIntegerField()
    Country = models.CharField(max_length=32) # Country should be foegin key to a new table.
    matches = models.IntegerField(default=0)
    run = models.IntegerField(default=0)
    highest_score = models.IntegerField(default=0)
    fifties = models.SmallIntegerField(default=0)
    hundreds = models.SmallIntegerField(default=0)

    def __str__(self):
        return "{} - {}".format(self.lastname, self.team.name)
    
    def get_fullname(self):
        return "{} {}".format(self.firstname, self.lastname)

class Match(models.Model):
    team1 = models.ForeignKey(Team, related_name='team1', on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team, related_name='team2', on_delete=models.CASCADE)
    date = models.DateField()
    result = models.CharField(max_length=100, blank=True, null=True)

class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image_url = models.URLField()

    def __str__(self):
        return self.title
    class Meta:
        verbose_name="News"
        verbose_name_plural = "News"

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username