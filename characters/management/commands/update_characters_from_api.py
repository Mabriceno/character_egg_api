# myapp/management/commands/update_characters_from_api.py

import requests
from django.core.management.base import BaseCommand
from django.utils import timezone
from characters.models import Character, Universe

class Command(BaseCommand):
    help = "Updates the Character table from the PokeAPI for a specific universe."

    def add_arguments(self, parser):
        parser.add_argument(
            'universe_name', 
            type=str, 
            help="Name of the universe in which you want to update the characters"
        )

    def handle(self, *args, **options):
        universe_name = options['universe_name']
        
        # Check if the universe exists in the database
        try:
            universe = Universe.objects.get(name=universe_name)
        except Universe.DoesNotExist:
            self.stdout.write(self.style.ERROR(f"The universe '{universe_name}' does not exist."))
            return
        
        url = universe.api_id.url
        params = {"limit": 100, "offset": 0}  # Initial settings for pagination

        while True:
            response = requests.get(url, params=params)
            if response.status_code != 200:
                self.stdout.write(self.style.ERROR(f"Error fetching data from API: {response.status_code}"))
                break
            
            data = response.json()
            
            # Loop through each Pokémon in the current page of results
            for pokemon in data["results"]:
                pokemon_id = int(pokemon["url"].split("/")[-2])

                # Create or update each character in the database
                character, created = Character.objects.update_or_create(
                    character_api_id=pokemon_id,
                    universe_id=universe,
                    defaults={
                        "name": pokemon["name"],
                        "updated_at": timezone.now()
                    }
                )

                action = "Created" if created else "Updated"
                self.stdout.write(self.style.SUCCESS(f"{action} character: {character.name}"))

            # Check if there is a next page
            if not data["next"]:
                break
            # Update the offset to the next page
            params["offset"] += params["limit"]
        
        self.stdout.write(self.style.SUCCESS("Character update completed."))

