letters = 'acdegilmnoprstuw'
hash = 7


def reverseHash(n):
    ans = ''
    while n > 0:
        i = n % 37
        try:
            ans += letters[i]
        except Exception as e:
            print('invalid value')
        n = int((n - i) / 37)
        if n == hash:
            return ans[::-1]
        if n < hash:
            print('invalid value')


input_val = input("Enter hash")
input_val = int(input_val)
print(reverseHash(input_val))
