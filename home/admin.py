from django.contrib import admin
from .models import Machines, MachineImage,Product,ProductImages,contact,Inquiry,InquiryProduct
# Register your models here.

admin.site.register(Machines)
admin.site.register(MachineImage)
admin.site.register(Product)
admin.site.register(ProductImages)
admin.site.register(contact)
admin.site.register(Inquiry)
admin.site.register(InquiryProduct)
