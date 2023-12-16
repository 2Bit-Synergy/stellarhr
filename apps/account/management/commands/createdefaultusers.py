from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group

from apps.account.models import User

class Command(BaseCommand):
    help = 'Seed the database with default initial data users'

    def handle(self, *args, **options):
        # Check if users already exist
        if User.objects.filter(username='admin@stellarhr.io').exists() and \
           User.objects.filter(username='hr@stellarhr.io').exists() and \
           User.objects.filter(username='employee@stellarhr.io').exists():
            self.stdout.write(self.style.SUCCESS('Users already exist. Skipping seeding.'))
            self.stdout.write(self.style.NOTICE('------------USERS-----------'))
            self.stdout.write(self.style.HTTP_INFO('admin@stellar.io | password'))
            self.stdout.write(self.style.HTTP_INFO('hr@stellar.io | password'))
            self.stdout.write(self.style.HTTP_INFO('employee@stellar.io | password'))
            self.stdout.write(self.style.NOTICE('----------------------------'))
            return

        # Create groups
        admin_group, created = Group.objects.get_or_create(name='Admin')
        hr_group, created = Group.objects.get_or_create(name='HR')
        employee_group, created = Group.objects.get_or_create(name='Employee')

        # Create users and assign them to groups
        admin_user, created = User.objects.get_or_create(username='admin@stellarhr.io', email='admin@stellarhr.io', first_name='Stellar', last_name='Admin', is_superuser=True, is_staff=True)
        if not created:
            self.stdout.write(self.style.SUCCESS('Admin user already exists. Skipping creation.'))
        else:
            admin_user.set_password('password')
            admin_user.save()
            admin_user.groups.add(admin_group)

        hr_user, created = User.objects.get_or_create(username='hr@stellarhr.io', email='hr@stellarhr.io', first_name='Stellar', last_name='HR', is_staff=True)
        if not created:
            self.stdout.write(self.style.SUCCESS('HR user already exists. Skipping creation.'))
        else:
            hr_user.set_password('password')
            hr_user.save()
            hr_user.groups.add(hr_group)

        employee_user, created = User.objects.get_or_create(username='employee@stellarhr.io', email='employee@stellarhr.io', first_name='Stellar', last_name='Employee')
        if not created:
            self.stdout.write(self.style.SUCCESS('Employee user already exists. Skipping creation.'))
        else:
            employee_user.set_password('password')
            employee_user.save()
            employee_user.groups.add(employee_group)

        self.stdout.write(self.style.SUCCESS('User seeded successfully'))
        self.stdout.write(self.style.NOTICE('------------USERS-----------'))
        self.stdout.write(self.style.HTTP_INFO('admin@stellar.io | password'))
        self.stdout.write(self.style.HTTP_INFO('hr@stellar.io | password'))
        self.stdout.write(self.style.HTTP_INFO('employee@stellar.io | password'))
        self.stdout.write(self.style.NOTICE('----------------------------'))
