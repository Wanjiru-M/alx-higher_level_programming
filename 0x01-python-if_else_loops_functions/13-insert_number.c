#include "lists.h"
#include <stdlib.h>
#include <unistd.h>

listint_t *insert_node(listint_t **head, int number)
{
	if (!head)
		return NULL;

	listint_t *new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return NULL;

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL || (*head)->n > number)
	{
		new_node->next = *head;
		*head = new_node;
		return new_node;
	}

	listint_t *current = *head;
	listint_t *previous = NULL;

	while (current && current->n < number)
	{
		previous = current;
		current = current->next;
	}

	previous->next = new_node;
	new_node->next = current;

	return new_node;
}
