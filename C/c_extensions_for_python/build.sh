# python3 setup.py build_ext --inplace
# gcc -shared -o Matrix_Operations.so -fPIC $(python3-config --includes) -I$(python3 -c "import numpy; print(numpy.get_include())") matrix_operations.c $(python3-config --ldflags)

# gcc -shared -o Matrix_Operations.so -fPIC \
#     -I"Users/mankulgupta/mankul/python-c-ext-env//include/python3.13" \
#     -I$(python3 -c "import numpy; print(numpy.get_include())") \
#     matrix_operations.c \
#     -L"Users/mankulgupta/mankul/python-c-ext-env/lib" -lpython3.13

# gcc -shared -o Matrix_Operations.so -fPIC \
#     $(python3-config --includes) \
#     -I$(python3 -c "import numpy; print(numpy.get_include())") \
#     matrix_operations.c \
#     $(python3-config --ldflags)


# NUMPY_INCLUDE="/Users/mankulgupta/mankul/cextforpy/lib/python3.13/site-packages/numpy/_core/include"

# clang -o MatrixOperations.so -shared -fPIC matrix_operations.c \ 
#   -I$("$NUMPY_INCLUDE") \
#   $(python3-config --includes) \
#   $(python3-config --ldflags)

#!/bin/bash

# # Get Python and NumPy include paths
# PYTHON_INCLUDE=$(python3 -c "from sysconfig import get_paths as gp; print(gp()['include'])")
# NUMPY_INCLUDE=$(python3 -c "import numpy; print(numpy.get_include())")

# # Print for debugging
# echo "Python include: $PYTHON_INCLUDE"
# echo "NumPy include: $NUMPY_INCLUDE"

# # Compile your C extension
# clang -shared -fPIC -o mymodule.so matrix_operations.c \
#   -I"$PYTHON_INCLUDE" \
#   -I"$NUMPY_INCLUDE" \
#   $(python3-config --ldflags)






