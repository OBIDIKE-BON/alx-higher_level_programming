#include "lists.h"
#include <stdlib.h>

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *temp = *head;

	if (head == NULL)
		return (NULL);

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;

	if (*head == NULL)
	{
		*head = new_node;
		new_node->next = NULL;
		return (new_node);
	}
	if (*head == NULL || (*head)->n > number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	while (temp->next)
	{
		if (temp->next->n >= number)
		{
			new_node->next = temp->next;
			temp->next = new_node;
			return (new_node);
		}
		temp = temp->next;
	}
	new_node->next = NULL;
	temp->next = new_node;

	return (new_node);
}