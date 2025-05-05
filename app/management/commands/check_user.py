from django.core.management.base import BaseCommand
from app.models import CustomUser

class Command(BaseCommand):
    help = 'Check user information'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Username to check')

    def handle(self, *args, **options):
        username = options['username']
        self.stdout.write(f'Checking user: {username}')
        
        try:
            user = CustomUser.objects.get(username=username)
            self.stdout.write('\nUser found:')
            self.stdout.write(f'Username: {user.username}')
            self.stdout.write(f'Email: {user.email}')
            self.stdout.write(f'Is active: {user.is_active}')
            self.stdout.write(f'Is email verified: {user.is_email_verified}')
            self.stdout.write(f'Last login: {user.last_login}')
            self.stdout.write(f'Date joined: {user.date_joined}')
        except CustomUser.DoesNotExist:
            self.stdout.write(self.style.ERROR('\nUser does not exist'))
            
            # Check if any users exist
            total_users = CustomUser.objects.count()
            if total_users == 0:
                self.stdout.write('\nNo users exist in the database.')
            else:
                self.stdout.write(f'\nTotal users in database: {total_users}')
                self.stdout.write('\nExample usernames:')
                for user in CustomUser.objects.all()[:5]:
                    self.stdout.write(f'- {user.username} ({user.email})') 