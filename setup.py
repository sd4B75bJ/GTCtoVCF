import os
import subprocess
import json
from setuptools import setup

PACKAGE_NAME = 'GTCtoVCF'

here = os.path.dirname(os.path.abspath(__file__))


def absolute_version():
    """
    Gets the absolute version of this package by inspecting details of GIT.
    Requires that the script is placed in the same directory as .git.

    Falls back to 'localbuild' if not GIT information could be obtained.
    :return:
    """

    def check_output(cmd):
        stdout = subprocess.check_output(cmd, cwd=here)
        return stdout.strip().decode()

    try:
        tag = check_output(["git", "describe", "--tags", "--long"])
        branch = check_output(["git", "symbolic-ref", "--short", "HEAD"])
        return "{}-{}".format(tag, branch)
    except subprocess.CalledProcessError:
        try:
            commit = check_output(['git', 'rev-parse', 'HEAD'])
            return commit
        except subprocess.CalledProcessError:
            return 'develop'


def write_version_file(version_str):
    with open(os.path.join(here, PACKAGE_NAME, '__version__.py'), 'w') as f:
        f.write('__version__ = {}\n'.format(json.dumps(version_str)))


package_version = absolute_version()
write_version_file(package_version)

setup(
    name=PACKAGE_NAME,
    version=package_version,
    packages=[PACKAGE_NAME],
    scripts=['{}/gtc_to_vcf.py'.format(PACKAGE_NAME)],
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
