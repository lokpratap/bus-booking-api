from django.db import models
# from django.contrib.auth.models import  AbstractUser

# class UserManager(BaseUserManager):
#     def create_user(self,email,password=None):
#         if not email:
#             raise ValueError("Users must have email address")
#         user = self.model(
#             email = self.normalize_email(email)
#         )
#         user.set_password(password)
#
#         user.save(using=self._db)
#         return user

#
# class User(AbstractUser):
#     name = models.CharField(max_length=255)
#     def __str__(self):
#         return self.email
#

#     USERNAME_FIELD = 'email'
#
#     GENDER_CHOICES = (
#         ('M', 'Male'),
#         ('F', 'Female'),
#     )
#     gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
#
#     class Meta:
#         verbose_name_plural = "bus_app"
#
#         def __string__(self):
#             return self.email
#
#
#
class Posts(models.Model):
    email = models.EmailField(max_length=255)
    phone = models.IntegerField()
    city = models.CharField(max_length=255)
    dob = models.DateField(max_length=8)

    class Meta:
        verbose_name_plural = "bus_app"
        def __string__(self):
            return self.email

