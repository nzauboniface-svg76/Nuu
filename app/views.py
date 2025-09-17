from django.shortcuts import render, redirect
from .models import CartOrder
# Create your views here.
def index(request):
    if request.method == "POST":
        customer = request.POST.get("customer")
        email = request.POST.get("email")
        address = request.POST.get("address")
        payment = request.POST.get("payment")
        items = request.POST.get("items")
        # Save order
        CartOrder.objects.create(
            customer=customer,
            email=email,
            address=address,
            payment=payment,
            items=items
        )
        return redirect("home")
    return render(request, "app/index.html")

def admin(request):
    orders = CartOrder.objects.all().order_by('-timestamp')
    return render(request, "app/admin.html", {"orders": orders})