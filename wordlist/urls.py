from django.urls import path

from . import views
from .views import WordList, WordCreate, WordUpdate, WordDelete

app_name = 'wordlist'
urlpatterns = [
    path('', WordList.as_view(), name='index'),
    path('create', WordCreate.as_view(), name='create'),
    path('<int:pk>/update', WordUpdate.as_view(), name='update'),
    path('<int:pk>/delete', WordDelete.as_view(), name='delete'),
]
