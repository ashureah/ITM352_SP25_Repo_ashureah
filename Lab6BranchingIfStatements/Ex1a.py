# write Python code that initializes a tuple of strings representing different 
# emotions (i.e., happy, sad, fear, surprise). Write code that uses a 
# conditional expression (do not use an if-statement or ternary expression) to print
#  “true” if the last element is “happy” and there are more than 3 elements, or “false” 
# if it is not. (Hint: You can use the len function to determine how many elements are 
# in the tuple and then use that information in the expression). 

emotions = ('happy', 'sad', 'fear', 'surprise')

print((len(emotions)>3) and (emotions[-1] == 'happy'))
