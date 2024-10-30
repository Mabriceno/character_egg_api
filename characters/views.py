
from rest_framework.views import APIView
from rest_framework.response import Response
from characters.models import Character
from characters.serializers import CharacterSerializer
import requests


class CharacterListAPIView(APIView):
    def get(self, request):
        characters = Character.objects.all()
        character_list = []

        for character in characters:
            # Serialize basic character data
            serializer = CharacterSerializer(character)
            character_data = serializer.data

            # Fetch image URL from PokeAPI
            api_url_pokemon = f'https://pokeapi.co/api/v2/pokemon/{character.name}'
            result = requests.get(api_url_pokemon)
            
            if result.status_code == 200:
                pokemon_data = result.json()
                url_image = pokemon_data['sprites']['other']['official-artwork']['front_default']
            else:
                url_image = None

            # Combine data with image URL
            character_data['image_url'] = url_image
            character_list.append(character_data)

        return Response(character_list)
    
class RandomCharacterAPIView(APIView):
    def get(self, request):
        # Get a random character from the database
        character = Character.objects.order_by('?').first()

        # If no character exists, return an error
        if not character:
            return Response({"error": "No characters found"}, status=404)

        # Serialize character data
        serializer = CharacterSerializer(character)
        character_data = serializer.data

        # Fetch image URL from PokeAPI
        api_url_pokemon = f'https://pokeapi.co/api/v2/pokemon/{character.name}'
        result = requests.get(api_url_pokemon)
        
        if result.status_code == 200:
            pokemon_data = result.json()
            url_image = pokemon_data['sprites']['other']['official-artwork']['front_default']
        else:
            url_image = None

        # Combine character data with image URL
        character_data['image_url'] = url_image

        return Response(character_data)