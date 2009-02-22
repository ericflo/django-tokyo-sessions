from setuptools import setup, find_packages
 
version = '0.1.0'
 
LONG_DESCRIPTION = """
django-tokyo-sessions
=======================

This is a session backend for Django that stores sessions in a Tokyo Cabinet
database, which communicates via Tokyo Tyrant using the PyTyrant library.  Tokyo
Cabinet is a key-value store similar to BDB.

The advantage to using this over other solutions is that your data is persistent
unlike memcached, and Tokyo Cabinet is designed to store key-value data like
this, so performance is much closer to that of memcached than with a database.

Installing django-tokyo-sessions
-----------------------------------

1. Either download the tarball and run ``python setup.py install``, or simply
   use easy install or pip like so ``easy_install django-tokyo-sessions``.


2. Set ``tokyo_sessions.tokyo`` as your session engine, like so::

       SESSION_ENGINE = 'tokyo_sessions.tokyo'


3. Add settings describing where to connect to the Tokyo Tyrant database::

       TT_HOST = '127.0.0.1'
       TT_PORT = 1978


That's it.  Hopefully this backend gives you all the better performance while
still not sacrificing persistence.
"""
 
setup(
    name='django-tokyo-sessions',
    version=version,
    description="This is a session backend for Django that stores sessions in a Tokyo Cabinet database, which communicates via Tokyo Tyrant using the PyTyrant library.  Tokyo Cabinet is a key-value store similar to BDB.",
    long_description=LONG_DESCRIPTION,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
    keywords='tokyo,session,cabinet,tyrant,pytyrant,django',
    author='Eric Florenzano',
    author_email='floguy@gmail.com',
    url='http://github.com/ericflo/django-tokyo-sessions/tree/master',
    license='BSD',
    packages=find_packages(),
    zip_safe=False,
    install_requires=['setuptools'],
    include_package_data=True,
    setup_requires=['setuptools_git'],
)