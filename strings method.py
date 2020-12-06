name = " shazia afroze   "
print (name.upper())
print (name.lower())
print (name.title())
print (name.strip()) # Removes spaces
print (name.lstrip())#removes from lefft
print (name.rstrip())#removes from right
print (name.find("afr"))# 012345678 - space(0),s(1) h(2) a(3) z(4) i(5) a(6) space(7) a(8)  (its index)
print (name.find('Afr')) # if character not found 'A' it gives -1
print (name.replace('a', 'u'))# it replaces a with 'u'
print ('afr' in name)# boolean
print ('swift' not in name)# boolean