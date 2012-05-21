from django.utils import unittest
from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import *

from mongoforms import MongoForm

from testprj.tests import MongoengineTestCase


class MongoformsFieldRenderTest(MongoengineTestCase):
    field = None  # mongoengine field instance to test
    rendered_widget = None  # widget rendering result

    def runTest(self):

        class TestDocument(Document):
            test_field = self.field

        class TestForm(MongoForm):
            class Meta:
                document = TestDocument
                fields = ['test_field']

        form = TestForm()
        self.assertMultiLineEqual(
            self.rendered_widget,
            form.fields['test_field'].widget.render())


class Test001StringField(MongoformsFieldRenderTest):
    field = StringField()
    rendered_widget = ''


class Test002IntField(MongoformsFieldRenderTest):
    field = IntField()
    rendered_widget = ''


class Test003FloatField(MongoformsFieldRenderTest):
    field = FloatField()
    rendered_widget = ''


class Test004BooleanField(MongoformsFieldRenderTest):
    field = BooleanField()
    rendered_widget = ''


class Test005DateTimeField(MongoformsFieldRenderTest):
    field = DateTimeField()
    rendered_widget = ''


class Test006EmbeddedDocumentField(MongoformsFieldRenderTest):
    field = EmbeddedDocumentField(EmbeddedDocument)
    rendered_widget = ''


class Test007ListField(MongoformsFieldRenderTest):
    field = ListField()
    rendered_widget = ''


class Test008DictField(MongoformsFieldRenderTest):
    field = DictField()
    rendered_widget = ''


class Test009ObjectIdField(MongoformsFieldRenderTest):
    field = ObjectIdField()
    rendered_widget = ''


class Test010ReferenceField(MongoformsFieldRenderTest):
    field = ReferenceField('self')
    rendered_widget = ''


class Test011MapField(MongoformsFieldRenderTest):
    field = MapField(StringField())
    rendered_widget = ''


class Test012DecimalField(MongoformsFieldRenderTest):
    field = DecimalField()
    rendered_widget = ''


class Test013ComplexDateTimeField(MongoformsFieldRenderTest):
    field = ComplexDateTimeField()
    rendered_widget = ''


class Test014URLField(MongoformsFieldRenderTest):
    field = URLField()
    rendered_widget = ''


class Test015GenericReferenceField(MongoformsFieldRenderTest):
    field = GenericReferenceField()
    rendered_widget = ''


class Test016FileField(MongoformsFieldRenderTest):
    field = FileField()
    rendered_widget = ''


class Test017BinaryField(MongoformsFieldRenderTest):
    field = BinaryField()
    rendered_widget = ''


class Test018SortedListField(MongoformsFieldRenderTest):
    field = SortedListField(StringField)
    rendered_widget = ''


class Test019EmailField(MongoformsFieldRenderTest):
    field = EmailField()
    rendered_widget = ''


class Test020GeoPointField(MongoformsFieldRenderTest):
    field = GeoPointField()
    rendered_widget = ''


class Test021ImageField(MongoformsFieldRenderTest):
    field = ImageField()
    rendered_widget = ''


class Test022SequenceField(MongoformsFieldRenderTest):
    field = SequenceField()
    rendered_widget = ''


class Test023UUIDField(MongoformsFieldRenderTest):
    field = UUIDField()
    rendered_widget = ''


class Test024GenericEmbeddedDocumentField(MongoformsFieldRenderTest):
    field = GenericEmbeddedDocumentField()
    rendered_widget = ''


MongoformsFieldsRender = unittest.TestSuite([
    Test001StringField(), Test002IntField(), Test003FloatField(),
    Test004BooleanField(), Test005DateTimeField(),
    Test006EmbeddedDocumentField(), Test007ListField(), Test008DictField(),
    Test009ObjectIdField(), Test010ReferenceField(), Test011MapField(),
    Test012DecimalField(), Test013ComplexDateTimeField(), Test014URLField(),
    Test015GenericReferenceField(), Test016FileField(), Test017BinaryField(),
    Test018SortedListField(), Test019EmailField(), Test020GeoPointField(),
    Test021ImageField(), Test022SequenceField(), Test023UUIDField(),
    Test024GenericEmbeddedDocumentField()])
