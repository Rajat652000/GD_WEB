from django.db import models

class Machines(models.Model):  # Class names should follow PascalCase
    Machine_name = models.CharField(max_length=250)
    Description = models.TextField()
    Price = models.IntegerField()
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Fix here
    image = models.ImageField(upload_to="machine_images/", null=True, blank=True)  # Specify upload directory

    def __str__(self):
        return self.Machine_name

    @property
    def getURL(self):
        if self.image:
            return self.image.url
        return ""  # Return an empty string if no image

class MachineImage(models.Model):
    machine = models.ForeignKey(Machines, on_delete=models.CASCADE, related_name="images")  
    image = models.ImageField(upload_to="machine_images/")  # Upload multiple images

    def __str__(self):
        return f"Image for {self.machine.Machine_name}"

class Product(models.Model):  # Class names should follow PascalCase
    Product_name = models.CharField(max_length=250)
    P_Description = models.TextField()
    P_Price = models.IntegerField()
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Fix here
    P_image = models.ImageField(upload_to="Produc_images/", null=True, blank=True)  # Specify upload directory

    def __str__(self):
        return self.Product_name

    @property
    def getURL(self):
        if self.P_image:
            return self.P_image.url
        return ""  # Return an empty string if no image

class ProductImages(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")  
    P_image = models.ImageField(upload_to="Produc_images/")  # Upload multiple images

    def __str__(self):
        return f"Image for {self.Product.Product_name}"
    
class contact(models.Model):
    name = models.CharField(max_length=122)
    phone = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    city = models.CharField(max_length=122)
    porpose = models.CharField(max_length=122)
    product_name = models.CharField(max_length=122)
    product_price = models.IntegerField()
    def __str__(self):
        return self.name


class Inquiry(models.Model):
    name = models.CharField(max_length=122)
    phone = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    city = models.CharField(max_length=122)
    purpose = models.CharField(max_length=122)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inquiry from {self.name} ({self.created_at})"

class InquiryProduct(models.Model):
    inquiry = models.ForeignKey(Inquiry, on_delete=models.CASCADE, related_name="products")
    product_name = models.CharField(max_length=250)
    product_price = models.IntegerField()
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product_name} (Inquiry ID: {self.inquiry.id})"