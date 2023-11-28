from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from .serializers import BookSerializer
from .models import Book


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # there's some changes made for book api

    @action(methods=['get'], detail=False, url_path=r'count', url_name='count')
    def get_book_count(self, request):
        book_count = Book.objects.count()
        return Response({'count': book_count})
