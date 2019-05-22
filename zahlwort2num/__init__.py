from argparse import ArgumentError

name = 'zahlwort2num'

class ZahlConverter:

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

    ORD_SUFFICIES = ['te', 'ter', 'tes', 'tem', 'ten']

    # TODO: Larger...
    SCALES = ['million', 'milliarde', 'billion', 'billiarde', 'trillion', 'trilliarde', 'quadrillion', 'quadrilliarde']
    MAX_SC = len(SCALES)


    def mult(self, number, splitter, factor, fun):
        spliter = number.split(splitter)
        lenSplt = len(spliter)
        if lenSplt == 2:
            return fun(spliter[0]) * factor + fun(spliter[1])
        elif lenSplt == 1:
            return fun(spliter[0])
        else:
            raise ArgumentError('Given input cannot be properly parsed. Please double check if it has proper structure.')


    def convOrd(self, number):
        # dritte, vierte

        suffList = [True for suffix in self.ORD_SUFFICIES if number.endswith(suffix)]
        if len(suffList) > 0:
            if number[-2::] == 'te':  # Only possible 2 or 3 letter suffix
                if number[-3:-2] == 's':  # TODO: Special case erst
                    valid_nr = number[0:-3]
                else:
                    valid_nr = number[0:-2]
            elif number[-4:-3] != 's':  # Check if suffix is (te*)
                valid_nr = number[0:-3]
            else:
                valid_nr = number[0:-4]  # It has to be "ste*"
            return str(self.convt2(valid_nr)) + '.'
        else:
            return self.convt2(number)

    # ---- BIG NUMS
    def ordWithBN(self, number, idx):
        # TODO Mlionste etc

        if len(number.split(' ')) == 1 or (idx > self.MAX_SC - 1):
            return self.convOrd(number)

        split_ = number.split(self.SCALES[self.MAX_SC - idx - 1])

        if len(split_) > 1:
            sp0 = split_[0].strip()
            sp1 = split_[1].strip()

            if split_[1].startswith('en'):
                sp1 = split_[1][3::]
            elif split_[1].startswith('n'):
                sp1 = split_[1][2::]

            return self.convOrd(sp0) * 10 ** ((self.MAX_SC - idx + 1) * 3) + self.ordWithBN(sp1, idx + 1)
            # TODO: eine + trailing
        else:
            return self.ordWithBN(number, idx + 1)


    def ordBn(self, number):
        return self.ordWithBN(number, 0)


    def convert(self):
        number = self.trimmedText()
        if number.startswith('minus'):
            num_without_minus = number.replace('minus ', '')
            res = self.ordBn(num_without_minus)
            if isinstance(res, int):
                return (-1) * res  # No type coertion ;)
            elif isinstance(res, str):
                return '-%s' % res
            else:
                raise ValueError('Bad datatype returned. Possibly wrong string has been provided')
        else:
            return self.ordBn(number)

    def trimmedText(self):
        return self.number.lower().strip()

    def __init__(self, number):
        self.convt2 = lambda number: self.mult(number, 'tausend', 1000, self.convh2)
        self.convh2 = lambda number: self.mult(number, 'hundert', 100, self.convu2)
        self.convu2 = lambda number: self.mult(number, 'und', 1, lambda word: self.CONST_NUMS[word])

        self.number = number

def convert(number):
    c = ZahlConverter(number)
    return c.convert()