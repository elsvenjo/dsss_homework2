from setuptools import setup, find_packages

setup(
    name="mathquiz",
    version="0.1.0",
    author="Sven Wolter",
    author_email="sven.wol@web.de",
    description="A simple math quiz game in Python",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/elsvenjo/dsss_homework2",
    packages=find_packages(),
    install_requires=[

    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)