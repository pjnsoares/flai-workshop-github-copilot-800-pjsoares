from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Clearing existing data...')
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Team.objects.all().delete()
        User.objects.all().delete()

        self.stdout.write('Creating users...')
        users_data = [
            {'username': 'ironman', 'email': 'ironman@avengers.com', 'password': 'IronMan123!'},
            {'username': 'spiderman', 'email': 'spiderman@avengers.com', 'password': 'Spidey123!'},
            {'username': 'captainamerica', 'email': 'cap@avengers.com', 'password': 'Cap123!'},
            {'username': 'blackwidow', 'email': 'blackwidow@avengers.com', 'password': 'Widow123!'},
            {'username': 'batman', 'email': 'batman@dcleague.com', 'password': 'Batman123!'},
            {'username': 'superman', 'email': 'superman@dcleague.com', 'password': 'Super123!'},
            {'username': 'wonderwoman', 'email': 'wonderwoman@dcleague.com', 'password': 'Wonder123!'},
            {'username': 'theflash', 'email': 'flash@dcleague.com', 'password': 'Flash123!'},
        ]
        users = []
        for u in users_data:
            user = User(**u)
            user.save()
            users.append(user)
        self.stdout.write(self.style.SUCCESS(f'  Created {len(users)} users'))

        self.stdout.write('Creating teams...')
        team_marvel = Team(
            name='Team Marvel',
            members=['ironman', 'spiderman', 'captainamerica', 'blackwidow'],
        )
        team_marvel.save()

        team_dc = Team(
            name='Team DC',
            members=['batman', 'superman', 'wonderwoman', 'theflash'],
        )
        team_dc.save()
        self.stdout.write(self.style.SUCCESS('  Created Team Marvel and Team DC'))

        self.stdout.write('Creating activities...')
        activities_data = [
            {'username': 'ironman', 'activity_type': 'Running', 'duration': 45.0, 'date': date(2024, 1, 15)},
            {'username': 'spiderman', 'activity_type': 'Strength Training', 'duration': 60.0, 'date': date(2024, 1, 15)},
            {'username': 'captainamerica', 'activity_type': 'Cycling', 'duration': 90.0, 'date': date(2024, 1, 16)},
            {'username': 'blackwidow', 'activity_type': 'Yoga', 'duration': 50.0, 'date': date(2024, 1, 16)},
            {'username': 'batman', 'activity_type': 'Running', 'duration': 60.0, 'date': date(2024, 1, 15)},
            {'username': 'superman', 'activity_type': 'Strength Training', 'duration': 75.0, 'date': date(2024, 1, 15)},
            {'username': 'wonderwoman', 'activity_type': 'Cycling', 'duration': 80.0, 'date': date(2024, 1, 16)},
            {'username': 'theflash', 'activity_type': 'Running', 'duration': 30.0, 'date': date(2024, 1, 16)},
        ]
        for a in activities_data:
            Activity(**a).save()
        self.stdout.write(self.style.SUCCESS(f'  Created {len(activities_data)} activities'))

        self.stdout.write('Creating leaderboard...')
        leaderboard_data = [
            {'username': 'ironman', 'score': 450},
            {'username': 'batman', 'score': 430},
            {'username': 'captainamerica', 'score': 400},
            {'username': 'superman', 'score': 390},
            {'username': 'wonderwoman', 'score': 370},
            {'username': 'spiderman', 'score': 350},
            {'username': 'blackwidow', 'score': 320},
            {'username': 'theflash', 'score': 310},
        ]
        for l in leaderboard_data:
            Leaderboard(**l).save()
        self.stdout.write(self.style.SUCCESS(f'  Created {len(leaderboard_data)} leaderboard entries'))

        self.stdout.write('Creating workouts...')
        workouts_data = [
            {'name': 'Iron Man Power Circuit', 'description': 'High-intensity circuit training inspired by Tony Stark\'s suit-up routine.', 'duration': 45.0},
            {'name': 'Spider Agility Drill', 'description': 'Agility and flexibility drills inspired by your friendly neighbourhood Spider-Man.', 'duration': 30.0},
            {'name': 'Captain\'s Shield Strength', 'description': 'Upper-body strength workout inspired by Captain America\'s shield training.', 'duration': 60.0},
            {'name': 'Black Widow Stealth Yoga', 'description': 'Core-focused yoga session inspired by Natasha Romanoff\'s spy training.', 'duration': 50.0},
            {'name': 'Batman Cape Cardio', 'description': 'Gotham-style endurance run and combat conditioning.', 'duration': 60.0},
            {'name': 'Superman Strength & Fly', 'description': 'Full-body strength workout channelling the Man of Steel.', 'duration': 75.0},
            {'name': 'Wonder Woman Warrior Training', 'description': 'Amazonian warrior workout combining strength and endurance.', 'duration': 80.0},
            {'name': 'Flash Speed Intervals', 'description': 'Sprint intervals to channel your inner fastest man alive.', 'duration': 30.0},
        ]
        for w in workouts_data:
            Workout(**w).save()
        self.stdout.write(self.style.SUCCESS(f'  Created {len(workouts_data)} workouts'))

        self.stdout.write(self.style.SUCCESS('\nDatabase populated successfully with superhero test data!'))
