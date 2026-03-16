from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Create users
        users = [
            User.objects.create(email='ironman@marvel.com', name='Iron Man', team=marvel, is_superhero=True),
            User.objects.create(email='captainamerica@marvel.com', name='Captain America', team=marvel, is_superhero=True),
            User.objects.create(email='spiderman@marvel.com', name='Spiderman', team=marvel, is_superhero=True),
            User.objects.create(email='batman@dc.com', name='Batman', team=dc, is_superhero=True),
            User.objects.create(email='superman@dc.com', name='Superman', team=dc, is_superhero=True),
            User.objects.create(email='wonderwoman@dc.com', name='Wonder Woman', team=dc, is_superhero=True),
        ]

        # Create activities
        Activity.objects.create(user=users[0], type='Running', duration=30, date=date(2023, 1, 1))
        Activity.objects.create(user=users[1], type='Cycling', duration=45, date=date(2023, 1, 2))
        Activity.objects.create(user=users[3], type='Swimming', duration=60, date=date(2023, 1, 3))

        # Create workouts
        workout1 = Workout.objects.create(name='Pushups', description='Upper body workout')
        workout2 = Workout.objects.create(name='Situps', description='Core workout')
        workout1.suggested_for.set([users[0], users[3]])
        workout2.suggested_for.set([users[1], users[4]])

        # Create leaderboards
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=120)

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
