'''
    A script to convert numbers to their actual names
'''
from time import sleep
mversion = '1.2.0'

#  list of numbers in string form to resolve number names less than 20
# first index is left blank so that doing num_array[0] gives ''
num_array = [
    '',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
    'ten',
    'eleven',
    'twelve',
    'thirteen',
    'fourteen',
    'fifteen',
    'sixteen',
    'seventeen',
    'eighteen',
    'nineteen'
]

#  list of numbers in string form to resolve number names less than 100 but higher than 20 
# first two indexes are left blank because we want tens[2] to be twenty
# to avoid unnecssary complexity
tens = [
    '', '', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'
]

#  tuple of numbers in string form to resolve higher order numbers
# first three indexes are left blank to avoid unnecssary complexity
num_tuple = ('', '', '',
             'thousand', 'million',
             'billion', 'trillion',
             'quadrillion',
             'quintillion')


# max allowable length of a number
MAX_LEN = len(num_tuple) - 1

# names a number from 0 to 100, we only need to name three digits at a time
# this is because all numbers are named in groups of maximum three
def name_number(num):
   
  
    # check for floating number  
    if num[0] == '.':
        print('%s is a floating number, this version %s does not support floating numbers' % (num, mversion))
        # need to learn how to throw errors in python
        exit(1)

    # check for 0 or something like `01` or `011` etc
    if num[0] == '0':
        if(len(num) > 1):
            return name_number(num[1:])
        return ''
    # checks if a number is less than three digits
    # then uses recursion to keep naming each digit first index first
    # till we get to the end of the number   
    if(len(num) < 3):
        
        if num[0] == '0' and num[1] == '0':
            return ''
        if(int(num) < 20):
            # not a tens number
            return num_array[int(num)]
        else:
            return tens[int(num[0])] + ' ' + name_number(num[1])
    else:
        # numbers with length greater than two need to be appended with `hundred`
        hold = name_number(num[0]) + ' hundred'
        # check if the following numbers after the first digit are all zeros
        # and act accordingly
        if num[1:] == '00':
            return hold
        return hold + ' and ' + name_number(num[1:])

# names a number that can be longer than three digits but less than 
def name_long_number(num):
    m_num = int(num)
    if m_num<1:
        return 'zero'
    # we need to start naming numbers from the back to avoid runnning
    # into trouble later on
    number = reversed(str(m_num))
    current_num = ''
   
    index = 0
    # holds the named number strings
    num_str_array = []

    for n in number:
        # check if we have exceded the maximum allowable length of numbers
        if index > MAX_LEN:
            print('%s is too long for this version %s, Max number is %s' %
                  (str(num), mversion, num_tuple[MAX_LEN]))
            return 0
        if (index % 3) < 1 and index > 0:
           # if we have gotten up to 3 numbers name the numbers 
            num_str_array.insert(0, name_number(current_num))
            current_num = ''

        current_num = n + current_num
        index += 1
    # check if we have missed one and add it if we have
    if len(current_num) > 0:
        num_str_array.insert(0, name_number(current_num))

    ans = ''
    num_length = len(num_str_array) - 1
    index = num_length
    # we need to reverse again to name number correctly
    for i in num_str_array:
        ans = ans + i.strip(' ') + ' ' + num_tuple[index + 2] + ', '
        index = index - 1
    # hopefully this is not too dirty but basically trying to remove `, ` from the 
    # end of the answer
    return ans[:(len(ans) - 2)].strip()


print(name_long_number('0110'))
