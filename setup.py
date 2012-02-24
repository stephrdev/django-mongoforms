from setuptools import setup, find_packages
from setuptools.command.test import test
 
class TestRunner(test):
    
    def run(self):
        
        if self.distribution.install_requires:
            self.distribution.fetch_build_eggs(self.distribution.install_requires)
        if self.distribution.tests_require:
            self.distribution.fetch_build_eggs(self.distribution.tests_require)
        
        import sys
        sys.path.insert(0, 'testprj')
        
        from testprj import settings as test_settings
        from django.conf import settings
        settings.configure(test_settings)
        
        from testprj.tests import mongoforms_test_runner as test_runner
        
        test_suite = test_runner.build_suite(['testapp'])
        test_runner.setup_test_environment()
        result = test_runner.run_suite(test_suite)
        test_runner.teardown_test_environment()
        
        return result


setup(
    name='django-mongoforms',
    version='0.2',
    description='A Django-ModelForm clone for mongoengine',
    author='Stephan Jaekel',
    author_email='steph@rdev.info',
    maintainer='Serge Matveenko',
    maintainer_email='s@matveenko.ru',
    url='http://github.com/stephrdev/django-mongoforms/',
    packages=find_packages(exclude=['examples', 'examples.*', 'testprj', 'testprj.*']),
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
    cmdclass={"test": TestRunner}
)
