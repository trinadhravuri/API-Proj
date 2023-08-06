from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializer import *
import requests
import jsonpath
# Create your views here.

class BookApiView(APIView):
    serializer_class = BooksSerializer
    def get(self,request):
        allbooks = Books.objects.all().values()
        context = {'message':"list of books",'Book list':allbooks}
        return Response(context)
    
    def post(self,request):
        print("Requested data is :", request.data)
        serializer_obj = BooksSerializer(data=request.data)
        if(serializer_obj.is_valid()):

            Books.objects.create(id=serializer_obj.data.get('id'),
                                book_name = serializer_obj.data.get('book_name'),
                                author = serializer_obj.data.get('author'),
                                publisher = serializer_obj.data.get('publisher'))

        book = Books.objects.all().filter(id=request.data['id']).values()
        context = {
            'message':'New book',
            'book':book
        }
        return Response(context)
    def delete(self,request,pk= None):
        return Response({'method':'DELETE'})


def home(request):
    allbooks = Books.objects.all()
    context = {
        'allbooks':allbooks
    }
    return render(request,'home.html',context)

def weather(request):
    res = requests.get('https://api.openweathermap.org/data/3.0/onecall?lat=16.2359&lon=80.0496&exclude=daily&appid=d5cc48f0306399b91909f485463d9bac')
    dat = res.text
    # dat_jpath = jsonpath.jsonpath(dat,'daily')
    # dat_jpath = dat_jpath['daily']
    context = {
        'dat':dat
    }
    return render(request,'home.html',context)

def ind_book(request,pk):
    book = Books.objects.get(pk=pk)
    context = {
        'book':book
    }
    return render(request,'home.html',context)