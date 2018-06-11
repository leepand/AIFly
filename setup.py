from setuptools import setup, find_packages

import AIFlysdk
import AIFlylocal
VERSION = AIFlysdk.__version__

setup(name='AIFly',
      version=VERSION,
      description='AIFly Server and AIFly SDK',
      author='ML Platform Dev Team @wanda',
      license='Apache-2.0',
      packages=find_packages(exclude=['contrib', 'docs', 'tests']),
      install_requires=['requests', 'retrying', 'simplejson']
      )