from setuptools import setup, find_packages

packages = find_packages(exclude=('pyoat.tests*', 'pyoat.*.tests*'))

setup(
	name="pyoat",
	version="1.0.0",
	description = "Data processing tools for optoacoustic tomography (OAT)",
	author = "Berkan Lafci",
	author_email = "lafciberkan@gmail.com",
	url = "https://github.com/berkanlafci/pyoat",
	keywords = ["optoacoustic tomography", "image reconstruction", "data analysis"],
	classifiers = [],
	install_requires = ['numpy', 'matplotlib', 'scipy', 'h5py', 'Pillow'],
	provides = ["pyoat"],
	packages = packages,
	include_package_data=True,
	extras_require = {},
	entry_points = {},
	)
