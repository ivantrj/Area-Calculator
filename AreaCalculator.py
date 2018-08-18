# Calculating the area of a tringle and a circle

print 'Calculator is up and running'

option = raw_input('Enter C for Circle or T for Triangle: ')

if option == 'c':
  radius = float(raw_input('Enter the radius: '))
  area = 3.14159 * radius ** 2
  print 'The area of a circle with radius %s is %s' %(radius, area)
elif option == 't':
  base = float(raw_input('Enter the base: '))
  height = float(raw_input('Enter the height: '))
  area = base / 2 * height
  print 'The area of a triangle with base %s and height %s is %s' % (base, height, area)
else:
  print '%s is an invalid option' % (option)

  
print 'Area Calculator is exiting now'