from django.forms import CharField, PasswordInput
from mongoengine.django.auth import User

from mongoforms import MongoForm

from documents import Test001Child, Test002StringField


class Test001ChildForm(MongoForm):
    class Meta:
        document = Test001Child
        fields = ('parent', 'name')


class Test002StringFieldForm(MongoForm):
    class Meta:
        document = Test002StringField
        fields = ('string_field_1', 'string_field_2')


class Test003FormFieldOrder(MongoForm):
    class Meta:
        document = User
        fields = ('username', 'email', 'password')
    password = CharField(widget=PasswordInput, label="Your password")
    repeat_password = CharField(widget=PasswordInput, label="Repeat password")
