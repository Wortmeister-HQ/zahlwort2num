# zahlwort2num

A small but useful (due shortage of/low quality support for lang_DE) package for handy convertion of german numerals (also ordinal) written as words to numbers. 

This might be a good complementary lib to https://github.com/savoirfairelinux/num2words

_Currently is doesn't support swiss variant. TBD_

# Installation

`pip2 install zahlwort2num`

# Usage

Definition:
`import zahlwort2num as w2n`

Example: 
 `w2n.convert("zweihundertfünfundzwanzig") # => 225` <br />
 `w2n.convert("neunte") # => '9.'` <br />
 `w2n.convert("minus siebenhundert millionen achtundsiebzig") # => -700000078` <br />
 or even: <br />
 `w2n.convert("sechshundertdreiundfünfzigtausendfünfhunderteinundzwanzig"") # => 653521` :tada: 
 

# WIKI
TBD

# TODO / Known issues
- [x] Make POC, functional for all common cases
- [x] Ordinal number support 
- [x] Take care for exceptions / trailing whitespaces etc.
- [ ] Make structure + publish as PyPI package
- [ ] More comprehensible tests
- [ ] Swiss variant
- [ ] More fault tolerant (ß -> ss) etc
- [ ] Larger scale than 10^60
- [ ] Ordinal with very large numbers (without addons) e.g `Millionste`
- [ ] Few benchmark improvements (e.g tail recursion etc)
- [ ] Better error handling + validation for idiotical cases (e.g `minus null Miliarde`)
- [ ] Simplify/refactor POC code, add better documentation
