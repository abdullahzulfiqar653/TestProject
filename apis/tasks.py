from celery import shared_task
from apis.models import Task


@shared_task
def print_user_tasks():
    tasks = Task.objects.filter(user_id=1)

    for task in tasks:
        print(
            f"Task: {task.title}, Duration: {task.duration}, Created At: {task.created_at}"
        )
