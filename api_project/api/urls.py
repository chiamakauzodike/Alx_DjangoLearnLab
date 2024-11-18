from django.urls import path
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter
from django.urls import include
from rest_framework.authtoken.views import obtain_auth_token

#initialising the router
router = DefaultRouter()
#registering the BookViewSet router
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('', include(router.urls)),
    path('api/token/', obtain_auth_token, name='api-token')
]