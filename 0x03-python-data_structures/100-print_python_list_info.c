#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *list_obj)
{
    long int size = PyList_Size(list_obj);
    PyListObject *list = (PyListObject *)list_obj;

    printf("[*] Size of the Python List = %li\n", size);
    printf("[*] Allocated = %li\n", list->allocated);

    PyObject **items = list->ob_item;
    int i = 0;
    while (i < size)
    {
        PyObject *item = items[i];
        const char *type_name = Py_TYPE(item)->tp_name;
        printf("Element %i: %s\n", i, type_name ? type_name : "<unknown>");
        i++;
    }
}
