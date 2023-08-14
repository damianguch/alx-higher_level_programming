#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: head of linked list
 * @number: data
 *
 * Return: address of new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = NULL;
	listint_t *newNode = NULL;

	if (!head)
		return (NULL);

	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);
	newNode->n = number;
	newNode->next = NULL;

	if (*head == NULL)
	{
		*head = newNode;
		(*head)->next = NULL;
		return (newNode);
	}

	if ((*head)->next == NULL)
	{
		if ((*head)->n < newNode->n)
			(*head)->next = newNode;
		else
		{
			newNode->next = *head;
			*head = newNode;
		}
		return (newNode);
	}

	temp = *head;
	while (temp->next != NULL)
	{
		if (newNode->n < temp->n)
		{
			newNode->next = temp;
			*head = newNode;
			return (newNode);
		}
	
		if (((newNode->n > temp->n) && (newNode->n < (temp->next)->n)) 
				|| (newNode->n == temp->n))
		{
			newNode->next = temp->next;
			temp->next = newNode;
			return (newNode);
		}
		temp = temp->next;
	}

	temp->next = newNode;
	return (newNode);
}
