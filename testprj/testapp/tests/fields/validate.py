from django.utils import unittest
from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import *

from mongoforms import MongoForm

from testprj.tests import MongoengineTestCase


class MongoformsFieldValidateTest(MongoengineTestCase):
    field = None  # mongoengine field instance to test
    correct_samples = None  # list of correct sample field values
    incorrect_samples = None  # list of incorrect sample field values

    def runTest(self):

        class TestDocument(Document):
            test_field = self.field

        class TestForm(MongoForm):
            class Meta:
                document = TestDocument
                fields = ['test_field']

        for sample in self.correct_samples:
            form = TestForm({'test_field': sample})
            self.assertTrue(form.is_valid())

        for sample in self.incorrect_samples:
            form = TestForm({'test_field': sample})
            self.assertFalse(form.is_valid())


class Test001StringField(MongoformsFieldValidateTest):
    field = StringField()
    correct_samples = []
    incorrect_samples = []


class Test002IntField(MongoformsFieldValidateTest):
    field = IntField()
    correct_samples = []
    incorrect_samples = []


class Test003FloatField(MongoformsFieldValidateTest):
    field = FloatField()
    correct_samples = []
    incorrect_samples = []


class Test004BooleanField(MongoformsFieldValidateTest):
    field = BooleanField()
    correct_samples = []
    incorrect_samples = []


class Test005DateTimeField(MongoformsFieldValidateTest):
    field = DateTimeField()
    correct_samples = []
    incorrect_samples = []


class Test006EmbeddedDocumentField(MongoformsFieldValidateTest):
    field = EmbeddedDocumentField(EmbeddedDocument)
    correct_samples = []
    incorrect_samples = []


class Test007ListField(MongoformsFieldValidateTest):
    field = ListField()
    correct_samples = []
    incorrect_samples = []


class Test008DictField(MongoformsFieldValidateTest):
    field = DictField()
    correct_samples = []
    incorrect_samples = []


class Test009ObjectIdField(MongoformsFieldValidateTest):
    field = ObjectIdField()
    correct_samples = []
    incorrect_samples = []


class Test010ReferenceField(MongoformsFieldValidateTest):
    field = ReferenceField('self')
    correct_samples = []
    incorrect_samples = []


class Test011MapField(MongoformsFieldValidateTest):
    field = MapField(StringField())
    correct_samples = []
    incorrect_samples = []


class Test012DecimalField(MongoformsFieldValidateTest):
    field = DecimalField()
    correct_samples = []
    incorrect_samples = []


class Test013ComplexDateTimeField(MongoformsFieldValidateTest):
    field = ComplexDateTimeField()
    correct_samples = []
    incorrect_samples = []


class Test014URLField(MongoformsFieldValidateTest):
    field = URLField()
    correct_samples = []
    incorrect_samples = []


class Test015GenericReferenceField(MongoformsFieldValidateTest):
    field = GenericReferenceField()
    correct_samples = []
    incorrect_samples = []


class Test016FileField(MongoformsFieldValidateTest):
    field = FileField()
    correct_samples = []
    incorrect_samples = []


class Test017BinaryField(MongoformsFieldValidateTest):
    field = BinaryField()
    correct_samples = []
    incorrect_samples = []


class Test018SortedListField(MongoformsFieldValidateTest):
    field = SortedListField(StringField)
    correct_samples = []
    incorrect_samples = []


class Test019EmailField(MongoformsFieldValidateTest):
    field = EmailField()
    correct_samples = []
    incorrect_samples = []


class Test020GeoPointField(MongoformsFieldValidateTest):
    field = GeoPointField()
    correct_samples = []
    incorrect_samples = []


class Test021ImageField(MongoformsFieldValidateTest):
    field = ImageField()
    correct_samples = []
    incorrect_samples = []


class Test022SequenceField(MongoformsFieldValidateTest):
    field = SequenceField()
    correct_samples = []
    incorrect_samples = []


class Test023UUIDField(MongoformsFieldValidateTest):
    field = UUIDField()
    correct_samples = []
    incorrect_samples = []


class Test024GenericEmbeddedDocumentField(MongoformsFieldValidateTest):
    field = GenericEmbeddedDocumentField()
    correct_samples = []
    incorrect_samples = []


MongoformsFieldsValidate = unittest.TestSuite([
    Test001StringField(), Test002IntField(), Test003FloatField(),
    Test004BooleanField(), Test005DateTimeField(),
    Test006EmbeddedDocumentField(), Test007ListField(), Test008DictField(),
    Test009ObjectIdField(), Test010ReferenceField(), Test011MapField(),
    Test012DecimalField(), Test013ComplexDateTimeField(), Test014URLField(),
    Test015GenericReferenceField(), Test016FileField(), Test017BinaryField(),
    Test018SortedListField(), Test019EmailField(), Test020GeoPointField(),
    Test021ImageField(), Test022SequenceField(), Test023UUIDField(),
    Test024GenericEmbeddedDocumentField()])
