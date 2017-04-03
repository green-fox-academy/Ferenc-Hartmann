#Create Counter class
#which has an integer field value
#when creating it should have a default value 0 or we can specify it when creating
#we can add(number) to this counter another whole number
#or we can add() without parameters just increasing the counter's value by one
#and we can get() the current value
#also we can reset() the value to the initial value
#Check if everything is working fine with the proper test
#Download test_counter.py and place it next to your solution
#Run the test file as a usual python program

class Counter():
    def __init__(self, integer_field_value=0):
        self.integer_field_value = integer_field_value
        self.default = integer_field_value
    def add(self, number=1):
        self.integer_field_value += number
        return self.integer_field_value
    def get(self):
        return self.integer_field_value
    def reset(self):
        self.integer_field_value = self.default
        return self.integer_field_value
