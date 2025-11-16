from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from octofit_tracker import models as octo_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Delete all data
        User.objects.all().delete()
        octo_models.Team.objects.all().delete()
        octo_models.Activity.objects.all().delete()
        octo_models.Leaderboard.objects.all().delete()
        octo_models.Workout.objects.all().delete()

        # Create teams
        marvel = octo_models.Team.objects.create(name='Team Marvel')
        dc = octo_models.Team.objects.create(name='Team DC')

        # Create users
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='pass', team=marvel)
        captain = User.objects.create_user(username='captain', email='captain@marvel.com', password='pass', team=marvel)
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='pass', team=dc)
        superman = User.objects.create_user(username='superman', email='superman@dc.com', password='pass', team=dc)

        # Create activities
        octo_models.Activity.objects.create(user=ironman, type='run', duration=30)
        octo_models.Activity.objects.create(user=batman, type='cycle', duration=45)

        # Create workouts
        octo_models.Workout.objects.create(user=ironman, description='Chest day', duration=60)
        octo_models.Workout.objects.create(user=superman, description='Leg day', duration=50)

        # Create leaderboard
        octo_models.Leaderboard.objects.create(user=ironman, score=100)
        octo_models.Leaderboard.objects.create(user=batman, score=90)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
