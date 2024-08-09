from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission #User
from django.conf import settings



# Once you’ve defined your model, you need to create the corresponding database table. 
# python manage.py makemigrations 
# python manage.py migrate


#Django has a built in User so there is conflict. Cant register and login is weird
class User(AbstractUser):
    CUSTOMER = 'customer'
    STAFF = 'staff'
    MANAGER = 'manager'
    ADMIN = 'admin'
    
    ROLE_CHOICES = [
        (CUSTOMER, 'Customer'),
        (STAFF, 'Staff'),
        (MANAGER, 'Manager'),
        (ADMIN, 'Admin'),
    ]
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=CUSTOMER)
    groups = models.ManyToManyField(Group, related_name='api_user_set')
    user_permissions = models.ManyToManyField(Permission, related_name='api_user_permissions_set')

class Product(models.Model):
    VEGETABLES = 'Vegetable'
    MEAT = 'Meat'
    DAIRY = 'Dairy'
    OTHER = 'Other'

    CATEGORY_CHOICES = [
        (VEGETABLES, 'Vegetable'),
        (MEAT, 'Meat'),
        (DAIRY, 'Dairy'),
        (OTHER, 'Other'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default=OTHER,
    )
    posted_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,  # If the user is deleted, the product's owner is set to null
        null=True,  # Allows the owner to be null (no owner)
        blank=True,  # Allows the owner field to be left blank in forms
        related_name='products'
    )

    def __str__(self):
        return self.name
        
'''class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")

    def __str__(self):
        return self.title'''
