# Exercises for chapter 3:

# Name: Kimberly Milberg

# 3.1
# moving the last line to the top produces the following error:
# NameError: name 'repeat_lyrics' is not defined

# 3.2
# the program runs properly in this instancee.
# it seems that this is because the functions is defined before it is printed.

#3.3
def right_justify(text):
	# print '%70s' % text -- this is one way, but doesn't use len()
    # here is another way using a for loop
    # text_length = len(text)
    # for x in range (0, (70-text_length)):
        # print " ",
    # print text
    
    # below is the solution that uses the skills learned so far
    text_length = len(text)
    print (" " * (70 - text_length)) + text

right_justify('kimberly')

# 3.4
#     1.  spam is printed twice, each on a separate line
#     2.
def do_twice(f, value):
    f(value)
    f(value)

# def print_spam(repeat):
	# print 'spam' * repeat

# do_twice(print_spam, 2)
# print " "
#     3. 
def print_twice(my_string):
	print my_string
	print my_string
#    4.
do_twice(print_twice, 'text')
print " "
#    5.
def do_four(f, my_string):
	do_twice(f, my_string)
	do_twice(f, my_string)

do_four(print_twice, 'kimberly')

