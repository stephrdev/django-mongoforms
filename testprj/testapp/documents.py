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
