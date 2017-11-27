from django.db import models

# Create your models here.
class BankDetails(models.Model):
    accNo = models.IntegerField(primary_key=True)
    bankName = models.CharField(max_length=50)
    branchName = models.CharField(max_length=50)
    ifsc = models.CharField(max_length=16)
    def __str__(self):
        return self.bankName



class Users(models.Model):
    userEmail = models.EmailField(max_length=100, primary_key=True)
    password = models.CharField(max_length=150)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)
    userType = models.CharField(max_length=13)
    accNo = models.ForeignKey(BankDetails, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=10, default='active')

    def __str__(self):
        return self.name



class BlogDetails(models.Model):
    blogId = models.CharField(max_length=15, primary_key=True)
    userEmail = models.ForeignKey(Users)
    url = models.URLField()
    type = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    class Meta:
        unique_together = (('blogId', 'userEmail'))


class Category(models.Model):
    category = models.CharField(max_length=50, unique= True)
    def __str__(self):
        return self.category


class MediaType(models.Model):
    mediaType = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.mediaType


class AdDetails(models.Model):
    adId = models.CharField(max_length=11, primary_key=True)
    category = models.ForeignKey(Category)
    adTitle = models.CharField(max_length=50)
    adDescription = models.CharField(max_length=200)
    mediaLink = models.ImageField(upload_to='media/images/')
    mediaType = models.ForeignKey(MediaType)


class Price(models.Model):
    mediaType = models.ForeignKey(MediaType)
    price = models.DecimalField(max_digits=8, decimal_places=2)


class Advertisement(models.Model):
    adId = models.ForeignKey(AdDetails)
    advEmail = models.ForeignKey(Users)
    postDate = models.DateField()
    targetLocation = models.CharField(max_length=50)
    price = models.ForeignKey(Price)

    class Meta:
        unique_together = (('adId','advEmail','postDate'))


class AdminDetails(models.Model):
    adminEmail = models.EmailField(max_length=100, primary_key=True)
    password = models.CharField(max_length=150)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    accessLevel = models.CharField(max_length=5, default='admin', editable=False)
