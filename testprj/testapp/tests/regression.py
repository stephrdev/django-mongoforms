from django.test.client import Client

from ..documents import Test001Parent
from ..forms import (Test002StringFieldForm, Test003FormFieldOrder,
    Test004StringFieldForm)

from testprj.tests import MongoengineTestCase


class MongoformsRegressionTests(MongoengineTestCase):

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

    def test002_issue_13_StringField_problem(self):
        form = Test002StringFieldForm(
            {'string_field_1': 'M', 'string_field_2': 'S'})
        self.assertTrue(form.is_valid())
        self.assertEqual('M', form.cleaned_data['string_field_1'])
        self.assertEqual('S', form.cleaned_data['string_field_2'])

    def test003_issue_19_form_field_order(self):
        form = Test003FormFieldOrder()
        self.assertListEqual(
            ['username', 'email', 'password', 'repeat_password'],
            form.fields.keys())

    def test004_issue_23_StringField_regex(self):
        form = Test004StringFieldForm({'string_field_3': 'testbar',})
        self.assertTrue(form.is_valid())
        self.assertEqual('testbar', form.cleaned_data['string_field_3'])

    def test004_issue_23_StringField_regex_fail(self):
        form = Test004StringFieldForm({'string_field_3': 'foobar',})
        self.assertFalse(form.is_valid())
