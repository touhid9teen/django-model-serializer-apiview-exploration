from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Alumni
from .serializers import AlumniSerializer, AlumniWithMentorSerializer, AlumniWithNetworkSerializer, AlumniWithOneToOneSerializer, 



# --------------------Basic API View:
class AlumniListCreateAPIView(APIView):
    def get(self, request):
        alumni = Alumni.objects.all()
        serializer = AlumniSerializer(alumni, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AlumniSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# ----------------APIView with ForeignKey:


class AlumniDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            alumni = Alumni.objects.get(pk=pk)
        except Alumni.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = AlumniWithMentorSerializer(alumni)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            alumni = Alumni.objects.get(pk=pk)
        except Alumni.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = AlumniWithMentorSerializer(alumni, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            alumni = Alumni.objects.get(pk=pk)
        except Alumni.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        alumni.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# ---------------------APIView with ForeignKey:

class AlumniDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            alumni = Alumni.objects.get(pk=pk)
        except Alumni.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = AlumniWithMentorSerializer(alumni)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            alumni = Alumni.objects.get(pk=pk)
        except Alumni.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = AlumniWithMentorSerializer(alumni, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            alumni = Alumni.objects.get(pk=pk)
        except Alumni.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        alumni.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# ------------------------APIView with ManyToManyField:
class AlumniNetworkListAPIView(APIView):
    def get(self, request):
        alumni = Alumni.objects.all()
        serializer = AlumniWithNetworkSerializer(alumni, many=True)
        return Response(serializer.data)

# ------------------------APIView with OneToOneField:

class AlumniOneToOneDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            alumni = Alumni.objects.get(pk=pk)
        except Alumni.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = AlumniWithOneToOneSerializer(alumni)
        return Response(serializer.data)
