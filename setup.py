import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="zahlwort2num",
    version="0.1.2",
    author="Piotr Walkowski",
    author_email="piotr@deluxe-soft.com",
    description="A small package for handy conversion of german numerals (also ordinal / signed) written as words to numbers.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/walu2/zahlwort2num",
    packages=setuptools.find_packages(),
    zip_safe = False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

