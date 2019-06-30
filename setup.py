import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pyshopbase',
    version='0.0.1',
    author='Tan Le',
    author_email='tanle2207@gmail.com',
    description="Python Wrapper for Shopbase Api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/lephattan/pyshopbase',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent'
    ]
)
