from setuptools import setup

requires = [
    'pymemcache==2.1.1',
    'redis==3.1.0',
    'six==1.12.0'
]

extras_require = {
    'test': [
        'pytest==4.2.1',
        'pytest-mock==1.10.1',
        'pytest-cov==2.5.1',
    ],
    'ci': [
        'python-coveralls==2.9.1',
    ]
}

with open('README.md') as f:
    long_description = f.read()

setup(
    name='scrooge_cache',
    version='0.1.1',
    description='Scrooge Cache',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
    author='Marcelo Moraes',
    author_email='marcelomoraesjr28@gmail.com',
    url='https://github.com/marcelomoraes28/scrooge_cache',
    keywords='cache scrooge redis memcache',
    include_package_data=True,
    zip_safe=False,
    extras_require=extras_require,
    install_requires=requires,
    packages=['scrooge']
)
