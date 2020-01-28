year_input = int(input())

def is_leap_year(year):
    if year % 4 == 0:
        return True
    else:
        return False

if is_leap_year(year_input):
    print('%.f is a leap year' % year_input)
else:
    print('%.f is not a leap year' % year_input)



