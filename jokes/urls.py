from django.urls import path

from .views import (
    JokeCreateView,
    JokeDeleteView,
    JokeDetailView,
    JokeListView,
    JokeUpdateView,
    vote,
)

app_name = 'jokes'

urlpatterns = [
    path('', JokeListView.as_view(), name='list'),
    path('joke/create/', JokeCreateView.as_view(), name='create'),
    path('<slug>/', JokeDetailView.as_view(), name='detail'),
    path('<slug>/update/', JokeUpdateView.as_view(), name='update'),
    path('<slug>/delete/', JokeDeleteView.as_view(), name='delete'),
    path('<slug>/vote/', vote, name='vote'),
]