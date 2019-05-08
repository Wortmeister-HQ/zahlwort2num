# zahlwort2num (v. 0.1.9)

:de: :de: :de:
A small but useful (due shortage of/low quality support for lang_DE) package for handy conversion of german numerals (incl. ordinal number) written as string to the from numbers. 

To put it differently: _It allows reverse text normalization for numbers._

This package might be a good complementary lib to https://github.com/savoirfairelinux/num2words

:crying_cat_face: _Currently is doesn't support swiss variant. TBD_ :switzerland:

# PyPi direct page of project 
https://pypi.org/project/zahlwort2num/

# Installation

`pip2 install zahlwort2num`

# Usage

### _Definition_: <br />

```python
import zahlwort2num as w2n
```

### _Example_: <br />
 ```python
 w2n.convert("Zweihundertfünfundzwanzig") # => 225
 w2n.convert("neunte") # => '9.' 
 w2n.convert("minus siebenhundert Millionen achtundsiebzig") # => -700000078
```
 _or even stuff like:_ <br />
 ```python
 w2n.convert("sechshundertdreiundfünfzigtausendfünfhunderteinundzwanzig") # => 653521
```
 :see_no_evil: 
 
#### Command line: 

* _(Obviously it is better to use a parameter enclosed with apostrophs due to possible spaces)_
```
bin/zahlwort2num-convert "eine Million siebenhunderteinundzwanzig"
```
# WIKI
TBD

# Already implemented features :sunglasses:
* Theoretically it works for any numbers from range 0 upto 999 * 10^27 [big numbers]
* Command-line mode ([see](#command-line) above)
* Supported with ordinal numerals (incl. inflections [sufficies like `'ste', 'ten'` etc. ])<br />
  _In this case it returns coerced __String__ type value e.g '15.' instead of __Integer___ :point_up: 
* Relative mild rules in terms of trailing whitespaces, lower/upper-case (unification).
* Handling of signed numerals (also ordinal ones) e.g `'minus zehn'`

# TODO / Known issues
- [x] ~~Make POC, functional for all common cases~~
- [x] ~~Ordinal number support~~
- [x] ~~Take care for exceptions / trailing whitespaces etc.~~
- [x] ~~Make structure + publish as PyPI package~~
- [x] Command line support :computer:
- [ ] More comprehensible tests
- [ ] Swiss variant
- [ ] More fault tolerant (ß -> ss) etc
- [ ] Larger scale than 10^60
- [ ] Ordinal with very large numbers (without addons) e.g `Millionste`
- [ ] Few benchmark improvements (e.g tail recursion etc)
- [ ] Better error handling + validation for idiotical cases (e.g `minus null Miliarde`)
- [ ] Simplify/refactor POC code, add better documentation
- [ ] Fractions?


