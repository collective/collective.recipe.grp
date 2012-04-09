from setuptools import find_packages
from setuptools import setup
import os

VERSION = '1.1.0'


setup(
    author='Alex Clark',
    author_email='aclark@aclark.net',
    description="A window unto Python's Standard Library grp function",
    entry_points={
        'zc.buildout': 'default = collective.recipe.grp:Recipe',
    },
    include_package_data=True,
    install_requires=[
        'setuptools',
        'zc.buildout',
    ],
    long_description=(
        open('README.rst').read() +
        open(os.path.join('docs', 'HISTORY.txt')).read()
    ),
    classifiers=[
        'Framework :: Buildout',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: Zope Public License',
    ],
    keywords='buildout group id unix',
    license='ZPL',
    name='collective.recipe.grp',
    namespace_packages=[
        'collective',
        'collective.recipe'
    ],
    packages=find_packages(),
    url='http://collective.github.com/collective.recipe.grp/',
    version=VERSION,
    zip_safe=False,
)
