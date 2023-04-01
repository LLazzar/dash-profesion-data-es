#Functions to trasnform scraped salary strings into the right number format

import re

#trasnform scraped median salary string into the right form
#string="€38,100" --> 38100
def convertM(string):
    return int(re.sub(r'[^\d]+', '', string))

#trasform scraped q1 and q2 salaries string in the right form
#string="€32K" --> 32000
def convertQ(string):
    return str(int(''.join(filter(str.isdigit, string)))*1000)

