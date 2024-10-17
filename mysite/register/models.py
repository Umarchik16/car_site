from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser



class UserProfile(AbstractUser):
    age = models.PositiveSmallIntegerField(default=0, null=True, blank=True,
                                           validators=[MinValueValidator(18), MaxValueValidator(100)])
    phone_number = PhoneNumberField(null=True, blank=True, region='KG')
    password = models.CharField(max_length=100)
    date_register = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

class Category(models.Model):
    category_name = models.CharField(max_length=50 , unique=True)



    def __str__(self):
        return self.category_name

class Car(models.Model):
    car_name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='category_car')
    description = models.TextField(null=True, blank=True)
    price = models.PositiveIntegerField(default=0)
    colors = models.CharField(max_length=50 , null=True, blank=True)
    TRAN_CHOICES = (
        ('avto', 'avto'),
        ('mechanics', 'mechanics'),
        ('semi-automatic' , 'semi-automatic')
    )
    transmission = models.CharField(max_length=15, verbose_name='каробка передач',choices=TRAN_CHOICES)#каробка передач

    acceleration = models.DecimalField(max_digits=6,verbose_name = 'ускарения', decimal_places=2, choices=[(i, str(i)) for i in range(1,6) ])#ускорения
    ENGINE_CHOICES = (
        ('petrol' , 'petrol'),
        ('diesel','diesel'),
        ('gas','gas'),
        ('electorate' , 'electorate'),
    )

    engine = models.CharField(max_length=50 , choices=ENGINE_CHOICES , verbose_name='вид топлива')#двигатель х.хл/бензин
    region = models.CharField(max_length=50)
    payment_method = models.CharField(max_length=50, null=True, blank=True)# способ оплаты
    STEERING_CHOICES = (
        ('left','left'),
        ('right','right'),
    )
    steering= models.CharField(max_length=50, choices=STEERING_CHOICES)# рулевое управления
    video = models.ImageField(upload_to="videos/")
    owner = models.ForeignKey(UserProfile,on_delete=models.CASCADE)

    def __str__(self):
        return self.car_name

class CarPhotos(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/", null=True, blank=True)





class Rating(models.Model):
    product = models.ForeignKey(Car,related_name='ratings', on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile,  on_delete=models.CASCADE)
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1,6) ], verbose_name='оценка')

    def __str__(self):
        return f'{self.user} - {self.product} - {self.stars} stars'

class Review(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Car, related_name='reviews',on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    parent_review = models.ForeignKey('self', related_name='replies', null=True, blank=True, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.author} - {self.text}'




