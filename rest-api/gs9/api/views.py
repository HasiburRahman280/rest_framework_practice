from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
@api_view()
def hellow_word(request):
    return Response({'msg':'Hellow Word'})

# @api_view(['GET'])
# def hellow_word(request):
#     return Response({'msg':'Hellow Word'})

# @api_view(['POST'])
# def hellow_word(request):
#     if request.method == "POST":
#         print(request.data)
#         return Response({'msg':'tHIS IS POST METHOD'})
    
@api_view(['GET','POST'])
def hellow_word(request):
    if request.method == "GET":
        return Response({'msg':'tHIS IS Get METHOD'})
 
    if request.method == "POST":
        print(request.data)
        return Response({'msg':'tHIS IS POST METHOD', 'data':request.data})
    
 
