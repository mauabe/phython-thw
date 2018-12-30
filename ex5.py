my_name = 'Mauricio Feldman-Abe'
my_age = 35 #it is a lie
my_height = 75 # inches
my_weight = 212 # lbs
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Black'
my_pi = 3.1415

print ("Let's talk about %s." % my_name)
print ("He's %d inches tall." % my_height)
print ("He's %d pounds heavy." % my_weight)
print ("Actualy that's not too heavy.")
print ("He's got %s eyes and %s hair. " % (my_eyes, my_hair))
print ("his teeth are usually %s depending on the coffee." % my_teeth)

# this line is tricky, try to get it exactly right
print ("If I add %d, %d, and %d I get  %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight))

print ("Let's talk about variable 'r': %r." % my_age)
print ("Let's round numbers %d." % round(3.1415))
