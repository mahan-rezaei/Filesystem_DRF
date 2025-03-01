from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import FileSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from permissions import IsOwnerOrReadOnly
from rest_framework.authentication import TokenAuthentication
from .models import File



class FileUploadView(APIView):
    """can upload a file with this view."""

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        ser_data = FileSerializer(data=request.data, context={'user': request.user})
        if ser_data.is_valid(raise_exception=True):
            ser_data.save()
            return Response({
                'message': 'file uploaded successfully.',
                'data': ser_data.data
            }, status=status.HTTP_201_CREATED)
        

class FileDeleteView(APIView):
    """delete one of teh user file who requested to this view."""

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get(self, request, file_id):
        file_instance = get_object_or_404(File, pk=file_id)
        file_instance.delete()
        return Response({
            'message': 'file deleted successfully',
        }, status=status.HTTP_204_NO_CONTENT)
