from django.db import models
from django.contrib.auth.models import AbstractUser
from users.managers import CustomUserManager
import random
import string
from django.utils.text import slugify

# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    address = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    USERNAME_FIELD = 'email'  # Use email instead of username
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.email})"

class UserProfile(models.Model):
    slug = models.SlugField(max_length=60, unique=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    cover_photo = models.ImageField(upload_to='cover_photos/', null=True, blank=True)
    bio = models.TextField(max_length=250,null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(
        max_length=1,
        choices=[('M','Male'),('F','Female'),('O','Other')],
        null=True, blank=True
    )
    location = models.CharField(max_length=100, null=True, blank=True)
    SINGLE = 'Single'
    MARRIED = 'Married'
    RELATIONSHIP = 'In a Relationship'
    RELATIONSHIP_STATUS_CHOICES = [
        (SINGLE, 'Single'),
        (MARRIED, 'Married'),
        (RELATIONSHIP, 'In a Relationship'),
    ]
    relationship_status = models.CharField(max_length=20, choices=RELATIONSHIP_STATUS_CHOICES, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @staticmethod
    def generate_unique_slug(user):
        base_name = f"{user.first_name} {user.last_name}".strip()
        if not base_name:
            base_name = user.email.split("@")[0]
        
        base_slug = slugify(base_name)
        random_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        return f"{base_slug}-{random_suffix}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_unique_slug(self.user)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.email} Profile"

class UserStats(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_status')
    followers = models.PositiveIntegerField(default=0)
    following = models.PositiveIntegerField(default=0)
    posts = models.PositiveIntegerField(default=0)
    friends = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user.email} Stats"

class UserPrivacySettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='privacy_settings')
    profile_visibility = models.CharField(
        choices=[('PUBLIC','Public'),('PRIVATE','Private')],
        default="PUBLIC"
    )
    show_email = models.BooleanField(default=True)
    show_phone = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.email} Privacy"

class WorkExperience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='work_experience')
    company = models.CharField(max_length=200, null=True, blank=True)
    position = models.CharField(max_length=100, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.email} - {self.position} at {self.company}"

class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='education')
    school = models.CharField(max_length=200, null=True, blank=True)
    degree = models.CharField(max_length=100, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.email} - {self.degree} at {self.school}"
