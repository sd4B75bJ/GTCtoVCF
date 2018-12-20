import os
import importlib
import importlib.util
import subprocess
import json
from setuptools import setup

def module_from_file(module_name, file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

package_name = 'gtctovcf'
here = os.path.dirname(os.path.abspath(__file__))
version_file = os.path.join(here, package_name, '__version__.py')

version_module = module_from_file('version', version_file)


setup(
    name=package_name,
    version=version_module.__version__,
    packages=[package_name],
    scripts=['{}/gtc_to_vcf.py'.format(package_name)],
    author='Ryan Kelley',
    url='https://github.com/Illumina/GTCtoVCF',
    author_email='rkelly@illumina.com',
    description='Convert GTC file to VCF format',
    test_suite='test',
    install_requires=[
        'pysam',
        'numpy',
        'pyvcf',
    ]
)
