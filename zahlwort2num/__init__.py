name = "zahlwort2num"

CONST_NUMS = {
    '': 0,
    'null': 0,
    'ein': 1,
    'eins': 1,
    'eine': 1,
    'er': 1,
    'zwei': 2,
    'drei': 3,
    'drit': 3,
    'vier': 4,
    u'fünf': 5,
    'sechs': 6,
    'sieben': 7,
    'sieb': 7,
    'acht': 8,
    'neun': 9,
    'zehn': 10,
    'elf': 11,
    u'zwölf': 12,
    'dreizehn': 13,
    'vierzehn': 14,
    'fünfzehn': 15,
    'sechzehn': 16,
    'siebzehn': 17,
    'achtzehn': 18,
    'neunzehn': 19,
    'zwanzig': 20,
    u'dreißig': 30,
    'dreissig': 30,
    'vierzig': 40,
    u'fünfzig': 50,
    'sechzig': 60,
    'siebzig': 70,
    'achtzig': 80,
    'neunzig': 90
}


def mult(number, splitter, factor, fun):
    spliter = number.split(splitter)
    lenSplt = len(spliter)
    if (lenSplt == 2):
        return fun(spliter[0]) * factor + fun(spliter[1])
    elif (lenSplt == 1):
        return fun(spliter[0])
    else:
        raise ArgumentError('Given input cannot be properly parsed. Please double check if it has proper structure.')


convt2 = lambda number: mult(number, 'tausend', 1000, convh2)
convh2 = lambda number: mult(number, 'hundert', 100, convu2)
convu2 = lambda number: mult(number, 'und', 1, lambda word: CONST_NUMS[word])

def convOrd(number):
    # dritte, vierte
    sufficies = ['te', 'ter', 'tes', 'tem', 'ten']
    suffList = [True for suffix in sufficies if number.endswith(suffix)]
    if (len(suffList) > 0):
        if number[-2::] == 'te':  # Only possible 2 or 3 letter suffix
            if (number[-3:-2] == 's'): #TODO: Special case erst
                valid_nr = number[0:-3]
            else:
                valid_nr = number[0:-2]
        elif (number[-4:-3] != 's'):  # Check if suffix is (te*)
            valid_nr = number[0:-3]
        else:
            valid_nr = number[0:-4]  # It has to be "ste*"
        return str(convt2(valid_nr)) + "."
    else:
        return convt2(number)


# ----

# TODO: Larger...
SCALES = ['million', 'milliarde', 'billion', 'billiarde', 'trillion', 'trilliarde', 'quadrillion', 'quadrilliarde']
MAX_SC = len(SCALES)

# ---- BIG NUMS
def ordWithBN(number, idx):
    # TODO Mlionste etc

    if (len(number.split(' ')) == 1 or (idx > MAX_SC - 1)):
        return convOrd(number)

    split_ = number.split(SCALES[MAX_SC - idx - 1])

    if (len(split_) > 1):
        sp0 = split_[0].strip()
        sp1 = split_[1].strip()

        if (split_[1].startswith('en')):
            sp1 = split_[1][3::]
        elif (split_[1].startswith('n')):
            sp1 = split_[1][2::]

        return convOrd(sp0) * 10 ** ((MAX_SC - idx + 1) * 3) + ordWithBN(sp1, idx + 1)
        #TODO: eine + trailing
    else:
        return ordWithBN(number, idx + 1)


def ordBn(number):
    return ordWithBN(number, 0)


def convert(number):
    number = number.lower().strip()
    if number.startswith('minus'):
        num_without_minus = number.replace('minus ', '')
        res = ordBn(num_without_minus)
        if isinstance(res, int):
            return (-1) * res  # No type coertion ;)
        elif isinstance(res, str):
            return "-%s" % res
        else:
            raise ValueError('Bad datatype returned. Possibly wrong string has been provided')
    else:
        return ordBn(number)