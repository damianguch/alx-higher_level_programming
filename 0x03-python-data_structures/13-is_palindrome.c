#include "lists.h"

/**
 * is_palindrome - verify if singly linked list is palindrome
 * @head: pointer to head of singly linked list
 *
 * Return: 0 if list not a palindrome or 1 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	unsigned int size = 0, i = 0;
	int data[1024];

	if (head == NULL)
		return (0);

	if (*head == NULL)
		return (1);

	while (current)
	{
		current = current->next;
		size++;
	}

	if (size == 1)
		return (1);

	current = *head;
	while (current)
	{
		data[i++] = current->n;
		current = current->next;
	}

	for (i = 0; i <= (size/2); i++)
	{
		if (data[i] != data[size - i - 1])
			return (0);
	}
	return (1);
}
