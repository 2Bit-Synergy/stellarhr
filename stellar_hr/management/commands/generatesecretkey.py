from django.core.management.base import BaseCommand
from django.core.management.utils import get_random_secret_key
import os

class Command(BaseCommand):
    help = 'Generate a new secret key and add it to the .env file'

    def handle(self, *args, **options):
        # Generate a new secret key
        secret_key = get_random_secret_key()

        # Update .env file or create it if it doesn't exist
        env_file_path = os.path.join(os.getcwd(), '.env')

        with open(env_file_path, 'a') as env_file:
            env_file.write(f'SECRET_KEY={secret_key}\n')

        self.stdout.write(self.style.SUCCESS(f'Secret key has been generated and added to {env_file_path}'))
