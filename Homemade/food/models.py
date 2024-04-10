from django.db import models


 

class Users(models.Model):
    User_Id=models.AutoField(primary_key=True)
    First_Name=models.CharField(max_length=100,null=True)
    Last_Name=models.CharField(max_length=100,null=True)
    Contact=models.CharField(max_length=10,null=True)
    Email_Id=models.CharField(max_length=100,null=True)
    Password=models.CharField(max_length=100,null=True)

class Homemaker(models.Model):
    Homemaker_Id=models.AutoField(primary_key=True)
    First_Name=models.CharField(max_length=100,null=True)
    Last_Name=models.CharField(max_length=100,null=True)
    Kitchen_name=models.CharField(max_length=100,null=True)
    Contact=models.CharField(max_length=10,null=True)
    Email_Id=models.CharField(max_length=100,null=True)
    Kitchen_Address=models.CharField(max_length=200,null=True)

class Item(models.Model):
    Item_Id=models.AutoField(primary_key=True)
    Homemaker_id=models.ForeignKey(Homemaker,default=1, verbose_name="Homemaker",on_delete=models.SET_DEFAULT) 
    Item_name= models.CharField(max_length=100,null=True)
    Item_price = models.IntegerField(default=1000)
    Item_quantity = models.IntegerField(default=1000)


class orders(models.Model):
    order_Id=models.AutoField(primary_key=True)
    Item_Id=models.ForeignKey(Item, default=1, verbose_name="Item", on_delete=models.SET_DEFAULT)
    User_Id=models.ForeignKey(Users,default=1, verbose_name="User", on_delete=models.SET_DEFAULT)
    order_date=models.DateField(("Date"))
    order_total_price=models.IntegerField(default=1000)

       










