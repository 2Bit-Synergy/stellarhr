from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group

class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def handle(self, *args, **options):
        admin_group, created = Group.objects.get_or_create(name='Admin')
        editor_group, created = Group.objects.get_or_create(name='HR')
        viewer_group, created = Group.objects.get_or_create(name='Employee')

        self.stdout.write(self.style.SUCCESS('Groups created successfully'))

