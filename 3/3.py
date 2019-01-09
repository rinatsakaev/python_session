import codecs
s = "\xFF"
s1 = r"C:\Users"

byte_str = b"abc"
print(byte_str[0]) #97 - код a
#byte_str[1] = "d" #throws 'bytes' object does not support item assignment
byte_arr = bytearray(byte_str)
byte_arr.insert(1, 5)
b_2 = byte_arr.replace(b'a', b'd')

str_unicode_char = "\u0394"
print(str_unicode_char)  # Δ
print('{:<30}'.format("blah"))
print('{:>30}'.format("blah"))
print('{:^30}'.format("blah"))
print('{:*^30}'.format("blah"))
str_to_decode = b'abcdef'
decoder = codecs.getdecoder('utf-8')
print(decoder(str_to_decode))
pass