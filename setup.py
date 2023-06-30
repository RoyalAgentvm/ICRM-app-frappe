from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in icrm/__init__.py
from icrm import __version__ as version

setup(
	name="icrm",
	version=version,
	description="Api for mobile app",
	author="Roy Muraya",
	author_email="roy.m.githaiga@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
