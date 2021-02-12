from django.core.management.base import BaseCommand, CommandError
from userActivityRestApi.models import User, ActivityPeriod
from faker import Faker
from nanoid import generate
from datetime import datetime, timedelta
import random


def generateData(num):
    for i in range(num):
        fake = Faker()

        user = User.objects.create(
            id=generate(size=10),
            real_name=fake.name(),
            tz=fake.timezone()
        )
        print(user)

        # print(User.objects.get())

        activityPeriod1 = ActivityPeriod.objects.create(
            start_time=datetime.now(),
            end_time=datetime.now() + timedelta(random.randint(2, 9))
            user=user
        )
        print(activityPeriod1)

        activityPeriod2 = ActivityPeriod.objects.create(
            start_time=datetime.now(),
            end_time=datetime.now() + timedelta(random.randint(2, 9))
            user=user
        )
        print(activityPeriod2)

    return None


class Command(BaseCommand):
    help = 'populate dummy date into database'

    # capturing number of records to be created from input
    def add_arguments(self, parser):
        parser.add_argument('no_of_records',
                            nargs='+',
                            type=int)

    def handle(self, *args, **options):
        num = 5
        for no_of_records in options['no_of_records']:
            num = no_of_records
        try:
            print(num)
            generateData(num)
        except Exception as err:
            print(err)
            raise CommandError(
                'Error while generating data. Please try again!'
            )

        self.stdout.write(
            self.style.SUCCESS(
                'Successfully generated and inserted {} records'.format(no_of_records))
        )
