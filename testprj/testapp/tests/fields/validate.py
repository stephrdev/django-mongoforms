from decimal import Decimal

from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import *

from mongoforms.fields import MongoFormFieldGenerator

from testprj.tests import MongoengineTestCase


class _FieldValidateTestCase(MongoengineTestCase):

    # mongoengine field instance to test
    field_class = None
    # list of correct sample field values before and after clean
    correct_samples = ()
    # list of incorrect sample field values before clean
    incorrect_samples = ()
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

        # skip test as we have already tested this in render tests
        if self.is_not_implemented:
            return

        # test for correct samples
        for dirty_value, clean_value in self.correct_samples:
            self.assertEqual(
                clean_value,
                self.get_form_field().validate(dirty_value))

        # test for incorrect samples
        for value in self.incorrect_samples:
            self.assertRaises(
                ValidationError,
                lambda: self.get_form_field().validate(value))


class Test001StringFieldValidate(_FieldValidateTestCase):
    field_class = StringField
    correct_samples = [('test value', None)]


class Test002IntFieldValidate(_FieldValidateTestCase):
    field_class = IntField
    correct_samples = [('42', None)]


class Test003FloatFieldValidate(_FieldValidateTestCase):
    field_class = FloatField
    correct_samples = [('3.14', None)]


class Test004BooleanFieldValidate(_FieldValidateTestCase):
    field_class = BooleanField
    correct_samples = [('1', None), ('0', None)]


class Test005DateTimeFieldValidate(_FieldValidateTestCase):
    field_class = DateTimeField
    correct_samples = [('1970-01-02 03:04:05.678901', None)]


class Test006EmbeddedDocumentFieldValidate(_FieldValidateTestCase):
    is_not_implemented = True

    def get_field(self):

        class TestEmbeddedDocument(EmbeddedDocument):
            pass

        class TestDocument(Document):
            test_field = EmbeddedDocumentField(TestEmbeddedDocument)

        return TestDocument._fields['test_field']


class Test007ListFieldValidate(_FieldValidateTestCase):
    field_class = ListField
    is_not_implemented = True


class Test008DictFieldValidate(_FieldValidateTestCase):
    field_class = DictField
    is_not_implemented = True


class Test009ObjectIdFieldValidate(_FieldValidateTestCase):
    field_class = ObjectIdField
    is_not_implemented = True


class Test010ReferenceFieldValidate(_FieldValidateTestCase):
    correct_samples = []

    def get_field(self):

        class TestDocument(Document):
            test_field = ReferenceField('self')

        return TestDocument._fields['test_field']


class Test011MapFieldValidate(_FieldValidateTestCase):
    is_not_implemented = True

    def get_field(self):

        class TestDocument(Document):
            test_field = MapField(StringField())

        return TestDocument._fields['test_field']


class Test012DecimalFieldValidate(_FieldValidateTestCase):
    field_class = DecimalField
    correct_samples = [(Decimal('3.14'), Decimal('3.14'))]


class Test013ComplexDateTimeFieldValidate(_FieldValidateTestCase):
    field_class = ComplexDateTimeField
    is_not_implemented = True


class Test014URLFieldValidate(_FieldValidateTestCase):
    field_class = URLField
    correct_samples = [('http://www.example.com/', None)]


class Test015GenericReferenceFieldValidate(_FieldValidateTestCase):
    field_class = GenericReferenceField
    is_not_implemented = True


class Test016FileFieldValidate(_FieldValidateTestCase):
    field_class = FileField
    is_not_implemented = True


class Test017BinaryFieldValidate(_FieldValidateTestCase):
    field_class = BinaryField
    is_not_implemented = True


class Test018SortedListFieldValidate(_FieldValidateTestCase):
    is_not_implemented = True

    def get_field(self):

        class TestDocument(Document):
            test_field = SortedListField(StringField)

        return TestDocument._fields['test_field']


class Test019EmailFieldValidate(_FieldValidateTestCase):
    field_class = EmailField
    correct_samples = [('user@example.com', None)]


class Test020GeoPointFieldValidate(_FieldValidateTestCase):
    field_class = GeoPointField
    is_not_implemented = True


class Test021ImageFieldValidate(_FieldValidateTestCase):
    field_class = ImageField
    is_not_implemented = True


class Test022SequenceFieldValidate(_FieldValidateTestCase):
    field_class = SequenceField
    is_not_implemented = True


class Test023UUIDFieldValidate(_FieldValidateTestCase):
    field_class = UUIDField
    is_not_implemented = True


class Test024GenericEmbeddedDocumentFieldValidate(_FieldValidateTestCase):
    field_class = GenericEmbeddedDocumentField
    is_not_implemented = True
