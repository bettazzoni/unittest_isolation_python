import unittest

from coverageutilities import called_modules_filenames, called_coverage_data

REPORT_ONE_FILE = '''\
Name                   Stmts   Miss  Cover   Missing
----------------------------------------------------
addsome\\test_satanic      34     32     6%   1-6, 11-54'''

REPORT_TWO_FILES = '''\
Name    Stmts   Exec  Cover  Missing
------------------------------------
foo        64     56    87%  23, 57, 85, 119, 125, 133, 137, 152
bar       105     90    86%  78-86, 237-246
------------------------------------
TOTAL     169    146    86% '''

ANALISYS_DATA = {"bar.py" : ("bar.py", [1]*105, None, [1]*15, ""), 
                 "foo.py" : ("foo.py",  [1]*64, None,  [1]*8, "")}

REPORT_MANY_FILES = '''\
Name       Stmts   Exec  Cover
------------------------------
types         47      0     0%
foo           64     56    87%
token        111      0     0%
whrandom      69     21    30%
bar          105     90    86%
coverage     141      2     1%
unittest     400     94    23%
string       121     15    12%
------------------------------
TOTAL        222    188    86% '''



class MockCoverage:
    def __init__(self, msg):
        self.msg=msg
    def report(self, file):
        file.write(self.msg)
    def analysis2(self, module):
        return ANALISYS_DATA[module]

class Test_coverageutilities(unittest.TestCase):

    def test_report_data_from_coverage_one_covered_file(self):
        mc = MockCoverage(REPORT_ONE_FILE)
        files = called_modules_filenames(mc)
        self.assertEqual(files, ["addsome\\test_satanic.py"])

    def test_report_data_from_coverage_2_covered_file(self):
        mc = MockCoverage(REPORT_TWO_FILES)
        files = called_modules_filenames(mc)
        self.assertEqual(files, ["foo.py", "bar.py"])

    def test_report_data_from_coverage_many_covered_files(self):
        files = called_modules_filenames(MockCoverage(REPORT_MANY_FILES))
        self.assertEqual(len(files), 8)

    def test_called_coverage_data_2_covered_file(self):
        mc = MockCoverage(REPORT_TWO_FILES)
        data = called_coverage_data(mc)
        self.assertEqual(data, { "foo.py": 56, "bar.py":90 })
