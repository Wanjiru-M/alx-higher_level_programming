#include <Python.h>

void print_python_list(PyObject *list_obj);
void print_python_bytes(PyObject *bytes_obj);

/**

print_python_list - Prints basic info about Python lists.

@list_obj: A PyObject list object.
*/
void print_python_list(PyObject *list_obj)
{
int size, alloc, i;
const char *type;
PyListObject *list = (PyListObject *)list_obj;
PyVarObject *var = (PyVarObject *)list_obj;

size = var->ob_size;
alloc = list->allocated;

printf("[] Python list info\n");
printf("[] Size of the Python List = %d\n", size);
printf("[*] Allocated = %d\n", alloc);

for (i = 0; i < size; i++)
{
type = list->ob_item[i]->ob_type->tp_name;
printf("Element %d: %s\n", i, type);
if (strcmp(type, "bytes") == 0)
print_python_bytes(list->ob_item[i]);
}
}

/**

print_python_bytes - Prints basic info about Python byte objects.

@bytes_obj: A PyObject byte object.
*/
void print_python_bytes(PyObject *bytes_obj)
{
unsigned char i, size;
PyBytesObject *bytes = (PyBytesObject *)bytes_obj;

printf("[.] bytes object info\n");
if (strcmp(bytes_obj->ob_type->tp_name, "bytes") != 0)
{
printf(" [ERROR] Invalid Bytes Object\n");
return;
}

printf(" size: %ld\n", ((PyVarObject *)bytes_obj)->ob_size);
printf(" trying string: %s\n", bytes->ob_sval);

if (((PyVarObject *)bytes_obj)->ob_size > 10)
size = 10;
else
size = ((PyVarObject *)bytes_obj)->ob_size + 1;

printf(" first %d bytes: ", size);
for (i = 0; i < size; i++)
{
printf("%02hhx", bytes->ob_sval[i]);
if (i == (size - 1))
printf("\n");
else
printf(" ");
}
}
