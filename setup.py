import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="my-loc",
    version="0.1",
    author="Piyush Kumar",
    author_email="pk33463@gmail.com",
    description="A python package to get the location.",
    long_description= long_description,long_description_content_type="text/markdown",
    url="https://github.com/PIYUSH-GEEK/my_loc",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data = True,
    install_requires = ["requests"],

)