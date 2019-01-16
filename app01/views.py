from django.shortcuts import render,HttpResponse
from app01.models import Book
# Create your views here.


def addbook(request):
    if request.method == "POST":
        title=request.POST.get("title")
        price=request.POST.get("price")
        date=request.POST.get("date")
        publish=request.POST.get("publish")

        Book.objects.create(title=title,price=price,pub_date=date,publish=publish)

        return HttpResponse("ok")
    return render(request,"addbook.html")

def books(request):

    book_list = Book.objects.all()

    return render(request,"books.html",locals())