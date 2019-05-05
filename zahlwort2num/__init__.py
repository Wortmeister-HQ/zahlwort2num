name = "zahlwort2num"

def atoml(number):
    if (number == 'null' or number == ''):
        return 0
    if (number == 'eins' or number == 'ein' or number == 'eine' or number == 'er'):
        return 1
    if (number == 'zwei'):
        return 2
    if (number == 'drei' or number == 'drit'):
        return 3
    if (number == 'vier'):
        return 4
    if (number == 'fünf'):
        return 5
    if (number == 'sechs'):
        return 6
    if (number == 'sieben' or number == 'sieb'):
        return 7
    if (number == 'acht'):
        return 8
    if (number == 'neun'):
        return 9
    if (number == 'zehn'):
        return 10
    if (number == 'elf'):
        return 11
    if (number == 'zwölf'):
        return 12
    if (number == 'dreizehn'):
        return 13
    if (number == 'vierzehn'):
        return 14
    if (number == 'fünfzehn'):
        return 15
    if (number == 'sechzehn'):
        return 16
    if (number == 'siebzehn'):
        return 17
    if (number == 'achtzehn'):
        return 18
    if (number == 'neunzehn'):
        return 19
    if (number == 'zwanzig'):
        return 20
    if (number == 'dreißig'):
        return 30
    if (number == 'vierzig'):
        return 40
    if (number == 'fünfzig'):
        return 50
    if (number == 'sechzig'):
        return 60
    if (number == 'siebzig'):
        return 70
    if (number == 'achtzig'):
        return 80
    if (number == 'neunzig'):
        return 90

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
convu2 = lambda number: mult(number, 'und', 1, atoml)

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