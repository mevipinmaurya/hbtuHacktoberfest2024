'''
Question:

In a bustling market town, Akash the young mathematician stumbled upon an ancient book in the attic of his grandfather's house. The book whispered of a forgotten magic, where printing prime numbers from a to b could reveal hidden truths. Determined to unlock its secrets, Alex scoured pages filled with dusty formulas until he cracked the code.
User task:
You are given a range of number from a to b (both inclusive) and you need to print all of the primes between a and b.
A prime number is a number which have exacty two factors i.e. 1 and number itself.

Note:
This is a functional problem. You do not need to take any input. You just need to complete the function, and print the output.

Input:
First Line will contain an integer a representing the start of the range.
Second Line will contain an integer b representing the end of the range.

Constraints:
0 <= a, b <= 10,000
Output
Print all prime numbers between a and b.
Example
Input:
5
13

Output:
5 7 11 13
'''

# Answer

def print_primes_in_range(A, B):
    for i in range(A, B + 1):
        count = 0
        for j in range(1, i + 1):
            if i % j == 0:
                count += 1
        if count == 2:
            print(i, end=" ")
