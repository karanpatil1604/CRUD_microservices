from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from .models import Dictionary
from .serializers import DictionarySerializer


class DictionaryViewSet(ModelViewSet):
    queryset = Dictionary.objects.all()
    serializer_class = DictionarySerializer

    def create(self, request, pk=None):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        return Response(
            serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        try:
            dictionary_item = Dictionary.objects.get(key=pk)
            serializer = self.get_serializer(dictionary_item)
            return Response(serializer.data)
        except Dictionary.DoesNotExist:
            return Response({"detail": "Dictionary not found"}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        try:
            dictionary_item = Dictionary.objects.get(key=pk)
            serializer = self.get_serializer(
                dictionary_item, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        except Dictionary.DoesNotExist:
            return Response({"detail": "Dictionary not found"}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            dictionary_item = Dictionary.objects.get(key=pk)
            dictionary_item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Dictionary.DoesNotExist:
            return Response({"detail": "Dictionary not found"}, status=status.HTTP_404_NOT_FOUND)
