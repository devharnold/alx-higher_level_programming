#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
/**
 * print_python_list_info - Print some basic info about Python lists
 * @p: PyObject
 *
 * Return: Nothing
 */
void print_python_list_info(PyObject *p)
{
PyObject *item;
PyListObject *list = (PyListObject *)p;
int i, size, alloc;

size = Py_SIZE(p);
alloc = list->allocated;
printf("[*] Allocated = %d\n", alloc);
printf("[*] Size of the Python List = %d\n", size);

for (i = 0; i < size; i++)
{
item =  PyList_GetItem(p, i);
printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
}
}
