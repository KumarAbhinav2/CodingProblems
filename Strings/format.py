def timeConversion(s):
    #
    # Write your code here.
    #
    post = s[len(s)-2:]
    hr = int(s[:2])
    res = ''
    if post == 'PM':
       if hr != 12:
            res = str(hr+12)+s[2:len(s)-2]
       else:
            res = s[:len(s)-2]
    if post == 'AM':
        if hr == 12:
            res = '00:00:00'
        else:
            res = s[:len(s)-2]
    return res

print(timeConversion('07:05:35PM'))
print(timeConversion('12:05:35PM'))
print(timeConversion('12:00:00AM'))
print(timeConversion('07:05:35AM'))