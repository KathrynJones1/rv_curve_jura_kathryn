import setuptools

setuptools.setup(
	name="rv_curve_jurapackage",
	version="0.1",
	author="Kathryn Jones",
	author_email="kathryn.jones@unibe.ch",
	description="Plot all RV curves that you want!",
	packages=setuptools.find_packages(),
	install_requires=["numpy", "matplotlib"],
	classifiers=["Programming Language :: Python :: 3"],
)
