#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: pointer to the start of the linked list
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;		  /* move slow pointer one step */
		fast = fast->next->next;	/* move fast pointer two steps */

		if (slow == fast)  /* if they meet, then there's a cycle */
			return (1);
	}

	return (0);  /* no cycle found */
}
