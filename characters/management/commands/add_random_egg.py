import random
from django.core.management.base import BaseCommand
from characters.models import Character

class Command(BaseCommand):
    help = "Randomly assigns one character as an egg."

    def handle(self, *args, **kwargs):
        # Fetch all characters
        characters = Character.objects.all()
        
        # Check if there are any characters in the database
        if not characters.exists():
            self.stdout.write(self.style.WARNING("No characters found in the database."))
            return

        # Reset all characters' egg field to False
        characters.update(egg=False)
        
        # Select a random character
        random_character = random.choice(characters)

        # Update the selected character's egg field to True
        random_character.egg = True
        random_character.save()

        # Print success message
        self.stdout.write(self.style.SUCCESS(f"Character '{random_character.name}' has been assigned as the egg."))