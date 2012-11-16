from setuptools import setup, find_packages

setup(
    name='django_admin_bootstrapped',
    version=0.0,
    author='Riccardo Forina',
    author_email='',
    url='https://github.com/riccardo-forina/django-admin-bootstrapped',
    install_requires=[
        'setuptools',
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
