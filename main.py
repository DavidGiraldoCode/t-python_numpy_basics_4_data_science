import numpy as np
import array

x = 1000 #This is a pointer, in a C strucutre, with a lot of values.

#Standard mutable multi-element container --> LIST
my_lits_A = list(range(10))
print(my_lits_A)
print(type(my_lits_A[0])) #<class 'int'>

my_list_B = [str(c) for c in my_lits_A]
print(my_list_B)
print(type(my_list_B[0])) #<class 'str'>

my_list_C = [True, "2", 3.0, 4]
print([type(item) for item in my_list_C])

#Each of the element is a complete Pyhton Object.
#Fixed-type arrays are more efficient.

normal_list = list(range(10))
array_list = array.array('i', normal_list)
# 'i' indicates it is an array of integers
print(array_list)

#========================================== using NumPy

print(np.array([1,4,2,5,6,10,3,7]))

# Here NumPy upcast from int to float
print(np.array([1,4,2,5,6.2,10,3,7])) 

# To prevent upcasting
print(np.array([1.2,4,2,5,6.2,10,3,7], dtype='float32'))

#Create multidimension array
print(np.array([range(i, i + 5) for i in [1, 4, -4]]))

#------------- creating from scratch 
zeros_only_array = np.zeros(10, dtype=int)
ones_only_array = np.ones((3,5), dtype=float)
full_of_array = np.full((3,5), 3.1416)
sequenced_array = np.arange(0, 100, 1.7)
evenly_spaced_array = np.linspace(0,1,20)
random_array = np.random.random((5,5))
normal_dist_array = np.random.normal(0,1,(3,3))
random_range_array = np.random.randint(0, 20, (4,4))
identity_matrix = np.eye(3)
uninitialized_array = np.empty(5)

print(zeros_only_array)
print(ones_only_array)
print(full_of_array)
print(sequenced_array)
print(evenly_spaced_array)
print(random_array)
print(normal_dist_array)
print(random_range_array)
print(identity_matrix)
print(uninitialized_array)

