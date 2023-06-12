#include "lists.h"

/**
 * is_palindrome - Checks if a linked list is a palindrome
 * @head: pointer to the head node of the list
 *
 * Return: 1 if the list is a palindrome, 0 if it isn't
 */
int is_palindrome(listint_t **head)
{
    listint_t *ptrSlow = *head, *ptrFast = *head, *ptrTemp = *head, *listDuplicated = NULL;

    if (*head == NULL || (*head)->next == NULL)
        return (1);
    while (1)
    {
        ptrFast = ptrFast->next->next;
        if (!ptrFast)
        {
            listDuplicated = ptrSlow->next;
            break;
        }
        if (!ptrFast->next)
        {
            listDuplicated = ptrSlow->next->next;
            break;
        }
        ptrSlow = ptrSlow->next;
    }
    flipLinkedList(&listDuplicated);
    while (listDuplicated && ptrTemp)
    {
        if (ptrTemp->n == listDuplicated->n)
        {
            listDuplicated = listDuplicated->next;
            ptrTemp = ptrTemp->next;
        }
        else
            return (0);
    }
    if (!listDuplicated)
        return (1);
    return (0);
}

/**
 * flipLinkedList - Flips the linked list
 * @head: pointer to the head node of the list
 *
 * Return: pointer to the head node of the flipped list
 */
void flipLinkedList(listint_t **head)
{
    listint_t *nodePrev = NULL;
    listint_t *nodeCurr = *head;
    listint_t *nextNode = NULL;

    while (nodeCurr)
    {
        nextNode = nodeCurr->next;
        nodeCurr->next = nodePrev;
        nodePrev = nodeCurr;
        nodeCurr = nextNode;
    }

    *head = nodePrev;
}
