# Efficient Janitor - Hackerrank solution

I received from Estrátegia Educacional a Hackerrank test for a Dev Full Stack slot.
Unfortunately it took me longer than proposed to solve the test, but I share the code in this repository.

# Problem description:

The janitor at Hacker High School is insanely efficient. By the end of each day, all of the waste from the trash cans in the school has been shifted into plastic bags which can carry waste weighing between 1.01 pounds and 3.00 pounds. 

All of the plastic bags must be dumped into the trash cans outside the school. The janitor can carry at most 3.00 pounds at once. One trip is described as selecting a few bags which together don't weigh more than 3.00 pounds, dumping them in the outdoor trash can and returning to the school. 

The janitor wants to make minimum number of trips to the outdoor trash can. 
Given the number of plastic bags, n, and the weights of each bag, determine the minimum number of trips if the janitor selects bags in the optimal way.

For example, given n = 6 plastic bags weighing weight = [1.01, 1.99, 2.5, 1.5, 1.01], the janitor can carry all of the trash out in 3 trips: [1.01 + 1.99 , 2.5, 1.5 + 1.01].

## Function Description:
Complete the function efficientJanitor in the editor below. The function must return a single integer that represents the minimum number of trips to be made.

efficientJanitor has the following parameter(s):
weight[weight[0],...weight[n-1]]: an array of floating-point integers

## Constraints
 - 1 ≤ n ≤ 1000
 - 1.01 ≤ weight[i] ≤ 3.0

## Input Format For Custom Testing
The first line contains an integer, n, that denotes the number of
elements in weight.

Each line i of the n subsequent lines (where 0 ≤ i < n) contains an integer that describes weight[i].

## Sample Case 0
Sample Input For Custom Testing
```sh
5
1.50
1.50
1.50
1.50
1.50
```
Sample Output
```sh
3
````
Explanation
In this case, the janitor will carry the first 2 plastic bags together, the 3rd and 4rd together and the last one alone to dispose of all of the trash in 3 trips.

## Sample Case 1
Sample Input For Custom Testing
```sh
4
1.50
1.50
1.50
1.50 
```
Sample Output
```sh
2
````

Explanation
In this case, the janitor will carry the first 2 plastics bags together and the 3rd and 4rd together requiring only 2 trips.


