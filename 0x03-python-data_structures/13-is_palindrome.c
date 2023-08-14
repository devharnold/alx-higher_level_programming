#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
  * is_palindrome - Checks if the list is Palindrome
  * @head: The head of the singly linked list
  *
  * Return: 0 if it is not a palindrome, 1 if it is a palindrome
  */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head, *fast = *head, *prev = NULL;

    if (*head == NULL || (*head)->next == NULL)
        return (1);

    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        listint_t *next = slow->next;
        slow->next = prev;
        prev = slow;
        slow = next;
    }

    if (fast != NULL)
        slow = slow->next;

    while (slow != NULL)
    {
        if (slow->n != prev->n)
            return (0);
        slow = slow->next;
        prev = prev->next;
    }

    return (1);
}

/**
  * get_nodeint_at_index - getting node from a linked list
  * @head: The head of the linked list
  * @index: The index to find in the linked list
  *
  * Return: Upon Success - The nodes of the list
  */
listint_t *get_nodeint_at_index(listint_t *head, unsigned int index)
{
        listint_t *current = head;
        unsigned int iter_times = 0;

        if (head)
        {
                while (current != NULL)
                {
                        if (iter_times == index)
                                return (current);

                        current = current->next;
                        ++iter_times;
                }
        }

        return (NULL);
}

/**
  * slistint_len - counting numbers within the list
  * @h: The linked list to count
  *
  * Return: Upon Success - Element numbers
  */

size_t listint_len(const listint_t *h)
{
        int lenght = 0;

        while (h != NULL)
        {
                ++lenght;
                h = h->next;
        }

        return (lenght);
}

