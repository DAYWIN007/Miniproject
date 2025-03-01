from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
import MySQLdb
from myapp.models import Product
# Create your views here.

def home(request):
    return render(request, 'base.html')
def inspirations(request):
    return render(request, 'body.html')

# def login_view(request):

#     form = AuthenticationForm()
#     return render(request, 'login.html', {'form': form})

def index_page(request):
    if request.method == 'POST':
        db=MySQLdb.connect(host="localhost",user="root",
                  password="",database="miniproject")
        
        brand = request.POST.get('brand')
        proid = request.POST.get('proid')
        ImagesURL = request.POST.get('images')
        proname = request.POST.get('proname')
        detail = request.POST.get('detail')
        price = request.POST.get('price')
        
        file = request.FILES.get('images')
        images_base64 = ''
        if file:
            file_data = file.read()
            import base64
            base64_string = base64.b64encode(file_data).decode('utf8')
            images_base64 = f"data:images/jpeg;base64,{base64_string}"

        with db.cursor() as cursor:
            cursor.executemany(
                """INSERT INTO product (brand,proid,images,proname,detail,price)
            VALUES (%s,%s,%s,%s,%s,%s)""",[(brand,proid,images_base64,proname,detail,price)])
            
            
        db.commit()
    
    db=MySQLdb.connect(host="localhost",user="root",
                  password="",database="miniproject")
    product_list = []
    with db.cursor() as cursor:
        query = "SELECT * FROM `product` WHERE 1"
        cursor.execute(query)
        rows = cursor.fetchall()
        for iteme in rows:
            pro = Product(*iteme) 
            product_list.append(pro)
            
    context = {'product_list': product_list}
    return render(request, 'index.html',context)


def nike_page(request):
    db=MySQLdb.connect(host="localhost",user="root",
                  password="",database="miniproject")
    product_list = []
    with db.cursor() as cursor:
        query = " SELECT * FROM `product` WHERE brand = 'Nike'"
        cursor.execute(query)
        rows = cursor.fetchall()
        for iteme in rows:
            pro = Product(*iteme) 
            product_list.append(pro)
            
    context = {'product_list': product_list}
    return render(request, 'nike.html',context)

def adidas_page(request):
    
    db=MySQLdb.connect(host="localhost",user="root",
                  password="",database="miniproject")
    product_list = []
    with db.cursor() as cursor:
        query = " SELECT * FROM `product` WHERE brand = 'adidas'"
        cursor.execute(query)
        rows = cursor.fetchall()
        for iteme in rows:
            pro = Product(*iteme) 
            product_list.append(pro)
            
    context = {'product_list': product_list}
    
    return render(request, 'adidas.html',context)

def puma_page(request):
    
    db=MySQLdb.connect(host="localhost",user="root",
                  password="",database="miniproject")
    product_list = []
    with db.cursor() as cursor:
        query = " SELECT * FROM `product` WHERE brand = 'Puma'"
        cursor.execute(query)
        rows = cursor.fetchall()
        for iteme in rows:
            pro = Product(*iteme) 
            product_list.append(pro)
            
    context = {'product_list': product_list}
    
    return render(request, 'puma.html',context)

def converse_page(request):
    
    db=MySQLdb.connect(host="localhost",user="root",
                  password="",database="miniproject")
    product_list = []
    with db.cursor() as cursor:
        query = " SELECT * FROM `product` WHERE brand = 'converse'"
        cursor.execute(query)
        rows = cursor.fetchall()
        for iteme in rows:
            pro = Product(*iteme) 
            product_list.append(pro)
            
    context = {'product_list': product_list}
    
    return render(request, 'converse.html',context)


def OnitsukaTiger_page(request):
    
    db=MySQLdb.connect(host="localhost",user="root",
                  password="",database="miniproject")
    product_list = []
    with db.cursor() as cursor:
        query = " SELECT * FROM `product` WHERE brand = 'Onitsuka Tiger'"
        cursor.execute(query)
        rows = cursor.fetchall()
        for iteme in rows:
            pro = Product(*iteme) 
            product_list.append(pro)
            
    context = {'product_list': product_list}
    
    return render(request, 'onitsukaTiger.html',context)

def allpro_page(request):
    return render(request, 'allpro.html')

def productadd(request):
    return render(request, 'productadd.html')