// #include<Python.h>
// #include<numpy/arrayobject.h>

// // Function to be called from Python
// PyObject* matrix_multiplication(PyObject* self, PyObject* args) 
// {
//     PyObject *matrix1_obj, *matrix2_obj;
//     // Parse the input from Python
//     // if (!PyArg_ParseTuple(args, "0!0!", &PyList_Type, &list1 , &PyList_Type ,&list2)) {
//     // if (!PyArg_ParseTuple(args, "0ii0ii", &plist, &row1, &col1 , &plist , &row2 ,&col2)) {
//     if (!PyArg_ParseTuple(args, /*"O!O!"*/"OO", &matrix1_obj,  &matrix2_obj)) {
//         return NULL; // Error in parsing
//     }

//     PyArrayObject *matrix1 = (PyArrayObject *)matrix1_obj;
//     PyArrayObject *matrix2 = (PyArrayObject *)matrix2_obj;
    
//     // len1 = PyList_Size(list1);
//     // len2 = PyList_Size(list2);
//     if (matrix1->nd != 2 || matrix2->nd != 2) {
//         PyErr_SetString(PyExc_TypeError, "Input must be 2D arrays");
//         return NULL;
//     }
//     if (matrix1->dimensions[1] != matrix2->dimensions[0]) {
//         PyErr_SetString(PyExc_ValueError, "Incompatible dimensions for multiplication");
//         return NULL;
//     }
//     int rows1 = matrix1->dimensions[0];
//     int cols1 = matrix1->dimensions[1];
//     int rows2 = matrix2->dimensions[0];
//     int cols2 = matrix2->dimensions[1];

//     npy_intp dims[2] = {rows1, cols2};
//     PyArrayObject * result_matrix = (PyArrayObject *)PyArray_SimpleNew(2, dims, PyArray_TYPE(matrix1));

//     for (int i = 0; i < rows1; i++) {
//         for (int j = 0; j < cols2; j++) {
//             double sum = 0;
//             for (int k = 0; k < cols1; k++) {
//                 sum += *(double *)PyArray_GETPTR2(matrix1, i, k) * *(double *)PyArray_GETPTR2(matrix2, k, j);
//             }
//             *(double *)PyArray_GETPTR2(result_matrix, i, j) = sum;
//         }
//     }
//     return Py_BuildValue("0!", result_matrix);
// }

// PyMethodDef MyMethods[] = {
//     {"matrix_multiplication", matrix_multiplication, METH_VARARGS, "Multiply two matrices"},
//     {NULL, NULL, 0, NULL} // Sentinel
// };
// static struct PyModuleDef mymodule = {
//     PyModuleDef_HEAD_INIT,
//     "MatrixOperations", // name of module
//     NULL, // module documentation, may be NULL
//     -1, // size of per-interpreter state of the module
//     MyMethods
// };
// PyMODINIT_FUNC PyInit_mymodule(void) {
//     return PyModule_Create(&mymodule);
// }
// int main(int argc, char *argv[]) {
//     // Initialize the Python interpreter
//     Py_Initialize();
//     // Add the module to Python
//     PyInit_mymodule();
//     // Finalize the Python interpreter
//     Py_Finalize();
//     return 0;
// }
// // Compile with: gcc -shared -o mymodule.so -fPIC $(python3-config --includes) mymodule.c $(python3-config --ldflags)
// // Use in Python:
// // import mymodule
// // result = mymodule.add_numbers(5, 10)
// // print(result)  # Output: 15


// matrix_operations.c
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <numpy/arrayobject.h>

// Matrix multiplication function
static PyObject* matrix_multiplication(PyObject* self, PyObject* args) 
{
    PyObject *matrix1_obj, *matrix2_obj;

    if (!PyArg_ParseTuple(args, "OO", &matrix1_obj, &matrix2_obj)) {
        return NULL;
    }

    PyArrayObject *matrix1 = (PyArrayObject *)PyArray_FROM_OTF(matrix1_obj, NPY_DOUBLE, NPY_ARRAY_IN_ARRAY);
    PyArrayObject *matrix2 = (PyArrayObject *)PyArray_FROM_OTF(matrix2_obj, NPY_DOUBLE, NPY_ARRAY_IN_ARRAY);

    if (!matrix1 || !matrix2) {
        Py_XDECREF(matrix1);
        Py_XDECREF(matrix2);
        PyErr_SetString(PyExc_TypeError, "Invalid NumPy arrays.");
        return NULL;
    }

    if (PyArray_NDIM(matrix1) != 2 || PyArray_NDIM(matrix2) != 2) {
        Py_DECREF(matrix1);
        Py_DECREF(matrix2);
        PyErr_SetString(PyExc_TypeError, "Inputs must be 2D arrays.");
        return NULL;
    }

    int rows1 = PyArray_DIM(matrix1, 0);
    int cols1 = PyArray_DIM(matrix1, 1);
    int rows2 = PyArray_DIM(matrix2, 0);
    int cols2 = PyArray_DIM(matrix2, 1);

    if (cols1 != rows2) {
        Py_DECREF(matrix1);
        Py_DECREF(matrix2);
        PyErr_SetString(PyExc_ValueError, "Incompatible dimensions for multiplication.");
        return NULL;
    }

    npy_intp dims[2] = {rows1, cols2};
    PyArrayObject *result = (PyArrayObject *)PyArray_ZEROS(2, dims, NPY_DOUBLE, 0);

    for (int i = 0; i < rows1; ++i) {
        for (int j = 0; j < cols2; ++j) {
            double sum = 0;
            for (int k = 0; k < cols1; ++k) {
                double a = *(double *)PyArray_GETPTR2(matrix1, i, k);
                double b = *(double *)PyArray_GETPTR2(matrix2, k, j);
                sum += a * b;
            }
            *(double *)PyArray_GETPTR2(result, i, j) = sum;
        }
    }

    Py_DECREF(matrix1);
    Py_DECREF(matrix2);

    return PyArray_Return(result);
}

static PyMethodDef MyMethods[] = {
    {"matrix_multiplication", matrix_multiplication, METH_VARARGS, "Multiply two 2D NumPy arrays."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef MatrixOperationsModule = {
    PyModuleDef_HEAD_INIT,
    "MatrixOperations",  // <-- module name must match init function
    "Matrix multiplication with NumPy C API",
    -1,
    MyMethods
};

PyMODINIT_FUNC PyInit_MatrixOperations(void) {
    import_array();  // Required for NumPy C API
    return PyModule_Create(&MatrixOperationsModule);
}
