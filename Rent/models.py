from django.db import models
from UserApp.models import UserModel
from django.contrib.auth.models import User

class Location(models.Model):
    location = models.CharField(max_length = 30)
    slug = models.SlugField(max_length = 40)

    def __str__(self):
        return self.location
    
class HouseType(models.Model):
    type = models.CharField(max_length = 30)
    slug = models.SlugField(max_length = 40)

    def __str__(self):
        return self.type


class House(models.Model):
    image = models.ImageField(upload_to="media/house/")
    title = models.CharField(max_length=200)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, default=1)
    house_type = models.ForeignKey(HouseType, on_delete=models.CASCADE, default=1)
    rental_price = models.IntegerField()
    description = models.TextField()
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='houses',null=True)
    rented = models.BooleanField(default=False)

    def __str__(self):
        return self.title


STAR_CHOICES = [
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
]

class Review(models.Model):
    reviewer = models.ForeignKey(UserModel, on_delete = models.CASCADE)
    house = models.ForeignKey(House, on_delete = models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    rating = models.CharField(choices = STAR_CHOICES, max_length = 10)
    
    def __str__(self):
        return f"User : {self.reviewer.user.first_name} ; House-title : {self.house.title}"
    

RENT_STATUS = [
    ('Accepted', 'Accepted'),
    ('Pending', 'Pending'),
]

class RentHouse(models.Model):
    user = models.ForeignKey(UserModel, on_delete = models.CASCADE)
    house = models.ForeignKey(House, on_delete = models.CASCADE)
    rent_status = models.CharField(choices = RENT_STATUS, max_length = 10, default = "Pending")
    rent_date = models.DateField(auto_now_add = True)
    cancel = models.BooleanField(default = False)
    
    def __str__(self):
        return f"House : {self.house.title} , Buyer : {self.user.user.first_name}"