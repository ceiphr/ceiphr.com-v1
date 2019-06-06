from django.test import TestCase
import datetime

from .models import Profile, Project

class ProjectModelTests(TestCase):

    def test_start_date_before_end_date(self):
        
        nonlinear_date_project = Project(start_date=datetime.date(2008, 1, 1), end_date=datetime.date(1979, 1, 1))
        self.assertIs(nonlinear_date_project.linear_dates(), False)
