from django.db.backends.utils import truncate_name
from django.shortcuts import render,HttpResponse
from django.db import connections
from .query import get_result

# Create your views here.
def login(request):
    # with connections['Datacurate'].cursor() as c:
    #     c.execute('SELECT * FROM CRS_MART where TXT_MOBILE=9999999999')
    #     return HttpResponse (dictfetchall(c))
    return render(request, 'home\login.html')

def home(request):
    # with connections['Datacurate'].cursor() as c:
    #     c.execute('SELECT * FROM CRS_MART where TXT_MOBILE=9999999999')
    #     return HttpResponse (dictfetchall(c))
    return render(request, 'home\index.html')

def dashboard(request):
    return render(request, 'home\index.html')

def bulk(request):
    return render(request, r'home\bulk.html')

def query(request):
    if request.method=="POST":
        search_value=request.POST.get('roll_number')
        #print(search_value)
        #print(request.POST.get('roll_number1'))
        option_value= request.POST.get('roll_number1')
        condition=request.POST.get('roll_number2')
        output_filter=request.POST.getlist('field2')
        r_value=request.POST.get('raze')
        r_value1=request.POST.get('raze1')
        
        
        
        #print(output_filter)
        #print(r_value)
        #print(r_value1)
        z=get_result(search_value,option_value,condition,output_filter,r_value,r_value1)
        null_output=True
       
        if len(z)==0:
            print("NULL")
        else:
            null_output=False
            print(z)
        context={'z':z,'option_value':option_value,'null_output':null_output,'output_filter':output_filter}
        #a=["table-warning","table-danger","table-success","table-primary","table-secondary"]
        return render(request, 'home\query.html',context)
    #elif request.method=="GET":
       # return render(request, 'home\query.html',{'z':z})
        

    return render(request, 'home\query.html')




        


def dictfetchall(cursor):
    columns=[col[0] for col in cursor.description]
    return[
        dict(zip(columns,row))
        for row in cursor.fetchall()
    ]
