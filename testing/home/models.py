from django.db import models
from django.db import connections
from django.shortcuts import render,HttpResponse



# Create your models here.
class CRS_MART(models.Model):
    with connections['Datacurate'].cursor() as c:
        c.execute('SELECT * FROM CRS_MART where TXT_MOBILE=9999999999')
    #return HttpResponse (dictfetchall(c))
