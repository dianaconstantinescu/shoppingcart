from django.shortcuts import render
from .models import Category,Product
# Create your views here.





def product_list(request):
   products= Product.objects.all()
   category=Category.objects.all()
   context={'category':category,'products':products}  #trebuie sa am products in for in template
   return render(request, "list.html", context)

def product_detail(request,productid):
    id=productid
    produs=Product.objects.get(pk=int(id))
    print(produs.id)
    context={'produs':produs}
    return render(request,'detail.html',context)

# Create your views here.