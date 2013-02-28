from mongoengine import *


class Test001Parent(Document):
    name = StringField(required=True)
    
    def __unicode__(self):
        return u'%s' % self.name


class Test001Child(Document):
    parent = ReferenceField(Test001Parent, required=True)
    name = StringField(required=True)
    
    def __unicode__(self):
        return u'%s' % self.name


class Test002StringField(Document):
    string_field_1 = StringField(choices=(
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
        ('XXL', 'Extra Extra Large')))
    string_field_2 = StringField(choices=('S', 'M', 'L', 'XL', 'XXL'))
    string_field_3 = StringField(regex=r'^test.*$')
