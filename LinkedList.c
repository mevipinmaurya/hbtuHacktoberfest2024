/*EXPERIMENT : 05
Name : Shrusti Moon
Roll no : UEC2024145

Expt  : Develop  a program to create a single linked list using  dynamic memory allocation functions.
        Implement the following operation on the linked list.
        a) Display 
		b) Insert a node in the linked list (at front,at end ,in the middle )
		C) Delete a node  from the linked list(at front,at end, in the middle) 
		d)Display the  linked list in the reverse e)Revert  the linked list
*/

#include <stdio.h>
#include <stdlib.h>

// Define the structure of a node
struct node {
    int data;
    struct node *link;
};

// Function to display list
void display(struct node *curr) {
    if (curr == NULL)
        printf("\nLIST IS EMPTY!\n");
    else {
        printf("\nLinked List: ");
        while (curr != NULL) {
            printf("%d -> ", curr->data);
            curr = curr->link;
        }
        printf("NULL\n");
    }
}

// Function to display in reverse using recursion
void reverse_display(struct node *curr) {
    if (curr != NULL) {
        reverse_display(curr->link);
        printf("%d -> ", curr->data);
    }
}

// Main Program
int main() {
    struct node *head = NULL, *ptr, *current;
    int ch, sr, pos, fnd, n, ch2, ch3;
    char c1;

    // Create first node
    ptr = malloc(sizeof(struct node));
    printf("Enter first number: ");
    scanf("%d", &ptr->data);
    ptr->link = NULL;
    head = ptr;

    // Creation of further nodes
    do {
        printf("Do you want to create another node? (Y/N): ");
        scanf(" %c", &c1);
        if (c1 == 'Y' || c1 == 'y') {
            current = malloc(sizeof(struct node));
            printf("Enter the number: ");
            scanf("%d", &current->data);
            current->link = NULL;
            ptr->link = current;
            ptr = current;
        }
    } while (c1 == 'Y' || c1 == 'y');

    // Menu-driven operations
    do {
        printf("\n================ MENU ================\n");
        printf("1. Display Linked List\n");
        printf("2. Search by Data\n");
        printf("3. Insert Node\n");
        printf("4. Delete Node\n");
        printf("5. Reverse the Linked List\n");
        printf("6. Display in Reverse (Recursive)\n");
        printf("7. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &ch);

        switch (ch) {
            case 1:
                display(head);
                break;

            case 2: // Search
                printf("Enter the data to search: ");
                scanf("%d", &sr);
                pos = 1;
                fnd = 0;
                current = head;
                while (current != NULL) {
                    if (current->data == sr) {
                        fnd = 1;
                        break;
                    }
                    pos++;
                    current = current->link;
                }
                if (fnd)
                    printf("%d found at position %d\n", sr, pos);
                else
                    printf("Element not found!\n");
                break;

            case 3: // Insert
                printf("\nWhere do you want to insert the data?\n");
                printf("1. At the beginning\n");
                printf("2. After a given value\n");
                printf("3. At the end\n");
                printf("Enter your choice: ");
                scanf("%d", &ch2);

                {
                    struct node *p = malloc(sizeof(struct node));
                    printf("Enter data for the new node: ");
                    scanf("%d", &p->data);
                    p->link = NULL;

                    if (ch2 == 1) { // Beginning
                        p->link = head;
                        head = p;
                    } else if (ch2 == 2) { // After a given value
                        printf("Enter value after which to insert: ");
                        scanf("%d", &n);
                        current = head;
                        while (current != NULL && current->data != n)
                            current = current->link;
                        if (current == NULL) {
                            printf("Value not found!\n");
                            free(p);
                        } else {
                            p->link = current->link;
                            current->link = p;
                        }
                    } else if (ch2 == 3) { // End
                        current = head;
                        while (current->link != NULL)
                            current = current->link;
                        current->link = p;
                    } else {
                        printf("Invalid choice!\n");
                        free(p);
                    }
                }
                display(head);
                break;

            case 4: // Delete
                printf("\nWhere do you want to delete the node?\n");
                printf("1. At the beginning\n");
                printf("2. A specific value\n");
                printf("3. At the end\n");
                printf("Enter your choice: ");
                scanf("%d", &ch3);

                if (head == NULL) {
                    printf("List is empty!\n");
                    break;
                }

                if (ch3 == 1) { // Beginning
                    current = head;
                    head = head->link;
                    free(current);
                } else if (ch3 == 2) { // Specific value
                    printf("Enter data to delete: ");
                    scanf("%d", &n);
                    current = head;
                    struct node *prev = NULL;
                    while (current != NULL && current->data != n) {
                        prev = current;
                        current = current->link;
                    }
                    if (current == NULL)
                        printf("Value not found!\n");
                    else {
                        if (prev == NULL)
                            head = current->link;
                        else
                            prev->link = current->link;
                        free(current);
                    }
                } else if (ch3 == 3) { // End
                    current = head;
                    struct node *prev = NULL;
                    while (current->link != NULL) {
                        prev = current;
                        current = current->link;
                    }
                    if (prev == NULL)
                        head = NULL;
                    else
                        prev->link = NULL;
                    free(current);
                } else
                    printf("Invalid choice!\n");

                display(head);
                break;

            case 5: // Reverse linked list (iteratively)
                {
                    struct node *p = head, *q = NULL, *r = NULL;
                    while (p != NULL) {
                        r = q;
                        q = p;
                        p = p->link;
                        q->link = r;
                    }
                    head = q;
                    printf("List reversed successfully!\n");
                    display(head);
                }
                break;

            case 6: // Display in reverse (recursive)
                if (head == NULL)
                    printf("\nLIST IS EMPTY!\n");
                else {
                    printf("\nReverse Display: ");
                    reverse_display(head);
                    printf("NULL\n");
                }
                break;

            case 7:
                printf("Exiting the Program...\n");
                break;

            default:
                printf("Invalid choice! Please try again.\n");
        }
    } while (ch != 7);

    return 0;
}

/* OUTPUT :
C:\Users\shrus\OneDrive\Desktop\DSA Assignments\Assignment 6>LinkedList.exe
Enter first number: 2
Do you want to create another node? (Y/N): Y
Enter the number: 6
Do you want to create another node? (Y/N): Y
Enter the number: 4
Do you want to create another node? (Y/N): Y
Enter the number: 9
Do you want to create another node? (Y/N): Y
Enter the number: 5
Do you want to create another node? (Y/N): N

================ MENU ================
1. Display Linked List
2. Search by Data
3. Insert Node
4. Delete Node
5. Reverse the Linked List
6. Display in Reverse (Recursive)
7. Exit
Enter your choice: 1

Linked List: 2 -> 6 -> 4 -> 9 -> 5 -> NULL

================ MENU ================
1. Display Linked List
2. Search by Data
3. Insert Node
4. Delete Node
5. Reverse the Linked List
6. Display in Reverse (Recursive)
7. Exit
Enter your choice: 2
Enter the data to search: 4
4 found at position 3

================ MENU ================
1. Display Linked List
2. Search by Data
3. Insert Node
4. Delete Node
5. Reverse the Linked List
6. Display in Reverse (Recursive)
7. Exit
Enter your choice: 3

Where do you want to insert the data?
1. At the beginning
2. After a given value
3. At the end
Enter your choice: 1
Enter data for the new node: 3

Linked List: 3 -> 2 -> 6 -> 4 -> 9 -> 5 -> NULL

================ MENU ================
1. Display Linked List
2. Search by Data
3. Insert Node
4. Delete Node
5. Reverse the Linked List
6. Display in Reverse (Recursive)
7. Exit
Enter your choice: 3

Where do you want to insert the data?
1. At the beginning
2. After a given value
3. At the end
Enter your choice: 2
Enter data for the new node: 8
Enter value after which to insert: 6

Linked List: 3 -> 2 -> 6 -> 8 -> 4 -> 9 -> 5 -> NULL

================ MENU ================
1. Display Linked List
2. Search by Data
3. Insert Node
4. Delete Node
5. Reverse the Linked List
6. Display in Reverse (Recursive)
7. Exit
Enter your choice: 3

Where do you want to insert the data?
1. At the beginning
2. After a given value
3. At the end
Enter your choice: 3
Enter data for the new node: 7

Linked List: 3 -> 2 -> 6 -> 8 -> 4 -> 9 -> 5 -> 7 -> NULL

================ MENU ================
1. Display Linked List
2. Search by Data
3. Insert Node
4. Delete Node
5. Reverse the Linked List
6. Display in Reverse (Recursive)
7. Exit
Enter your choice: 4

Where do you want to delete the node?
1. At the beginning
2. A specific value
3. At the end
Enter your choice: 1

Linked List: 2 -> 6 -> 8 -> 4 -> 9 -> 5 -> 7 -> NULL

================ MENU ================
1. Display Linked List
2. Search by Data
3. Insert Node
4. Delete Node
5. Reverse the Linked List
6. Display in Reverse (Recursive)
7. Exit
Enter your choice: 4

Where do you want to delete the node?
1. At the beginning
2. A specific value
3. At the end
Enter your choice: 2
Enter data to delete: 4

Linked List: 2 -> 6 -> 8 -> 9 -> 5 -> 7 -> NULL

================ MENU ================
1. Display Linked List
2. Search by Data
3. Insert Node
4. Delete Node
5. Reverse the Linked List
6. Display in Reverse (Recursive)
7. Exit
Enter your choice: 4

Where do you want to delete the node?
1. At the beginning
2. A specific value
3. At the end
Enter your choice: 3

Linked List: 2 -> 6 -> 8 -> 9 -> 5 -> NULL

================ MENU ================
1. Display Linked List
2. Search by Data
3. Insert Node
4. Delete Node
5. Reverse the Linked List
6. Display in Reverse (Recursive)
7. Exit
Enter your choice: 5
List reversed successfully!

Linked List: 5 -> 9 -> 8 -> 6 -> 2 -> NULL

================ MENU ================
1. Display Linked List
2. Search by Data
3. Insert Node
4. Delete Node
5. Reverse the Linked List
6. Display in Reverse (Recursive)
7. Exit
Enter your choice: 6

Reverse Display: 2 -> 6 -> 8 -> 9 -> 5 -> NULL

================ MENU ================
1. Display Linked List
2. Search by Data
3. Insert Node
4. Delete Node
5. Reverse the Linked List
6. Display in Reverse (Recursive)
7. Exit
Enter your choice: 7
Exiting the Program...

*/
