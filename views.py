from django.shortcuts import render,redirect
from app.models import User_Details
from app.models import Book_Details
from app.models import Book_Login
# Create your
#
# @views here.

def login(request):
    if request.method=='POST':
        a=request.POST.get('firstname')
        print(a)
        b=request.POST.get('Lastname')
        c=request.POST.get('mail')
        d=request.POST.get('password')
        s=request.POST.get('number')
        obj=User_Details.objects.create(Fname=a,Lname=b,User_Name=a,Password=d)
        return redirect('booklogin')
    return render(request,'login.html')

def lib(request):
    if request.method=='POST':
        library=Book_Details.objects.create(Name=request.POST.get('Name'),Code=request.POST.get('Code'),Author_name=request.POST.get('Author'),
                                            Date=request.POST.get('Date'),Status=request.POST.get('Status'),Amount=request.POST.get('Amount'),
                                            Created_date=request.POST.get('Created_date'),Created_by=request.POST.get('Created_by'),
                                            Updated_date=request.POST.get('Updated_date'),Updated_by=request.POST.get('Updated_by'))
        return redirect("Bookdetails")
    return render(request, 'book.html')
def book_login(request):

    if request.method=='POST':

        a=request.POST.get('Name')
        b=request.POST.get('Password')

        try:
            obj=User_Details.objects.get(Fname=a,Password=b)
            return redirect('Bookdetails')
        except:
            pass
    return render(request,'booklogin.html')
def bookdetails(request):
    obj=Book_Details.objects.all()
    return render(request,'bookdetails.html',{'obj':obj})
def updatebook(request,pk):
    print("pk")
    print(pk)
    obj=Book_Details.objects.get(id=pk)
    if request.method=='POST':
        library = Book_Details.objects.filter(id=pk).update(Name=request.POST.get('Name'), Code=request.POST.get('Code'),
                                              Author_name=request.POST.get('Author'),
                                              Date=request.POST.get('Date'),
                                              Amount=request.POST.get('Amount'))
        return redirect('Bookdetails')
                                              # Created_date=request.POST.get('Created_date'),
                                              # Created_by=request.POST.get('Created_by'),
                                              # Updated_date=request.POST.get('Updated_date'),
                                              # Updated_by=request.POST.get('Updated_by'))
    return render(request,'updatebook.html',{'obj':obj})

def deletebook(request,pk):
    print("pk")
    print(pk)
    obj=Book_Details.objects.filter(id=pk).delete()
    return redirect('Bookdetails')

def takebook(request,pk):
    print('pk')
    print(pk)
    obj= obj=Book_Details.objects.filter(id=pk).update(Status="Unavailable")
    return redirect("Bookdetails")

def retainbook(request,pk):
    print('pk')
    print(pk)
    obj= obj=Book_Details.objects.filter(id=pk).update(Status="Available")
    return redirect("Bookdetails")
