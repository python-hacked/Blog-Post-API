from django.db import models

# Create your models here.

class User(models.Model):
    role =  [
        ('admin', 'admin'),
        ('user', 'user'),
    ]
    auther = models.CharField(choices=role)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # user_key = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category,on_delete=models.CASCADE, blank=True, related_name='categories')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.BigIntegerField()
    stock = models.BigIntegerField()

    def __str__(self):
        return self.name



STATUS_CHOICE = [("S","success"),
                 ("F","failed")]
class Payment(models.Model):
    order = models.ForeignKey(Product, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=20)
    payment_id = models.CharField(max_length=100)
    payment_status = models.CharField(max_length=20, choices=STATUS_CHOICE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)      


    