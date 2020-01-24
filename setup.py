"""Setup file for the library"""
from setuptools import setup, find_packages

setup(
    name='testlibrary',
    version='0.1',
    description='This is a test for a tutorial on how to create a python library',  # noqa
    # url='git@github.com:dlopezco/test-lib.git',
    download_url='https://github.com/comparaonline/etl-builder/archive/v1.3.4.tar.gz',  # noqa
    author='Compara',
    author_email='bi@comparaonline.com',
    license='MIT',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
    ]
)