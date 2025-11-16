from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        t = Team.objects.create(name='Test Team')
        self.assertEqual(str(t), 'Test Team')
    def test_user_create(self):
        t = Team.objects.create(name='Test Team')
        u = User.objects.create_user(username='test', email='test@example.com', password='pass', team=t)
        self.assertEqual(u.email, 'test@example.com')
    def test_activity_create(self):
        t = Team.objects.create(name='Test Team')
        u = User.objects.create_user(username='test', email='test@example.com', password='pass', team=t)
        a = Activity.objects.create(user=u, type='run', duration=10)
        self.assertEqual(a.type, 'run')
    def test_workout_create(self):
        t = Team.objects.create(name='Test Team')
        u = User.objects.create_user(username='test', email='test@example.com', password='pass', team=t)
        w = Workout.objects.create(user=u, description='desc', duration=20)
        self.assertEqual(w.description, 'desc')
    def test_leaderboard_create(self):
        t = Team.objects.create(name='Test Team')
        u = User.objects.create_user(username='test', email='test@example.com', password='pass', team=t)
        l = Leaderboard.objects.create(user=u, score=42)
        self.assertEqual(l.score, 42)
