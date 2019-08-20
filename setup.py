import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="myloc",
    version="1.1.1",
    author="Piyush Kumar",
    author_email="pk33463@gmail.com",
    description="A python package to get the location.",
    long_description= long_description,long_description_content_type="text/markdown",
    url="https://github.com/PIYUSH-GEEK/myloc",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages = ["my_loc"],
    include_package_data = True,
    install_requires = ["requests", "bs4"],

)
