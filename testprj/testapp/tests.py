from django.test.client import Client
from django.utils import unittest

from documents import Test001Parent

from testprj.tests import MongoengineTestCase


class MongoformsTests(MongoengineTestCase):
    
    def test001_possible_changes_loose_in_ReferenceField_clean_method(self):
        # drop any parent present
        Test001Parent.objects.delete()
        
        # prepare two test parents
        parent1 = Test001Parent(name='parent1')
        parent1.save()
        parent2 = Test001Parent(name='parent2')
        parent2.save()
        
        # prepare test client
        c = Client()
        
        # post form with first parent and empty name
        response = c.post('/test001/', {'parent': parent1.pk})
        
        # assert first parent is selected
        self.assertEqual(response.context['form'].data['parent'],
            unicode(parent1.pk), 'first parent must be selected')
        
        # post form with second parent and empty name
        response = c.post('/test001/', {'parent': parent2.pk})
        
        # assert second parent is selected
        self.assertEqual(response.context['form'].data['parent'],
            unicode(parent2.pk), 'second parent must be selected')
