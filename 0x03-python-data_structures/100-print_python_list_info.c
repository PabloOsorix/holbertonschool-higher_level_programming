#include <Python.h>

/**
 * print_python_list_info - This function Prints basic info about Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int size_of_py, allocated, j;
	PyObject *obj;

	size_of_py = Py_SIZE(p);
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size_of_py);
	printf("[*] Allocated = %d\n", allocated);

	for (j = 0; j < size_of_py; j++)
	{
		printf("Element %d: ", j);

		obj = PyList_GetItem(p, j);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}