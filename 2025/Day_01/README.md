# Day 1 : Secret Entrance

[Link to puzzle]([https://www.pokebip.com/page/jeuxvideo/legendes-pokemon-z-a/guide-des-lieux/1e-arrondissement-beau-vert](https://adventofcode.com/2025/day/1))

## Part 1 : Strategy

1. Convert rotation in positive number for right rotation and in negative number for left rotation.
2. Use modulo 100 on dial value to check when the dial point 0.
3. Increment the counter when it point 0.

## Part 2 : Strategy 
1. Keep Part 1 rotation converson
2. Check if the current rotation is negative or greater than 99 and increment the euclidian division to count each time the dial point 0.
3. Check if the value equal zero to increment of 1.
