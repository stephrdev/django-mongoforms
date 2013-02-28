from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import *

from mongoforms.fields import MongoFormFieldGenerator

from testprj.tests import MongoengineTestCase


class _FieldRenderTestCase(MongoengineTestCase):
    # mongoengine field instance to test
    field_class = None
    # widget rendering result (most common value)
    rendered_widget = '<input name="test_field" type="text" />'
    # hook for not implemented fields
    is_not_implemented = False

    def setUp(self):
        self.generator = MongoFormFieldGenerator()

    def get_field(self):

        class TestDocument(Document):
            test_field = self.field_class()

        return TestDocument._fields['test_field']

    def get_form_field(self):
        return self.generator.generate('test_field', self.get_field())

    def runTest(self):

        if self.is_not_implemented:
            self.assertRaises(NotImplementedError, self.get_form_field)
        else:
            self.assertMultiLineEqual(
                self.rendered_widget,
                self.get_form_field().widget.render('test_field', None))


class Test001StringFieldRender(_FieldRenderTestCase):
    field_class = StringField
    rendered_widget = \
        '<textarea cols="40" name="test_field" rows="10">\r\n</textarea>'


class Test002IntFieldRender(_FieldRenderTestCase):
    field_class = IntField


class Test003FloatFieldRender(_FieldRenderTestCase):
    field_class = FloatField


class Test004BooleanFieldRender(_FieldRenderTestCase):
    field_class = BooleanField
    rendered_widget = \
        '<input name="test_field" type="checkbox" />'


class Test005DateTimeFieldRender(_FieldRenderTestCase):
    field_class = DateTimeField


class Test006EmbeddedDocumentFieldRender(_FieldRenderTestCase):
    is_not_implemented = True

    def get_field(self):

        class TestEmbeddedDocument(EmbeddedDocument):
            pass

        class TestDocument(Document):
            test_field = EmbeddedDocumentField(TestEmbeddedDocument)

        return TestDocument._fields['test_field']


class Test007ListFieldRender(_FieldRenderTestCase):
    field_class = ListField
    is_not_implemented = True


class Test008DictFieldRender(_FieldRenderTestCase):
    field_class = DictField
    is_not_implemented = True


class Test009ObjectIdFieldRender(_FieldRenderTestCase):
    field_class = ObjectIdField
    is_not_implemented = True


class Test010ReferenceFieldRender(_FieldRenderTestCase):
    rendered_widget = \
        '<select name="test_field">\n</select>'

    def get_field(self):

        class TestDocument(Document):
            test_field = ReferenceField('self')

        return TestDocument._fields['test_field']


class Test011MapFieldRender(_FieldRenderTestCase):
    is_not_implemented = True

    def get_field(self):

        class TestDocument(Document):
            test_field = MapField(StringField())

        return TestDocument._fields['test_field']


class Test012DecimalFieldRender(_FieldRenderTestCase):
    field_class = DecimalField


class Test013ComplexDateTimeFieldRender(_FieldRenderTestCase):
    field_class = ComplexDateTimeField
    is_not_implemented = True


class Test014URLFieldRender(_FieldRenderTestCase):
    field_class = URLField


class Test015GenericReferenceFieldRender(_FieldRenderTestCase):
    field_class = GenericReferenceField
    is_not_implemented = True


class Test016FileFieldRender(_FieldRenderTestCase):
    field_class = FileField
    is_not_implemented = True


class Test017BinaryFieldRender(_FieldRenderTestCase):
    field_class = BinaryField
    is_not_implemented = True


class Test018SortedListFieldRender(_FieldRenderTestCase):
    is_not_implemented = True

    def get_field(self):

        class TestDocument(Document):
            test_field = SortedListField(StringField)

        return TestDocument._fields['test_field']


class Test019EmailFieldRender(_FieldRenderTestCase):
    field_class = EmailField


class Test020GeoPointFieldRender(_FieldRenderTestCase):
    field_class = GeoPointField
    is_not_implemented = True


class Test021ImageFieldRender(_FieldRenderTestCase):
    field_class = ImageField
    is_not_implemented = True


class Test022SequenceFieldRender(_FieldRenderTestCase):
    field_class = SequenceField
    is_not_implemented = True


class Test023UUIDFieldRender(_FieldRenderTestCase):
    field_class = UUIDField
    is_not_implemented = True


class Test024GenericEmbeddedDocumentFieldRender(_FieldRenderTestCase):
    field_class = GenericEmbeddedDocumentField
    is_not_implemented = True
