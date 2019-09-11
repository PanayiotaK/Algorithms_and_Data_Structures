# Algorithms and Data Structures

* **Add_keys_to_Hash_Table** :
	* The file consists of two functions, `hash_quadratic` and `hash_double`. The initial hash function is h(k) = 6k + 3 mod 19.  
	* In `hash_quadratic` collisions are handled with quadratic probing. 
	* In `hash_double` collisions are handled using Double Hashing. 
(secondary hash function  h'(k) = 11 − (k mod 11) ).
* **Happy_numbers** :
	* The functions counts how many numbers between the given range are ephemeral. Which means their  k-descendant sequence reaches to 1. 
	* e.g. the 2-descendant sequence of 19. 
		* 19 → ($1^2$ + $9^2$ = 82 )82 → 68 → 100 → 1
	
* **validity_of_expression** :
	* The algorithm takes sum-and-product expression and checks if there are any pairs of brackets that are redundant; i.e. if their removal does not affect the calculation that is done. Stacks are used for the implantation of the algorithm.
*   **Hybrid_Sorting_algorithm** :
	* A hybrid sorting algorithm that uses Merge Sort and  Selection Sort. Selection Sort is used for any list of length four or less.
