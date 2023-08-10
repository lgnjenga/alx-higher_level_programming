#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list.
 *
 * @head: A pointer to the head of the linked list.
 * @number: The number to insert.
 *
 * Return: If the function fails - NULL.
 * Otherwise - the address of the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));
	listint_t *current = *head, *prev = NULL;

	if (!new_node)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	/* If list is empty or number is less than the first node's value */
	if (!*head || (*head)->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	/* Traverse the list to find the appropriate position */
	while (current && current->n < number)
	{
		prev = current;
		current = current->next;
	}

	/* Insert the new node */
	new_node->next = current;
	prev->next = new_node;

	return (new_node);
}
