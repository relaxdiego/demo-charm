import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="demo-charm-mmaglana",
    version="0.0.1",
    author="Mark S. Maglana",
    author_email="mmaglana@gmail.com",
    description="A demo project for trying out the Operator Framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/relaxdiego/demo-charm",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
