from setuptools import setup, find_packages
import os

CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
]

setup(
    author="Riccardo Forina",
    author_email="riccardo.forina@codingnot.es",
    name='django-admin-bootstrapped',
    version='0.3.1',
    description='A Bootstrap theme for Django Admin',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    url='https://github.com/riccardo-forina/django-admin-bootstrapped',
    license='BSD License',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    install_requires=[
        'setuptools',
        'Django>=1.4',
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False
)
