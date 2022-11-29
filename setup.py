from glob import glob
from os import read
from os.path import basename, splitext
from setuptools import find_packages, setup

setup(
	name="C-PyUtils",
	version="0.0.1",
	long_description=read('README.md'),
	url="https://github.com/skdkfk8758/C-PyUtils.git",
	author="CarpDm",
	author_email="skdkfk8758@gmail.com",
	license="CarpDm",
	packages=find_packages(where='src'),
	package_dir={'': 'src'},
	py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
	install_requires=[

	]
)