"""

Data type object 'dtype' is an instance of numpy.dtype class. It can be created with numpy.dtype.

"""

import numpy as np


# sample example with int16 data type
i16 = np.dtype(np.int16)
print(i16)
lst = [[3.4, 8.7, 9.9],
       [1.1, -7.8, -0.7],
       [4.1, 12.3, 4.8]]
A = np.array(lst, dtype=i16)
print(A)


"""
We create a structured array with the 'density' column. The data type is defined as np.dtype([('density', np.int)]).
We assign this data type to the variable 'dt' for the sake of convenience.
We use this data type in the darray definition, in which we use the first three densities
Output:
[(393,) (337,) (256,)]
The internal representation:
array([(393,), (337,), (256,)],
      dtype=[('density', '<i4')])

"""

# defining the dataType for density
dt = np.dtype([('density', np.int32)])

# also we can write above code like this
dt = np.dtype([('density', 'i4')])

# creating an array
x = np.array([(393,), (337,), (256,)],
             dtype=dt)
print(x)
print("\nThe internal representation:")
print(repr(x))


"""
Defining a data type for each fields:
S20 - String can contains length 20
i2 - int16
i4 - int32
"""
dt = np.dtype([('country', 'S20'), ('density', 'i4'), ('area', 'i4'), ('population', 'i4')])
x = np.array([('Netherlands', 393, 41526, 16928800),
('Belgium', 337, 30510, 11007020),
('United Kingdom', 256, 243610, 62262000),
('Germany', 233, 357021, 81799600),
('Liechtenstein', 205, 160, 32842),
('Italy', 192, 301230, 59715625),
('Switzerland', 177, 41290, 7301994),
('Luxembourg', 173, 2586, 512000),
('France', 111, 547030, 63601002),
('Austria', 97, 83858, 8169929),
('Greece', 81, 131940, 11606813),
('Ireland', 65, 70280, 4581269),
('Sweden', 20, 449964, 9515744),
('Finland', 16, 338424, 5410233),
('Norway', 13, 385252, 5033675)],
             dtype=dt)
print(x[:4])
print(x['density'])
print(x['country'])
print(x['area'][2:5])


# example1:
# defining the user defined data type
time_type = np.dtype(np.dtype([('time', [('h', int), ('min', int), ('sec', int)]),
                               ('temperature', float)]))
times = np.array([((2, 42, 17), 20.8), ((13, 19, 3), 23.2)], dtype=time_type)
print(times)
print(times['time'])
print(times['time']['h'])
print(times['temperature'])


