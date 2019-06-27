from setuptools import setup

version = 'V1.0.0'


setup(
    name='howfoFrame',
    description='howfoFrame 一款基于flask的小型自定义框架',
    version=version,
    packages=['vendor',
              'vendor.Base',
              'vendor.Config',
              'vendor.Db',
              'vendor.Log'],
    tests_require=['pytest'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)

