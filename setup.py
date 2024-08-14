"""
File containing the required information to successfully build a python package
"""

import setuptools

with open("README.md", "r", encoding="utf-8", newline="\n") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pet_bit_melody',
    version='1.0.0',
    packages=setuptools.find_packages(),
    install_requires=[
    ],
    author="Henry Letellier",
    author_email="henrysoftwarehouse@protonmail.com",
    description="This is a music player/composer for 8, 16, 32 bit and piano cord music.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Hanra-s-work/pet_bit_melody",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
