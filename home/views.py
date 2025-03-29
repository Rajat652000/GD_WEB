from django.shortcuts import render,redirect,get_object_or_404
from .models import Machines,MachineImage,Product,ProductImages,contact,Inquiry,InquiryProduct
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail
# Create your views here.

def Index(request):
    machine = Machines.objects.all()
    context = {
        "machines": machine
    }
    return render(request, 'index.html', context)

def Machine_detail(request, pk):
    machine_detail = get_object_or_404(Machines, id=pk)
    return render(request, 'detail_page.html', {'machine_detail': machine_detail})

def Machine_form(request):
    if request.user.is_anonymous:
        return redirect("login")
    if request.method == "POST":
        m_name = request.POST.get("machine_name")
        m_description = request.POST.get("description")
        m_price = request.POST.get("price")
        m_image = request.FILES.get("image")

        machine = Machines(Machine_name=m_name, Description=m_description, Price=m_price, image=m_image)
        machine.save()

        
        more_images = request.FILES.getlist("extra_images[]") 
        for img in more_images:
            MachineImage.objects.create(machine=machine, image=img)

        return redirect("/")

    return render(request, "machine_form.html")

def Product_form(request):
    if request.user.is_anonymous:
        return redirect("login")
    if request.method == "POST":
        P_name = request.POST.get("Product_name")
        P_description = request.POST.get("description")
        P_price = request.POST.get("price")
        P_image = request.FILES.get("image")

        product = Product(Product_name=P_name, P_Description=P_description, P_Price=P_price, P_image=P_image)
        product.save()

        
        more_images = request.FILES.getlist("extra_images[]") 
        for img in more_images:
            ProductImages.objects.create(Product=product, P_image=img)

        return redirect("prodcut")

    return render(request, "product_form.html")

def userlogin(request):
    if request.method == "POST":
        name = request.POST.get("name")
        password = request.POST.get("password")
        action = request.POST.get("action")  # Get which button was clicked

        user = authenticate(username=name, password=password)
        if user is not None:
            login(request, user)
            # Redirect based on which button was clicked
            if action == "upload_machine":
                return redirect("m_form")
            elif action == "upload_product":
                return redirect("P_form")
            return render(request, 'login.html', {"error": "Invalid credentials"})
        else:
            return render(request, 'login.html', {"error": "Invalid credentials"})
    
    return render(request, 'login.html')

def About(request):
    return render(request,"about.html")
 
def Contact(request,pk):
    product_detail = get_object_or_404(Machines, id=pk)
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        city = request.POST.get('city')
        porpose = request.POST.get('porpose')
        machine_name = request.POST.get("machine_name")
        machine_price = request.POST.get("machine_price")
        if all([name,phone,email,city,porpose,machine_name,machine_price]):
            Contact = contact(name=name, phone=phone, email=email, city=city, porpose=porpose, product_name = machine_name, product_price = machine_price)
            Contact.save()
        subject = f"New Inquiry from {name}"
        message = f"""
        Name: {name}
        Phone: {phone}
        Email: {email}
        City: {city}
        Purpose: {porpose}
        Machine Name: {machine_name}
        Machine Price: {machine_price}
        """
        from_email = email  # Use customer's email as sender
        owner_email = "rp9470043@gmail.com"  # Replace with the owner's email
        
        send_mail(subject, message, from_email, [owner_email])
        return render(request, "thank_you.html", {"name": name})
    return render(request,"contact.html",{"Product_detail":product_detail})


def product(request):
    product = Product.objects.all()
    context = {
        "Products": product
    }
    return render(request, 'product.html', context)

def product_detail(request, pk):
    product_detail = get_object_or_404(Product, id=pk)
    return render(request, 'product_detail.html', {'product_detail': product_detail})


def contact_form(request, pk):
    all_products = Product.objects.all()
    product = get_object_or_404(Product, id=pk)

    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        city = request.POST.get('city')
        purpose = request.POST.get('purpose')

        # Create Inquiry entry
        inquiry = Inquiry.objects.create(name=name, phone=phone, email=email, city=city, purpose=purpose)

        # Save all products in the InquiryProduct model
        products = request.POST.getlist("product_name[]")
        prices = request.POST.getlist("product_price[]")
        quantities = request.POST.getlist("quantity[]")
        product_details = []
        for product_name, product_price, quantity in zip(products, prices, quantities):
            InquiryProduct.objects.create(
                inquiry=inquiry,
                product_name=product_name,
                product_price=product_price,
                quantity=int(quantity)
            )
            product_details.append(f"{product_name} - Price: {product_price}, Quantity: {quantity}")
        # Prepare email content
        subject = f"New Inquiry from {name}"
        message = f"""
        Name: {name}
        Phone: {phone}
        Email: {email}
        City: {city}
        Purpose: {purpose}

        Products:
        {chr(10).join(product_details)}
        """
        from_email = email  # Use customer's email as sender
        owner_email = "rp9470043@gmail.com"  # Replace with the owner's email

        send_mail(subject, message, from_email, [owner_email])

        return render(request, "thank_you.html", {"name": name})

    return render(request, "Product_contact.html", {"product": product, "all_products": all_products})


def Machine_Delete(request,pk):
    machine = Machines.objects.get(id=pk)
    machine.delete()
    return redirect("machine_list")

def Product_Delete(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return redirect("product_list")

def machine_list(request):
    machines = Machines.objects.all()
    return render(request,"machine_list.html",{"machines": machines})

def product_list(request):
    #if request.user.is_anonymous:
    #    return redirect("login")
    products = Product.objects.all()
    return render(request,"product_list.html",{"products": products})