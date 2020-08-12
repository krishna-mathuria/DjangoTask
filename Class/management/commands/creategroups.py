 
"""
    PLEASE RUN THIS COMMAND ONLY AFTER DB MIGRATION HAS BEEN COMPLETED
    WHENEVER NUMBER OF USER ROLE INCREASES ADD HERE ALSO
"""
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group


class Command(BaseCommand):
    help = "Create different User groups"

    def handle(self, *args, **kwargs):
        """
            If number of groups increases in system do add here
        """
        group_list = [
            "Teacher",
            "Student",
            "Super-admin",
        ]
        for group in group_list:
            new_group, created = Group.objects.get_or_create(name=group)
        self.stdout.write("Groups has been created")