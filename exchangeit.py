"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and amount.
It prints out the result of converting the first currency to the second.

Author: Iddo Barnoon
Date:   03/16/2024
"""
import currency

src = input('3-letter code for original currency: ')
dst = input('3-letter code for the new currency: ')
amt = float(input('Amount of the original currency: '))
print('You can exchange ' + str(amt), src, 'for ' + str(round(currency.exchange(src,dst,amt), 3)), dst + '.')