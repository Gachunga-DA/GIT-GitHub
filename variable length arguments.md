The variable length argument is used when there is more than one argument to be passed through a function that has been defined. 
It is majorly used when we do not know the number of arguments neeed for a function. 
* is placed before a parameter and holds non-keyworded variable lengths
** is placed before a parameter for keyworded variable length arguments
*var is for all positional argumensts from that point to the end that are collected as a tuple i.e 'var'
**var is for all positional arguments from that point to the end that are collected as a dictionary called 'var'

Tuple-These are inchangeable or immutable values. Its elements cannot be modified neither can the values. It is similar to a list. However, it does not use square brackets[] but uses parethesis(). It therefore helps in storing fixed data. 
example:
#create a tuple
my_tuple=(1,2,3, "hello", True)
print(my tuple)
output 
(1,2,3, "Hello", True)
NB:Tuples do not allow for adding or removing values given. 
