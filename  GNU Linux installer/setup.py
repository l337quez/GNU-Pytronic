#Setup para usar la libreria setuptools y generar RPM y DEB
#https://youtu.be/a9GzDZB5VeU    video guia
from setuptools import setup, find_packages
import sys

extra = {}
if sys.version_info <= (3,):
	extra['use_2to3']= True

setup(name="GNU pytronic",
      version= '0.1'
      url=
      description
      packages
      classifiers=[
          'Programming Language :: Python'
          'License :: GPL V3 '
          ],
      **extra






)
