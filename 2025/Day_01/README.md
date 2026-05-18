# Day 1 : Secret Entrance

[Link to puzzle](https://adventofcode.com/2025/day/1)

## Part 1 : Strategy

1. Convert rotation in positive number for right rotation and in negative number for left rotation.
2. Use modulo 100 on dial value to check when the dial point 0.
3. Increment the counter when it point 0.

## Part 2 : Strategy 
1. Keep Part 1 rotation converson
2. Check different cases :
  - Case 1 : the rotation is negative => increment the counter by a value of 1 + euclidian quotient divided by 100.
  - Case 2 : the rotation is greater than 100 => increment the counter by the euclidian quotient divided by 100.
  - Case 3 : the dial point 0 => increment the counter by a value of 1.
  - Case 4 : value between 1 and 99 => no increment.
