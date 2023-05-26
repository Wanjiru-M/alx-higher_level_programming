#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
#include <stddef.h>

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Pointer to the head node of the linked list.
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	int values[9999];
	int count = 0, left = 0, right = 0;
	listint_t *current = *head;

	if (!current || !current->next)
		return (1);

	while (current)
	{
		values[count] = current->n;
		current = current->next;
		count++;
	}

	right = count - 1;

	while (left < right)
	{
		if (values[left] != values[right])
			return (0);
		left++;
		right--;
	}

	return (1);
}
