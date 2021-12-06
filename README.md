# PythonLearning
## Exercise 1: Gravitational Force
Gravitational force is the attractive force that exists between two masses. It can be calculated by using the following formula:

    Fg = G*M*m/(r ** 2)
G is the gravitational constant, M and m are the two masses, and r is the distance between them.

You must implement this equation in Python to calculate the gravitational force between Earth and the moon.

## Exercise 2: Discounted Price
In this challenge, you must discount a price according to its value.

 - If the price is 300 or above, there will be a 30% discount.

 - If the price is between 200 and 300 (200 inclusive), there will be a 20% discount.

 - If the price is between 100 and 200 (100 inclusive), there will be a 10% discount.

 - If the price is less than 100, there will be a 5% discount.

 - If the price is negative, there will be no discount.

## Exercise 3: The Factorial! 
In this challenge, you must implement the `factorial()` function. It takes an integer as a parameter and calculates its factorial. Python does have a built-in factorial function but you’ll be creating your own for practice.

## Exercise 4: Balanced Brackets
Given a string containing only square brackets, [], you must check whether the brackets are balanced or not. The brackets are said to be balanced if, for every opening bracket, there is a closing bracket.

You will write your code in the `check_balance()` function, which returns True if the brackets are balanced and False if they are not.

For an empty string, the function will return True.

For the sake of simplicity, you can assume that the string will not contain any other characters.
![brackets](brackets.png)

## Exercise 5: A Sum of Zero
You must implement the `check_sum()` function which takes in a list and returns True if the sum of two numbers in the list is zero. If no such pair exists, return False.
![sum](sum.png)

## Exercise 6: Fibonacci Series
The Fibonacci sequence is a series of numbers where every number is the sum of the two numbers before it. The first two numbers are 0 and 1:

    0 1 1 2 3 5 8 13
You must write the `fib()` function which takes in a positive integer, n, and returns the n-th Fibonacci number. However, instead of using recursion, your function must use any of the loops.

## Exercise 7: From List to Tuple
You are given a list called my_list. Using this list, you must create a tuple called `my_tuple`. The tuple will contain the list’s first element, last element, and the length of the list, in that same order.

## Exercise 8: Kth Maximum Integer in a List
Given a list of integers and a number k, find the kth largest integer in the list. The integer will be stored in the kth_max variable.

For example, with a list of 7 integers, if k = 2, then kth_max will be equal to the second-largest integer in the list. 
If k = 6, kth_max will equal the 6th largest integer.
 
## Exercise 9: Highs and Lows
You must implement the `count_low_high()` function. Its parameter is a list of numbers.

If a number is greater than 50 or divisible by 3, it will count as a high. If these conditions are not met, the number is considered a low.

At the end of the function, you must return a list that contains the number of lows and highs, in that order.

In case the list is empty, you may return None.

