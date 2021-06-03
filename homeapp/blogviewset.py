from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from homeapp.Serializer.Blogserializer import BlogSerializer
from homeapp.models import BlogModel

@api_view(['GET','POST'])

def blogsection(request):

    if request.method=='GET':

        v=BlogModel.objects.all()
        serializer=BlogSerializer(v,many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)

    if request.method=='POST':

        serializer=BlogSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

