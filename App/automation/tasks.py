# Celery Import:
from celery import shared_task

# Application Import:
from .models.automation_policy import *
from .models.relations import *
from .models.task_manager import *
from .models.template import *

@shared_task(bind=True, track_started=True)
def automation_task(self):
    print('Done')