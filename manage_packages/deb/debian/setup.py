from setuptools import setup, find_packages

setup(
    name="hello_world",
    version="0.0.1",
    author="Andrey Vorobev",
    author_email="andrey.vorobev.aqa@gmail.com",
    url="example.ru",
    description="A hello world example package",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operationg System :: OS Independent"
    ],
)