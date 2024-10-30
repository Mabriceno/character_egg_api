# myapp/urls.py

from django.urls import path
from characters.views import CharacterListAPIView, RandomCharacterAPIView


urlpatterns = [
    path('api/characters/', CharacterListAPIView.as_view(), name='character-list'),
    path('api/characters/random/', RandomCharacterAPIView.as_view(), name='random-character')
]