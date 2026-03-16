from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class BasicModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Marvel', description='Marvel superheroes')
        self.assertEqual(team.name, 'Marvel')

    def test_create_user(self):
        team = Team.objects.create(name='DC', description='DC superheroes')
        user = User.objects.create(email='batman@dc.com', name='Batman', team=team, is_superhero=True)
        self.assertEqual(user.name, 'Batman')

    def test_create_activity(self):
        team = Team.objects.create(name='Marvel', description='Marvel superheroes')
        user = User.objects.create(email='spiderman@marvel.com', name='Spiderman', team=team, is_superhero=True)
        activity = Activity.objects.create(user=user, type='Running', duration=30, date='2023-01-01')
        self.assertEqual(activity.type, 'Running')

    def test_create_workout(self):
        workout = Workout.objects.create(name='Pushups', description='Upper body workout')
        self.assertEqual(workout.name, 'Pushups')

    def test_create_leaderboard(self):
        team = Team.objects.create(name='Marvel', description='Marvel superheroes')
        leaderboard = Leaderboard.objects.create(team=team, points=100)
        self.assertEqual(leaderboard.points, 100)
