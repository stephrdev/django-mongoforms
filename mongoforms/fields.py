from django import forms
from django.utils.encoding import smart_unicode
from bson.errors import InvalidId
from bson.objectid import ObjectId


class ReferenceField(forms.ChoiceField):
    """
    Reference field for mongo forms. Inspired by `django.forms.models.ModelChoiceField`.
    """
    def __init__(self, queryset, *aargs, **kwaargs):
        forms.Field.__init__(self, *aargs, **kwaargs)
        self.queryset = queryset

    def _get_queryset(self):
        return self._queryset

    def _set_queryset(self, queryset):
        self._queryset = queryset
        self.widget.choices = self.choices

    queryset = property(_get_queryset, _set_queryset)

    def _get_choices(self):
        if hasattr(self, '_choices'):
            return self._choices

        self._choices = [(obj.id, smart_unicode(obj)) for obj in self.queryset]
        return self._choices

    choices = property(_get_choices, forms.ChoiceField._set_choices)

    def clean(self, value):
        try:
            oid = ObjectId(value)
            oid = super(ReferenceField, self).clean(oid)
            if 'id' in self.queryset._query_obj.query:
                obj = self.queryset.get()
            else:
                obj = self.queryset.get(id=oid)
        except (TypeError, InvalidId, self.queryset._document.DoesNotExist):
            raise forms.ValidationError(self.error_messages['invalid_choice'] % {'value':value})
        return obj


class MongoFormFieldGenerator(object):
    """This class generates Django form-fields for mongoengine-fields."""

    def generate(self, field_name, field):
        """Tries to lookup a matching formfield generator (lowercase
        field-classname) and raises a NotImplementedError of no generator
        can be found.
        """

        if hasattr(self, 'generate_%s' % field.__class__.__name__.lower()):
            generator = getattr(
                self,
                'generate_%s' % field.__class__.__name__.lower())
            return generator(
                field_name,
                field,
                (field.verbose_name or field_name).capitalize())
        else:
            raise NotImplementedError('%s is not supported by MongoForm' % \
                field.__class__.__name__)

    def generate_stringfield(self, field_name, field, label):

        if field.regex:
            return forms.CharField(
                label=label,
                regex=field.regex,
                required=field.required,
                min_length=field.min_length,
                max_length=field.max_length,
                initial=field.default)
        elif field.choices:
            choices = tuple(field.choices)
            if not isinstance(field.choices[0], (tuple, list)):
                choices = zip(choices, choices)
            return forms.ChoiceField(
                label=label,
                required=field.required,
                initial=field.default,
                choices=choices)
        elif field.max_length is None:
            return forms.CharField(
                label=label,
                required=field.required,
                initial=field.default,
                min_length=field.min_length,
                widget=forms.Textarea)
        else:
            return forms.CharField(
                label=label,
                required=field.required,
                min_length=field.min_length,
                max_length=field.max_length,
                initial=field.default)

    def generate_emailfield(self, field_name, field, label):
        return forms.EmailField(
            label=label,
            required=field.required,
            min_length=field.min_length,
            max_length=field.max_length,
            initial=field.default)

    def generate_urlfield(self, field_name, field, label):
        return forms.URLField(
            label=label,
            required=field.required,
            min_length=field.min_length,
            max_length=field.max_length,
            initial=field.default)

    def generate_intfield(self, field_name, field, label):
        return forms.IntegerField(
            label=label,
            required=field.required,
            min_value=field.min_value,
            max_value=field.max_value,
            initial=field.default)

    def generate_floatfield(self, field_name, field, label):
        return forms.FloatField(
            label=label,
            required=field.required,
            min_value=field.min_value,
            max_value=field.max_value,
            initial=field.default)

    def generate_decimalfield(self, field_name, field, label):
        return forms.DecimalField(
            label=label,
            required=field.required,
            min_value=field.min_value,
            max_value=field.max_value,
            initial=field.default)

    def generate_booleanfield(self, field_name, field, label):
        return forms.BooleanField(
            label=label,
            required=field.required,
            initial=field.default)

    def generate_datetimefield(self, field_name, field, label):
        return forms.DateTimeField(
            label=label,
            required=field.required,
            initial=field.default)

    def generate_referencefield(self, field_name, field, label):
        return ReferenceField(
            field.document_type.objects,
            label=label)
