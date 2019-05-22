import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='zahlwort2num',
    version='0.2.1',
    author='Piotr Walkowski',
    author_email='piotr@deluxe-soft.com',
    description='A small package for handy conversion of german numerals (also ordinal / signed) written as words to numbers.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/walu2/zahlwort2num',
    packages=setuptools.find_packages(),
    keywords='german nlp numeral converter deutsch sprache ordinal zahlen human number',
    install_requires=[
          'markdown',
    ],
    zip_safe = False,
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Text Processing :: Linguistic',
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
    scripts=['bin/zahlwort2num-convert'],
    entry_points = {
        'console_scripts': ['zahlwort2num-covert=zahlwort2num.command_line:main'],
    }
)