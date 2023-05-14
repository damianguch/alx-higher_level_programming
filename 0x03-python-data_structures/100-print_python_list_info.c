#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists
 * @p: a pointer to a PyObject list
 */
void print_python_list_info(PyObject *p)
{
	int size, alloc, index;
	PyObject *list_obj;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (index = 0; index < size; index++)
	{
		printf("Element %d: ", i);

		list_obj = PyList_GetItem(p, index);
		printf("%s\n", Py_TYPE(list_obj)->tp_name);
	}
}
