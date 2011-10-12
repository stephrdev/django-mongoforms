from mongoforms import MongoForm

from documents import Test001Child


class Test001ChildForm(MongoForm):
    class Meta:
        document = Test001Child
        fields = ('parent', 'name')
