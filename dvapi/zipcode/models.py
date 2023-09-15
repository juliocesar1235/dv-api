from django.db import models

# Create your models here.
class Zipcode(models.Model):
  id = models.AutoField(
    primary_key=True
  )

  zipcode = models.CharField(
    max_length=200,
    null=False,
    blank=False
  )

  settlement = models.CharField(
    max_length=500,
    null=False,
    blank=False
  )

  settlement_type = models.CharField(
    max_length=200,
    null=False,
    blank=False
  )

  municipality = models.CharField(
      max_length=200,
      null=False,
      blank=False
  )
  
  state = models.CharField(
      max_length=200,
      null=False,
      blank=False
  )

  city = models.CharField(
      max_length=200,
      null=True,
      blank=True
  )

  settlement_zipcode = models.CharField(
      max_length=200,
      null=False,
      blank=False
  )
  
  state_code = models.IntegerField(
      null=False,
      blank=False
  )

  office_zipcode = models.CharField(
      max_length=200,
      null=False,
      blank=False
  )

  settlement_type_code = models.CharField(
    max_length=50,
    null=False,
    blank=False
  )
  
  settlement_id = models.IntegerField(
    null=False,
    blank=False
  )

  zone = models.CharField(
    max_length=200,
    null=False,
    blank=False
  )

  city_code = models.IntegerField(
    null=True,
    blank=True
  )

  municipality_code = models.IntegerField(
    null=False,
    blank=False
  )
  



  class Meta:
    db_table = 'Zipcode'