#include "lists.h"

listint_t *reverse_list(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * reverse_listint - reverses a singly-linked list
 * @head: pointer to head of the list to reverse
 *
 * Return: pointer to the head of the reversed list
 */

listint_t *reverse_list(listint_t **head)
{
	listint_t *node = *head, *next, *prev = NULL;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}

	*head = prev;
	return (*head);
}

/**
 * is_palindrome - verifies if a singly linked list is a palindrome.
 * @head: pointer to the head of the linked list.
 *
 * Return: 0 if the linked list is not a palindrome or 1 otherwise
 */

int is_palindrome(listint_t **head)
{
	listint_t *current, *reverse, *middle;
	size_t size = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	current = *head;
	while (current)
	{
		current = current->next;
        size += 1;
	}

	current = *head;
	for (i = 0; i < (size / 2) - 1; i++)
		current = current->next;

	if ((size % 2) == 0 && current->n != current->next->n)
		return (0);

	current = current->next->next;
	reverse = reverse_list(&current);
	middle = reverse;

	current = *head;
	while (reverse)
	{
		if (current->n != reverse->n)
			return (0);
		current = current->next;
		reverse = reverse->next;
	}
	reverse_list(&middle);

	return (1);
}
