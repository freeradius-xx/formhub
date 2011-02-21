# http://stackoverflow.com/questions/4126165/problem-downloading-google-spreadsheet-using-curl
import os, sys
from xls2json import ExcelReader
from survey import Survey

# in google docs, these spreadsheets have been published as web pages,
# this way we can download the corresponding xls without sending a
# password, these also provide great examples of how to use xls2xform.
spreadsheets = {
    "Water" : "0Av9fIlfpFAtddC1XYmxnWVpEdkFZUkg3aUFKcGxHVHc",
    "LGA" : "0Av9fIlfpFAtddG5COTdMck1sLVBja2pxcmJRamM1U3c",
    "Agriculture" : "0Av9fIlfpFAtddE1GYVpqWEdEMnU5RVk1dFgtdDJYVHc",
    "Education" : "0Av9fIlfpFAtddFluNk4xNkJvSkhYejkwekhIQWVPZWc",
    "Health" : "0Av9fIlfpFAtddGlPdzE1djBqeUR5Q0tZZ21aZk5vWFE",
    }

def download(name):
    cmd = 'curl "https://spreadsheets1.google.com/pub?key=%(key)s&output=xls" -o %(name)s.xls' % {
        "key" : spreadsheets[name],
        "name" : name,
        }
    os.system(cmd)

if __name__=="__main__":
    name = sys.argv[1]
    download(name)
    converter = ExcelReader("%s.xls" % name)
    converter.print_json_to_file()
    s = Survey(name=name)
    s.load_elements_from_json("%s.json" % name)
    print s.to_xml()