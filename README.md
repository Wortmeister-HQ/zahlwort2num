# zahlwort2num

:de: :de: :de:
A small but useful (due shortage of/low quality support for lang_DE) package for handy convertion of german numerals (also ordinal) written as words to numbers. 

This might be a good complementary lib to https://github.com/savoirfairelinux/num2words

:crying_cat_face: _Currently is doesn't support swiss variant. TBD_ :switzerland:

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
 w2n.convert("minus siebenhundert millionen achtundsiebzig") # => -700000078
```
 _or even stuff like:_ <br />
 ```python
 w2n.convert("sechshundertdreiundfünfzigtausendfünfhunderteinundzwanzig") # => 653521
```
 :see_no_evil: 
 
#### Command line
* _(Obviously it is better to use parameter inside apostroph due possible spaces)_
```
bin/zahlwort2num-convert "ein million siebenhunderteinundzwanzig"
```
# WIKI
TBD

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
