# Django Import:
from django.db.models import Manager


# Managers class:
class Base(Manager):

    def get_queryset(self):
        return super(
            Base, self
        ).get_queryset().filter(deleted=False)


class ActiveManager(Manager):

    def get_queryset(self):
        return super(
            ActiveManager, self
        ).get_queryset().filter(deleted=False, status=1)