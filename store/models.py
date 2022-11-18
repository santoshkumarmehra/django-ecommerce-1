from django.db import models
import datetime

class Customer(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    phoneno = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500)


    def __str__(self):
        return self.first_name


    def register(self):
        self.save()

    
    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False


class Category(models.Model):
    name = models.CharField(max_length=20)


    @staticmethod
    def get_all_category():
        return Category.objects.all()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=70)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=200, default='')
    image = models.ImageField(upload_to='images/', max_length=5000, null=True, blank=True)


    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)


    @staticmethod
    def get_all_product():
        return Product.objects.all()


    @staticmethod
    def get_all_product_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.objects.all()


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    Transaction_id = models.CharField(max_length=100, default=1)
    price = models.IntegerField()
    date = models.DateField(default=datetime.datetime.today)


    @staticmethod
    def get_products_by_name(ids):
        return Order.objects.filter(customer = Customer(id=ids))
