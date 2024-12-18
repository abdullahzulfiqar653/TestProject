import time
from django.core.management.base import BaseCommand

from apis.models import Task


class Command(BaseCommand):
    help = "Prints all tasks in the database every 10 seconds"

    def handle(self, *args, **kwargs):
        tasks = Task.objects.all()
        for task in tasks:
            self.stdout.write(
                f"Task: {task.title}, Duration: {task.duration}, Created At: {task.created_at} by {task.user.username}"
            )
            time.sleep(10)
