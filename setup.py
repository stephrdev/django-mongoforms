from setuptools import setup, find_packages

setup(
    name='django-mongoforms',
    version='0.1',
    description='A Django-ModelForm clone for mongoengine',
    author='Stephan Jaekel',
    author_email='steph@rdev.info',
    url='http://github.com/stephrdev/django-mongoforms/',
    packages=find_packages(exclude=['examples', 'examples.*']),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    zip_safe=False,
)
