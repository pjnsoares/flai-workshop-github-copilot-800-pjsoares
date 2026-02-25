from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import User, Team, Activity, Leaderboard, Workout
from datetime import date


class UserAPITests(APITestCase):
    def setUp(self):
        User.objects.all().delete()
        self.user = User.objects.create(
            username='ironman',
            email='ironman@avengers.com',
            password='IronMan123!',
        )

    def test_list_users(self):
        url = reverse('user-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_create_user(self):
        url = reverse('user-list')
        data = {'username': 'blackwidow', 'email': 'bw@avengers.com', 'password': 'Widow123!'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TeamAPITests(APITestCase):
    def setUp(self):
        Team.objects.all().delete()
        self.team = Team.objects.create(name='Team Marvel', members=['ironman', 'spiderman'])

    def test_list_teams(self):
        url = reverse('team-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_create_team(self):
        url = reverse('team-list')
        data = {'name': 'Team DC', 'members': ['batman', 'superman']}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ActivityAPITests(APITestCase):
    def setUp(self):
        Activity.objects.all().delete()
        self.activity = Activity.objects.create(
            username='ironman',
            activity_type='Running',
            duration=45.0,
            date=date(2024, 1, 15),
        )

    def test_list_activities(self):
        url = reverse('activity-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_create_activity(self):
        url = reverse('activity-list')
        data = {'username': 'batman', 'activity_type': 'Cycling', 'duration': 60.0, 'date': '2024-01-20'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class LeaderboardAPITests(APITestCase):
    def setUp(self):
        Leaderboard.objects.all().delete()
        self.entry = Leaderboard.objects.create(username='ironman', score=450)

    def test_list_leaderboard(self):
        url = reverse('leaderboard-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_create_leaderboard_entry(self):
        url = reverse('leaderboard-list')
        data = {'username': 'batman', 'score': 430}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class WorkoutAPITests(APITestCase):
    def setUp(self):
        Workout.objects.all().delete()
        self.workout = Workout.objects.create(
            name='Iron Man Power Circuit',
            description='High-intensity circuit training.',
            duration=45.0,
        )

    def test_list_workouts(self):
        url = reverse('workout-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_create_workout(self):
        url = reverse('workout-list')
        data = {'name': 'Batman Cape Cardio', 'description': 'Gotham endurance run.', 'duration': 60.0}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ApiRootTests(APITestCase):
    def test_api_root(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('users', response.data)
        self.assertIn('teams', response.data)
        self.assertIn('activities', response.data)
        self.assertIn('leaderboard', response.data)
        self.assertIn('workouts', response.data)
