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
    listint_t *start = NULL, *end = NULL;
    unsigned int i = 0, len = 0, len_cyc = 0, len_list = 0;

    if (head == NULL)
        return (0);

    if (*head == NULL)
        return (1);

    start = *head;
    len = listint_len(start);
    len_cyc = len * 2;
    len_list = len_cyc - 2;
    end = *head;

    for (; i < len_cyc; i = i + 2)
    {
        if (start[i].n != end[len_list].n)
            return (0);

        len_list = len_list - 2;
    }

    return (1);
}

/**
  * slistint_len - counting numbers within the list
  * @h: The linked list to count
  *
  * Return:Upon Success - Number of elements
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


/**
  * get_nodeint_at_index - getting node from a linked list
  * @head: The head of the linked list
  * @index: The index to find in the linked list
  *
  * Return: (Upon Success - Node found)
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

