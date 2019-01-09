import re
str_to_match = "<a> b <c>"
res1 = re.match("(<.*>)", str_to_match)
print(res1.groups())  # ('<a> b <c>',)

res2 = re.match("(<.*?>)", str_to_match)
print(res2.groups())  # ('<a>',)

str_to_match2 = "aaaaa bbbb ccc cd b"
res3 = re.match("(a{3})", str_to_match2)
print(res3.groups()) #('aaa',)
res3 = re.match("(a{6})", str_to_match2)
print(res3) #None

#match ищет в начале строки. Если начало не совпадает, то none
res3 = re.match("(a+\sb+)", str_to_match2)
print(res3.groups()) #('aaaaa bbbb',)

res3 = re.fullmatch("(a+\sb+)", str_to_match2)
print(res3) #None

res3 = re.fullmatch("(a+\sb+).*", str_to_match2)
print(res3.groups()) #('aaaaa ',)bbbb