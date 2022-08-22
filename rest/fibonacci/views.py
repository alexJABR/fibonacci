from ast import Return
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from fibonacci.models import Fibonacci
from fibonacci.serializers import FibonacciSerializer
import json, os
from django.urls import include,  re_path
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    re_path(r'^$', schema_view)
]
@api_view(['GET', 'POST'])
def fibonacci_list(request, format=None):
    """
    List all fibonacci, or create a new fibonacci.
    """
    if request.method == 'GET':
        fibonacci = Fibonacci.objects.all()
        serializer = FibonacciSerializer(fibonacci, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FibonacciSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def fibonacci_new(request, size, format=None):
    try:
        if size > 999:
            return Response(status=status.HTTP_204_NO_CONTENT)
        fibonacci = Fibonacci.objects.get(total=size)
        serializer = FibonacciSerializer(fibonacci)
        return Response(serializer.data)
    except Fibonacci.DoesNotExist:
        resultado=fibonacci_build(size)
        fibonacci = Fibonacci(total=size, resultado=resultado)
        fibonacci.save()
        with open('storage/'+str(size)+'.json', 'w') as f:
            f.write(resultado)
        serializer = FibonacciSerializer(fibonacci)
        return Response(serializer.data)

@api_view(['GET'])
def fibonacci_delete(request, size, format=None):
    try:
        fibonacci = Fibonacci.objects.get(total=size)
        fibonacci.delete()
        os.remove('storage/'+str(size)+'.json')
        fibonacci = Fibonacci.objects.all()
        serializer = FibonacciSerializer(fibonacci, many=True)
        return Response(serializer.data)
    except Fibonacci.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

def fibonacci_build(pos):  
  fibonacci = [1,1]
  for i in range(0,pos-2):
    fibonacci.append(fibonacci[i]+fibonacci[i+1])
  return json.dumps(fibonacci)