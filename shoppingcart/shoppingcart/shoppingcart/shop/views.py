from django.shortcuts import render
from .models import Category,Product
# Create your views here.





def product_list(request):
   products= Product.objects.all()
   categories=Category.objects.all()
   context={'category':categories,'products':products}  #trebuie sa am products in for in template
   return render(request, "list.html", context)

def category_product_list(request,categoryid=1):
    categories=Category.objects.all()
    products=Product.objects.filter(category=categoryid)
    context={'category':categories,'products':products}
    return render(request,"categoryproductlist.html",context)

def product_detail(request,productid):
    id=productid
    produs=Product.objects.get(pk=int(id))
    print(produs.id)
    context={'produs':produs}
    return render(request,'detail.html',context)

# Create your views here.