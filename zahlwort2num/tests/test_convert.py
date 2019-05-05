from unittest import TestCase

import zahlwort2num as w2n


class Testconvertert(TestCase):
    def test_hardcoded_upto_100(self):
        assert w2n.convert('eins') == 1
        assert w2n.convert('zwei') == 2
        assert w2n.convert('drei') == 3
        assert w2n.convert('vier') == 4
        assert w2n.convert('fünf') == 5
        assert w2n.convert('sechs') == 6
        assert w2n.convert('sieben') == 7
        assert w2n.convert('acht') == 8
        assert w2n.convert('neun') == 9
        assert w2n.convert('zehn') == 10
        assert w2n.convert('elf') == 11
        assert w2n.convert('zwölf') == 12
        assert w2n.convert('dreizehn') == 13
        assert w2n.convert('vierzehn') == 14
        assert w2n.convert('fünfzehn') == 15
        assert w2n.convert('sechzehn') == 16
        assert w2n.convert('siebzehn') == 17
        assert w2n.convert('achtzehn') == 18
        assert w2n.convert('neunzehn') == 19
        assert w2n.convert('zwanzig') == 20
        assert w2n.convert('einundzwanzig') == 21
        assert w2n.convert('zweiundzwanzig') == 22
        assert w2n.convert('dreiundzwanzig') == 23
        assert w2n.convert('vierundzwanzig') == 24
        assert w2n.convert('fünfundzwanzig') == 25
        assert w2n.convert('sechsundzwanzig') == 26
        assert w2n.convert('siebenundzwanzig') == 27
        assert w2n.convert('achtundzwanzig') == 28
        assert w2n.convert('neunundzwanzig') == 29
        assert w2n.convert('dreißig') == 30
        assert w2n.convert('einunddreißig') == 31
        assert w2n.convert('zweiunddreißig') == 32
        assert w2n.convert('dreiunddreißig') == 33
        assert w2n.convert('vierunddreißig') == 34
        assert w2n.convert('fünfunddreißig') == 35
        assert w2n.convert('sechsunddreißig') == 36
        assert w2n.convert('siebenunddreißig') == 37
        assert w2n.convert('achtunddreißig') == 38
        assert w2n.convert('neununddreißig') == 39
        assert w2n.convert('vierzig') == 40
        assert w2n.convert('einundvierzig') == 41
        assert w2n.convert('zweiundvierzig') == 42
        assert w2n.convert('dreiundvierzig') == 43
        assert w2n.convert('vierundvierzig') == 44
        assert w2n.convert('fünfundvierzig') == 45
        assert w2n.convert('sechsundvierzig') == 46
        assert w2n.convert('siebenundvierzig') == 47
        assert w2n.convert('achtundvierzig') == 48
        assert w2n.convert('neunundvierzig') == 49
        assert w2n.convert('fünfzig') == 50
        assert w2n.convert('einundfünfzig') == 51
        assert w2n.convert('zweiundfünfzig') == 52
        assert w2n.convert('dreiundfünfzig') == 53
        assert w2n.convert('vierundfünfzig') == 54
        assert w2n.convert('fünfundfünfzig') == 55
        assert w2n.convert('sechsundfünfzig') == 56
        assert w2n.convert('siebenundfünfzig') == 57
        assert w2n.convert('achtundfünfzig') == 58
        assert w2n.convert('neunundfünfzig') == 59
        assert w2n.convert('sechzig') == 60
        assert w2n.convert('einundsechzig') == 61
        assert w2n.convert('zweiundsechzig') == 62
        assert w2n.convert('dreiundsechzig') == 63
        assert w2n.convert('vierundsechzig') == 64
        assert w2n.convert('fünfundsechzig') == 65
        assert w2n.convert('sechsundsechzig') == 66
        assert w2n.convert('siebenundsechzig') == 67
        assert w2n.convert('achtundsechzig') == 68
        assert w2n.convert('neunundsechzig') == 69
        assert w2n.convert('siebzig') == 70
        assert w2n.convert('einundsiebzig') == 71
        assert w2n.convert('zweiundsiebzig') == 72
        assert w2n.convert('dreiundsiebzig') == 73
        assert w2n.convert('vierundsiebzig') == 74
        assert w2n.convert('fünfundsiebzig') == 75
        assert w2n.convert('sechsundsiebzig') == 76
        assert w2n.convert('siebenundsiebzig') == 77
        assert w2n.convert('achtundsiebzig') == 78
        assert w2n.convert('neunundsiebzig') == 79
        assert w2n.convert('achtzig') == 80
        assert w2n.convert('einundachtzig') == 81
        assert w2n.convert('zweiundachtzig') == 82
        assert w2n.convert('dreiundachtzig') == 83
        assert w2n.convert('vierundachtzig') == 84
        assert w2n.convert('fünfundachtzig') == 85
        assert w2n.convert('sechsundachtzig') == 86
        assert w2n.convert('siebenundachtzig') == 87
        assert w2n.convert('achtundachtzig') == 88
        assert w2n.convert('neunundachtzig') == 89
        assert w2n.convert('neunzig') == 90
        assert w2n.convert('einundneunzig') == 91
        assert w2n.convert('zweiundneunzig') == 92
        assert w2n.convert('dreiundneunzig') == 93
        assert w2n.convert('vierundneunzig') == 94
        assert w2n.convert('fünfundneunzig') == 95
        assert w2n.convert('sechsundneunzig') == 96
        assert w2n.convert('siebenundneunzig') == 97
        assert w2n.convert('achtundneunzig') == 98

    def test_more_specific(self):
        words = ["sieben",
                 "neunundneunzig",
                 "eintausend",
                 "zweihunderttausend",
                 "fünfundvierzighundertvier",
                 "fünfundvierzighundertelf",
                 "zweihundertfünfundzwanzig",  # 225
                 "dreitausendsechshundertfünfundzwanzig",  # 3625
                 "zwölftausendachthundertvierundfünfzig",  # 12854
                 "sechshundertdreiundfünfzigtausendfünfhunderteinundzwanzig",  # 653521
                 "vierundzwanzigstem",
                 "siebzigste",
                 "neunundneunzig",
                 "fünfhunderttausendzwei",
                 "eine million viertausend",
                 "siebenhundert trillion neun milliarde eine million neuntausendeins",
                 "neun quadrilliarde elf",
                 "zwei milliarden",
                 "eintausend",
                 "minus eine million",
                 "minus dreizehn",
                 "minus siebenhundert millionen achtundsiebzig",
                 "minus elf",
                 "null",
                 "siebte",
                 "neunte",
                 "erste",
                 "zwanzigste",
                 "neunundvierzig"
                 ]

        numbers = [7, 99, 1000, 200000, 4504, 4511, 225, 3625, 12854, 653521, '24.', '70.',
                   99, 500002, 1004000, 700000000009001009001, 9000000000000000000000000011,
                   2000000000, 1000, -1000000, -13, -700000078, -11, 0, '7.', '9.', '1.', '20.', 49]

        for (idx, word) in enumerate(words):
            assert (w2n.convert(word) == numbers[idx])
