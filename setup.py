"""
Author : Utkarsh Kumar Mahawar
"""

from setuptools import setup, find_packages

setup(
    # name of package on PyPi
    name='fnexchange-jira',
    version='0.1.1',

    # URL to your repo (if open source)
    #url='http://github.com/bhumilharia/fnexchange-slack',

    license='Apache',

    # your name
    author='utkarsh',

    # your email here
    author_email='bhumilharia@gmail.com',
    description='fnExchange plugin for Slack integration',
    long_description=__doc__,
    keywords='fnexchange plugin',

    # if cross-platform
    platforms='any',

    # add your dependencies here
    install_requires=[
        'fnexchange',
        'requests>=2.4.2',
    ],

    py_modules=['fnexchange_jira'],
    include_package_data=True,
    zip_safe=False,

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers for a full list
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
)
