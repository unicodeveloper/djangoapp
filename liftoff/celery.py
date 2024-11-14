import os
from celery import Celery
from django.conf import settings

# Set the default Django settings module for the 'celery' program
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'liftoff.settings')

app = Celery('liftoff')

# Configure Celery to use Django settings with the 'CELERY' namespace
app.config_from_object('django.conf:settings', namespace='CELERY')

# Discover tasks in Django apps
app.autodiscover_tasks()

# Set timezone and disable UTC if preferred
app.conf.enable_utc = False
app.conf.timezone = 'Europe/London'  # Replace with your actual timezone, e.g., 'America/New_York'

# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     sender.add_periodic_task(300 ,runPeriodically.s(), name='Update Truck Locations Every 5 minutes')

# Example task (optional, for testing)
@app.task(bind=True)
def debug_task(self):
    print('This should execute whatever tasks')
