#http://cwa.govmu.org/Documents/Publications/Customer%20Charter.pdf
MINIMUM_CHARGE = 45
FIRST10 = 6
NEXT10 = 8
NEXT30 = 17
ADDITIONAL = 32

#user input
unit = int(input('CWA m3 used: '))

UNIT = unit
rate = 'MINIMUM_CHARGE'
charge = MINIMUM_CHARGE

#FIRST10
gamut = 10
if unit > gamut:
    charge += gamut * FIRST10
    unit -= gamut
else:
    rate = 'FIRST10'
    charge += unit * FIRST10
    
#NEXT10 
gamut = 10
if unit > gamut:
    charge += gamut * NEXT10
    unit -= gamut
elif rate == 'MINIMUM_CHARGE':
    rate = 'NEXT10'
    charge += unit * NEXT10

#NEXT30  
gamut = 30
if unit > gamut:
    charge += gamut * NEXT30
    unit -= gamut
elif rate == 'MINIMUM_CHARGE':
    rate = 'NEXT30'
    charge += unit * NEXT30
    
#ADDITIONAL  
if rate == 'MINIMUM_CHARGE':
    rate = 'ADDITIONAL'
    charge += unit * ADDITIONAL
    
print("Charge is Rs {} under the {} rate for {} units.".format(charge, rate, UNIT))
