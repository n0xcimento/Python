
'''
    A script que input a numeric check amount that is less than 1000 and uses the dictionary to write
    the word equivalent of the amount..
'''

UN = {0:'', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
M10 = {0:'', 1: 'ten', 2: 'twety', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}

num10_19 = {0:'', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}


def flout_part(num):

    dec = num.split('.')[1]
    dec += ''.join(['/', str(10 ** len(dec))])
    return dec


def unit(num):
    return UN[int(num)]


def dezena(num):
    num_int = int(num)

    if (num_int == 10) or (num_int >= 20):
        return M10[num_int//10] + ' ' + unit(num[1:])
    else:
        return num10_19[num_int]


def centena(num):
    num_int = int(num)
    return unit(num[0]) + ' hundred ' + dezena(num[1:])


def umilhar(num):
    return unit(num[0]) + ' thousand ' + centena(num[1:])


def int_part(num):
    ans = ''
    if len(num) == 1:
        ans += unit(num)
    elif len(num) == 2:
        ans += dezena(num)
    elif len(num) == 3:
        ans += centena(num)
    elif len(num) == 4:
        ans += umilhar(num)
    return ans


def num2alpha(num):
    ans = int_part(num.split('.')[0])

    if num.find('.') != -1:
        ans += ' and ' + flout_part(num)
    return ans


print(num2alpha('112.43'))