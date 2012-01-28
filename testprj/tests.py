import os, sys

from django.test.simple import DjangoTestSuiteRunner
from django.test.testcases import TestCase


class MongoengineDjangoTestSuiteRunner(DjangoTestSuiteRunner):
    
    def setup_databases(self, **kwargs):
        return None
    
    def teardown_databases(self, old_config, **kwargs):
        pass


class MongoengineTestCase(TestCase):
    """ completely dummy test case class """
    
    def setUp(self):
        TestCase.setUp(self)
    
    def _fixture_setup(self):
        pass
    
    def _fixture_teardown(self):
        pass


mongoforms_test_runner = MongoengineDjangoTestSuiteRunner(
    verbosity=1,
    interactive=True,
    failfast=True)
