import sys


from setuptools import setup, find_packages


dependencies = [
    'PyYAML~=3.12',
    'confluent-kafka~=0.9',
]

if sys.version_info[0] == 2:
    dependencies.append('ipaddr~=2.1.11')


setup(
    name='libtervis',
    version='0.1.0.dev0',
    url='http://github.com/getsentry/libtervis',
    license='BSD',
    author='Sentry',
    author_email='hello@getsentry.com',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=dependencies,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
