from django.core.management.base import BaseCommand
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from apps.account.models import User

#  user = User.objects.get(username=username)
# # Get or create the group
# group, created = Group.objects.get_or_create(name=group_name)
# # Assign the user to the group
# user.groups.add(group)
class Command(BaseCommand):
    def handle(self, *args, **options):
        content_type = ContentType.objects.get_for_model(User)

        # Todo
        can_add = Permission.objects.create(codename='can_add', name='Can Add', content_type=content_type)
        can_change = Permission.objects.create(codename='can_change', name='Can Change', content_type=content_type)

        admin_group = Group.objects.get(name='Admin')
        hr_group = Group.objects.get(name='HR')

        admin_group.permissions.add(can_add, can_change)
        hr_group.permissions.add(can_change)