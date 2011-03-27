from django import forms
from mongoengine.base import ValidationError

def mongoengine_validate_wrapper(old_clean, new_clean):
    """
    A wrapper function to validate formdata against mongoengine-field
    validator and raise a proper django.forms ValidationError if there
    are any problems.
    """

    def inner_validate(value):
        value = old_clean(value)
        try:
            new_clean(value)
            return value
        except ValidationError, e:
            raise forms.ValidationError(e)
    return inner_validate

def iter_valid_fields(meta):
    """walk through the available valid fields.."""

    # fetch field configuration and always add the id_field as exclude
    meta_fields = getattr(meta, 'fields', ())
    meta_exclude = getattr(meta, 'exclude', ()) + (meta.document._meta.get('id_field'),)
    # walk through the document fields
    for field_name, field in meta.document._fields.iteritems():
        # skip excluded or not explicit included fields
        if (meta_fields and field_name not in meta_fields) or field_name in meta_exclude:
            continue
        yield (field_name, field)
