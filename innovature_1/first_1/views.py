from .models import BooksList
from .serializers import BookSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import generics


# @api_view(['GET','POST','PUT'])
# @permission_classes([IsAuthenticated])
# def books_list(request, pk):

#     if request.method == 'GET':
#         books = BooksList.objects.all()
#         serializer = BookSerializer(books, many=True)
#         #serializer will be an object inorder to access what's inside it we use .data
#         return Response(serializer.data)

#     if request.method == 'POST':
#         serializer = BookSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#     if request.method == 'PUT':
#          books = BooksList.objects.get(pk=pk)
#          serializer = BookSerializer(books, data=request.data)
#          if serializer.is_valid():
#              serializer.save()
#              return Response(serializer.data)
#          else:
#              return Response(serializer.errors)

#innovature , innovature123
# Git url - https://github.com/Sathyajith6909/innovature_1.git







# class BookDetailAV(APIView):

#     def get(self,request,pk):

#         try:
#             ott = BooksList.objects.get(pk=pk)
#         except BooksList.DoesNotExist:
#             return Response({'Error':'Sorry the page you are looking for does not exist'},
#             status=status.HTTP_404_NOT_FOUND)
#         serializer = BookSerializer(ott,context={'request': request})
#         return Response(serializer.data)
    

#     def put(self,request,pk):
#         ott = BooksList.objects.get(pk=pk)
#         serializer = BookSerializer(ott, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


#     def delete(self,request,pk):
#         ott = BooksList.objects.get(pk=pk)
#         ott.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#########
    # def post(self,request):
    #     serializer = BookSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     else:
    #         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#########


class ShelfList(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    queryset = BooksList.objects.all()
    serializer_class = BookSerializer