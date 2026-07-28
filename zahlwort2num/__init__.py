from argparse import ArgumentError

from .__version__ import __version__

name = 'zahlwort2num'

class ZahlConverter:
    CONST_NUMS = {
        '': 0,
        'null': 0,
        'ein': 1,
        'eins': 1,
        'eine': 1,
        'er': 1,
        'ers': 1,
        'zwei': 2,
        'zwo': 2,
        'drei': 3,
        'drit': 3,
        'dritt': 3,  # for ordinals like "dritte"
        'vier': 4,
        'fünf': 5,
        'sechs': 6,
        'sieben': 7,
        'sieb': 7,
        'siebt': 7,  # for ordinals like "siebte"
        'acht': 8,
        'achte': '8.',  # ordinal
        'neun': 9,
        'zehn': 10,
        'elf': 11,
        'zwölf': 12,
        'dreizehn': 13,
        'vierzehn': 14,
        'fünfzehn': 15,
        'sechzehn': 16,
        'siebzehn': 17,
        'achtzehn': 18,
        'neunzehn': 19,
        'zwanzig': 20,
        'dreißig': 30,
        'dreissig': 30,  # Swiss variant
        'vierzig': 40,
        'fünfzig': 50,
        'sechzig': 60,
        'siebzig': 70,
        'achtzig': 80,
        'neunzig': 90,
        # Austrian German variants
        'zwoa': 2,  # Austrian/Bavarian variant for "zwei"
        # Fractions
        'halb': 2,  # for "ein halb" = 1/2
        'halbe': 2,  # for "eine halbe" = 1/2
        'viertel': 4,  # for "ein viertel" = 1/4
        'drittel': 3,  # for "ein drittel" = 1/3
        'fünftel': 5,  # for "ein fünftel" = 1/5
        'sechstel': 6,  # for "ein sechstel" = 1/6
        'siebtel': 7,  # for "ein siebtel" = 1/7
        'achtel': 8,  # for "ein achtel" = 1/8
        'neuntel': 9,  # for "ein neuntel" = 1/9
        'zehntel': 10,  # for "ein zehntel" = 1/10
    }

    ORD_SUFFIXES = ['stem', 'ste', 'ter', 'tes', 'tem', 'ten', 'e', 'te']
    SCALES = ['million', 'milliarde', 'billion', 'billiarde', 'trillion', 'trilliarde', 'quadrillion', 'quadrilliarde', 'quintillion', 'sextillion', 'septillion', 'oktillion', 'nonillion', 'dezillion']
    MAX_SCALE_IDX = len(SCALES) - 1

    def __init__(self, number: str):
        self.number = number.lower().strip()
        self.convt2 = lambda num: self._apply_multiplier(num, 'tausend', 1000, self._convert_hundreds)
        self._convert_hundreds = lambda num: self._apply_multiplier(num, 'hundert', 100, self._convert_units)
        self._convert_units = lambda num: self._apply_multiplier(num, 'und', 1, self._convert_single_unit)

    def _apply_multiplier(self, number: str, splitter: str, factor: int, func):
        parts = number.split(splitter)
        if len(parts) == 2:
            if splitter != 'und' and not parts[0]:
                return factor + func(parts[1])
            return func(parts[0]) * factor + func(parts[1])
        elif len(parts) == 1:
            return func(parts[0])
        else:
            raise ArgumentError(None, 'Invalid input structure.')

    def _convert_single_unit(self, word: str) -> int:
        word = word.replace('ß', 'ss')  # Handle Swiss variant
        result = self.CONST_NUMS.get(word, None)
        if result is None:
            raise ValueError(f"Unknown number word: {word}")
        return result

    def _convert_ordinal(self, number: str) -> str:
        # First try to convert as a regular number
        try:
            regular_result = self.convt2(number)
            return str(regular_result)
        except ValueError:
            # If regular conversion fails, check if it's an ordinal
            for suffix in self.ORD_SUFFIXES:
                if number.endswith(suffix):
                    if suffix == 'e':
                        # Special case for ordinals ending with 'e' (like 'achte')
                        base_number = number[:-1]
                    elif suffix == 'te':
                        # For 'te' suffix, remove 'te' and check if we need to remove more
                        base_number = number[:-2]
                        # If the remaining ends with 't', remove it too (for cases like 'zwanzigste' -> 'zwanzig')
                        if base_number.endswith('t'):
                            base_number = base_number[:-1]
                    elif suffix == 'ste':
                        # For 'ste' suffix, remove 'ste' and check if we need to remove more
                        base_number = number[:-3]
                        # If the remaining ends with 't', remove it too (for cases like 'zwanzigste' -> 'zwanzig')
                        if base_number.endswith('t'):
                            base_number = base_number[:-1]
                    elif suffix == 'stem':
                        # For 'stem' suffix, remove 'stem' entirely
                        base_number = number[:-4]
                    else:
                        # For other suffixes, just remove the suffix
                        base_number = number[:-len(suffix)]
                    try:
                        base_number_value = self.convt2(base_number)
                        return f"{base_number_value}."
                    except ValueError:
                        # If base_number contains invalid words, continue checking other suffixes
                        continue
            
            # If no ordinal suffix works either, this is an error
            raise ValueError(f"Cannot convert '{number}' to a number")

    def _convert_big_numbers(self, number: str, idx: int):
        if idx > self.MAX_SCALE_IDX or ' ' not in number:
            ordinal_result = self._convert_ordinal(number)
            # If it's an ordinal (ends with '.'), return as string, otherwise convert to int
            if isinstance(ordinal_result, str) and ordinal_result.endswith('.'):
                return ordinal_result
            try:
                return int(ordinal_result)
            except ValueError:
                return ordinal_result
        split_ = number.split(self.SCALES[self.MAX_SCALE_IDX - idx])
        if len(split_) > 1:
            base, rest = split_[0].strip(), split_[1].strip()
            if rest == 'en' or rest.startswith('en '):
                rest = rest[3:] if rest.startswith('en ') else ''
            elif rest == 'n' or rest.startswith('n '):
                rest = rest[2:] if rest.startswith('n ') else ''
            base_result = self._convert_ordinal(base)
            # If base is ordinal, return as string
            if isinstance(base_result, str) and base_result.endswith('.'):
                return base_result
            base_value = int(base_result) if isinstance(base_result, str) and not base_result.endswith('.') else base_result
            multiplier = (self.MAX_SCALE_IDX - idx + 2) * 3
            return base_value * 10 ** multiplier + self._convert_big_numbers(rest, idx + 1)
        return self._convert_big_numbers(number, idx + 1)

    def _is_fraction(self, number: str) -> bool:
        """Check if the number string represents a fraction like 'ein und zwei' or 'drei viertel'"""
        parts = number.split(' ')
        if len(parts) == 3 and parts[1] == 'und' and parts[0] in self.CONST_NUMS and parts[2] in self.CONST_NUMS:
            return True  # "ein und zwei" style
        elif len(parts) == 2 and parts[0] in self.CONST_NUMS and parts[1] in ['halb', 'halbe', 'viertel', 'drittel', 'fünftel', 'sechstel', 'siebtel', 'achtel', 'neuntel', 'zehntel']:
            return True  # "drei viertel" style
        elif len(parts) == 2 and parts[0] == 'ein' and parts[1] in ['halb', 'halbe', 'viertel', 'drittel', 'fünftel', 'sechstel', 'siebtel', 'achtel', 'neuntel', 'zehntel']:
            return True  # "ein viertel" style
        elif len(parts) == 2 and parts[0] == 'eine' and parts[1] in ['halbe', 'viertel', 'drittel', 'fünftel', 'sechstel', 'siebtel', 'achtel', 'neuntel', 'zehntel']:
            return True  # "eine halbe" style
        return False

    def _convert_fraction(self, number: str) -> float:
        parts = number.split(' ')
        if len(parts) == 3 and parts[1] == 'und':
            # "ein und zwei" style
            numerator = self._convert_single_unit(parts[0])
            denominator = self._convert_single_unit(parts[2])
            return numerator / denominator
        elif len(parts) == 2:
            # "drei viertel" or "ein viertel" style
            numerator = self._convert_single_unit(parts[0])
            denominator = self.CONST_NUMS.get(parts[1], None)
            if denominator is None:
                raise ValueError(f"Unknown fraction denominator: {parts[1]}")
            return numerator / denominator
        raise ArgumentError(None, 'Invalid fraction structure.')

    def _is_decimal(self, number: str) -> bool:
        """Check if the number string represents a decimal number like 'zwei komma fünf'"""
        parts = number.split(' komma ')
        if len(parts) == 2:
            try:
                # Try to convert both parts
                self.convt2(parts[0])
                self.convt2(parts[1])
                return True
            except ValueError:
                pass
        return False

    def _convert_decimal(self, number: str) -> float:
        """Convert decimal number like 'zwei komma fünf' to float"""
        parts = number.split(' komma ')
        if len(parts) == 2:
            integer_part = self.convt2(parts[0])
            decimal_part = self.convt2(parts[1])

            # Convert decimal part to proper decimal places
            decimal_str = str(decimal_part)
            decimal_value = decimal_part / (10 ** len(decimal_str))

            return float(f"{integer_part}.{decimal_part}")
        raise ArgumentError(None, 'Invalid decimal structure.')

    def convert(self):
        if self.number.startswith('minus'):
            num_without_minus = self.number.replace('minus ', '')
            res = self._convert_big_numbers(num_without_minus, 0)
            if isinstance(res, str) and res.endswith('.'):
                return f"-{res}"
            return -res
        elif self._is_fraction(self.number):
            return self._convert_fraction(self.number)
        elif self._is_decimal(self.number):
            return self._convert_decimal(self.number)
        return self._convert_big_numbers(self.number, 0)

def convert(number: str):
    converter = ZahlConverter(number)
    return converter.convert()
