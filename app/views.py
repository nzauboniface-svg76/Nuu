from django.shortcuts import render, redirect
from .models import CartOrder
# Create your views here.
def index(request):
    success = False
    order_summary = None
    if request.method == "POST":
        customer = request.POST.get("customer")
        email = request.POST.get("email")
        address = request.POST.get("address")
        payment = request.POST.get("payment")
        items_json = request.POST.get("items")
        # Save order
        CartOrder.objects.create(
            customer=customer,
            email=email,
            address=address,
            payment=payment,
            items=items_json
        )
        success = True
        import json
        try:
            items = json.loads(items_json)
        except Exception:
            items = []
        total = sum([item.get('price', 0) * item.get('quantity', 1) for item in items])
        order_summary = {
            "customer": customer,
            "email": email,
            "address": address,
            "payment": payment,
            "items": items,
            "total": total
        }
    return render(request, "app/index.html", {"success": success, "order_summary": order_summary})

def admin(request):
    orders = CartOrder.objects.all().order_by('-timestamp')
    return render(request, "app/admin.html", {"orders": orders})