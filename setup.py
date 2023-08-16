from setuptools import setup

setup(
    name='arstats',
    version='1.2.0',
    packages=['arstats'],
    url='https://github.com/philhanna/parstats',
    license='MIT',
    author='Phil Hanna',
    author_email='ph1204@gmail.com',
    description='Displays statistics for Linux Aisleriot card games',
    install_requires=[
        'pytest',
    ],
)
