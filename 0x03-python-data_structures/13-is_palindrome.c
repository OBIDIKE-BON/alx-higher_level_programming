#include "lists.h"

/**
 * checkForPalindrone - adds a new node at the end of a listint_t list
 * @left: pointer to pointer of first node of listint_t list
 * @right: pointer to be moved to the end
 * Return: 0, if the linked list is not a palindrone and 1 otherwise.
 */
int checkForPalindrone(listint_t **left, listint_t *right)
{
	int isPalindrone, isPal;

	if (right == NULL)
	{
		return (1);
	}

	isPalindrone = checkForPalindrone(left, right->next);
	if (!isPalindrone)
	{
		return (0);
	}

	isPal = (*left)->n == right->n ? 1 : 0;
	*left = (*left)->next;

	return (isPal);
}

/**
 * is_palindrome - checks if a listint_t list is a palindrone
 * @head: pointer to pointer of first node of listint_t list
 * Return: 0, if the linked list is not a palindrone and 1 otherwise.
 */
int is_palindrome(listint_t **head)
{
	listint_t *right = *head;
	listint_t **left = head;

	return (checkForPalindrone(left, right));
}
