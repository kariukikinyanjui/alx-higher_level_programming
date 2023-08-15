#include "lists.h"
/**
 * print_python_list_info - Prints basic information about Python lists.
 * @p: Pointer to the Python object (list) for which info is to be printed.
 */
void print_python_list_info(PyObject *p)
{
	int size = PyList_Size(p);
	int allocated = ((PyListObject *)->p)->allocated;
	int i;
	const char *item_type;

	printf("[] Size of the Python List = %d\n", allocated);
	printf("[*} Allocated = %d\n", allocated);

	for (i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);

		item_type = Py_TYPE(item)->tp_name;
		printf("Element %d: %s\n", i, item_type);
	}


}

