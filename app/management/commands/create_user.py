from django.core.management.base import BaseCommand
from app.models import CustomUser
from django.contrib.auth.hashers import make_password

class Command(BaseCommand):
    help = 'Create a new user'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Username')
        parser.add_argument('email', type=str, help='Email address')
        parser.add_argument('password', type=str, help='Password')

    def handle(self, *args, **options):
        username = options['username']
        email = options['email']
        password = options['password']
        
        try:
            user = CustomUser.objects.create(
                username=username,
                email=email,
                password=make_password(password),
                is_active=True,
                is_email_verified=True  # Setting this to True for testing
            )
            self.stdout.write(self.style.SUCCESS(f'\nUser created successfully:'))
            self.stdout.write(f'Username: {user.username}')
            self.stdout.write(f'Email: {user.email}')
            self.stdout.write(f'Is active: {user.is_active}')
            self.stdout.write(f'Is email verified: {user.is_email_verified}')
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'\nError creating user: {str(e)}')) 