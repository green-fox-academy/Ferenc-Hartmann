
example = "In a dishwasher far far away";

# I would like to replace "dishwasher" with "galaxy" in this example
# Please fix it for me!
# Expected ouput: In a galaxy far far away

a= "galaxy"

example = (example[0:5] + str(a) + example[15:])

print(example)
