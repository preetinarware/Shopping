from django.db import models

# Create your models here.

class enquiries(models.Model):
        name = models.CharField(max_length=20)
        email = models.EmailField(max_length=20)
        contact_no= models.IntegerField()
        subject = models.CharField(max_length=20)
        your_ques = models.CharField(max_length=100)

        def __str__(self):
                return self.name
class More_Products(models.Model):
    name = models.CharField(max_length=10)
    img = models.ImageField()
    price = models.IntegerField()
    rate = models.IntegerField()
    desc = models.TextField(max_length=100)
    field_names=models.CharField(max_length=15)
    head1=models.TextField(max_length=30)
    head2=models.TextField(max_length=30)

    def __str__(self):
        return self.name

class mycart(models.Model):
    user = models.CharField(max_length=10)
    product_id = models.IntegerField()
    quntity = models.IntegerField()

    def __str__(self):
        return self.user

class Oders(models.Model):
    name=models.CharField(max_length=10)
    contact_no = models.IntegerField()
    addres1=models.TextField()
    addres2 = models.TextField()
    pincode= models.IntegerField()
    product_name= models.CharField(max_length=100)
    time=models.DateTimeField(auto_now=True)
    total=models.IntegerField(default=0)
    quntitys=models.IntegerField(default=0)
    prodid=models.IntegerField(default=0)
    price = models.IntegerField(default=0)


    def __str__(self):
          return  self.name + (self.product_name)


class abouts(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField(max_length=550)
    def __str__(self):
          return self.title

class Book_testdrive(models.Model):
    name=models.CharField(max_length=15)
    email=models.EmailField(max_length=20)
    contact_no=models.IntegerField(max_length=50)
    Bike_model=models.IntegerField(max_length=10)
    Addres=models.TextField(max_length=50)
    zipcode=models.IntegerField(max_length=10)
    your_question=models.TextField(max_length=50)

    def __str__(self):
        return self.name

class product_access(models.Model):

    field_name=models.CharField(max_length=15)
    prod_id=models.IntegerField(max_length=5)
    h1=models.TextField(max_length=30)
    h2 = models.TextField(max_length=30)
    h3=models.TextField(max_length=30)
    h4=models.TextField(max_length=30)
    h5=models.TextField(max_length=30)
    h6=models.TextField(max_length=30)
    h7=models.TextField(max_length=30)

    def __str__(self):
        return self.field_name

class product_specif(models.Model):
    field_names = models.CharField(max_length=15)
    prod_id = models.IntegerField(max_length=5)
    h1 = models.TextField(max_length=30)
    h2 = models.TextField(max_length=30)
    h3 = models.TextField(max_length=30)
    h4 = models.TextField(max_length=30)
    h5 = models.TextField(max_length=30)
    h6 = models.TextField(max_length=30)
    h7 = models.TextField(max_length=30)

    def __str__(self):
        return self.field_names

class product_key(models.Model):
    field_namess = models.CharField(max_length=15)
    prod_id = models.IntegerField(max_length=5)
    h1 = models.TextField(max_length=30)
    h2 = models.TextField(max_length=30)
    h3 = models.TextField(max_length=30)
    h4 = models.TextField(max_length=30)
    h5 = models.TextField(max_length=30)
    h6 = models.TextField(max_length=30)
    h7 = models.TextField(max_length=30)

    def __str__(self):
        return self.field_namess

class profile(models.Model):
    user_ids =models.IntegerField(max_length=10)
    username=models.CharField(max_length=20)
    image=models.ImageField()
    gender = models.CharField(max_length=15)
    contact = models.IntegerField(max_length=10)
    Current_add = models.TextField(max_length=50)
    Permanant_add = models.TextField(max_length=50)
    DOB = models.DateField()
    def __str__(self):
        return self.username


