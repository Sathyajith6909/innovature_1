from .models import BooksList
from .serializers import BookSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response



@api_view(['GET','POST'])
def books_list(request):

    if request.method == 'GET':
        books = BooksList.objects.all()
        serializer = BookSerializer(books, many=True)
        #serializer will be an object inorder to access what's inside it we use .data
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)