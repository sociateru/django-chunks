from setuptools import setup, find_packages

setup(name='django-chunks',
      version='0.4.1.2',
      description='Keyed blocks of content for use in your Django templates',
      author='Clint Ecker',
      author_email='me@clintecker.com',
      url='http://code.google.com/p/django-chunks/',
      packages=find_packages(),
      include_package_data=True,
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
      )
