from tabnanny import verbose
from django.db import models
from geography.models import ZipCode

class Reporter(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name

class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    
class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

class Customer(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    # 이때는 verbose field name이 person's first name
    first_name = models.CharField("person's first name", max_length=30)
    # 이때는 first name
    first_name = models.CharField(max_length=30)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
    
class Runner(models.Model):
    MedalType = models.TextChoices('MedalType', 'Gold Silver Bronze')
    name = models.CharField(max_length=60)
    medal = models.CharField(blank=True, choices=MedalType.choices, max_length=10)
    
class Fruit(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

class Manufacturer(models.Model):
    pass
class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    

class Topping(models.Model):
    pass
class Pizza(models.Model):
    toppings = models.ManyToManyField(Topping)
    
class Person(models.Model):
    name = models.CharField(max_length=128)
    def __str__(self):
        return self.name
class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')
    def __str__(self):
        return self.name
class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)
    
 
class Restaurant(models.Model):
    zip_code = models.ForeignKey(
        ZipCode, 
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True,
    )

class Ox(models.Model):
    horn_length = models.IntegerField()
    class Meta:
        ordering = ["horn_length"]
        verbose_name_plural = "oxen"