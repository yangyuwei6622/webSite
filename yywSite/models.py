from django.db import models

# Create your models here.
class BookInfo(models.Model):
    btitle = models.CharField(max_length = 20)
    bpub_date = models.DateField()
    def __str__(self):
        return self.btitle
class HeroInfo(models.Model):
    hName = models.CharField(max_length=10)
    hGender = models.BooleanField()
    hContent = models.CharField(max_length=20)
    hBook = models.ForeignKey('BookInfo', on_delete=models.CASCADE,default=0)
    hText = models.CharField(max_length=20 ,default=0)
    def __str__(self):
        return self.hName