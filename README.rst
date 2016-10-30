About Project Euler
===================
(Pasted from the Project Euler homepage)
Project Euler is a series of challenging mathematical/computer programming problems that will
require more than just mathematical insights to solve. Although mathematics will help you arrive
at elegant and efficient methods, the use of a computer and programming skills will be required
to solve most problems.

The motivation for starting Project Euler, and its continuation, is to provide a platform for
the inquiring mind to delve into unfamiliar areas and learn new concepts in a fun and recreational
context.

Inspiration
============
I heard about Project Euler completely by accident. I was fascinated by the beautiful features of
amicable numbers(亲和数), and there happened to be a related problem(`Problem 21 <https://projecteuler.net/problem=21>`_)
distributed by Project Euler. However, what I have learned was far beyond what I expected.
A new world was open for me, a world of mathematics and algorithm, full of unknowns and miracles.
It was so attractive that I could not stop myself exporing it.

In the beginning, I just solved those problems and uploaded my Python solutions named with
the official problem indices. However, as I approached, I found the problems are not independent
and many are closely related each other, so I reorganized the work and categorized the problems
(and also solutions). After that, ah, doesn't it like a gallery, a space for my little programs,
themed with the art of computer programming?

Now, enjoy yourself！

Gallery
========
Category
--------
- `Combinations and permutations`_
- `Dynamic programming`_
- `Encryption and decryption`_
- `Figurate number`_
- `Fraction and decimals`_
- `Games`_
- `Interesting number games`_
- `Prime number related`_
- `Pythagorean triplet`_
- `Recursive definition`_
- `Totient function`_
- `Unclassified`_

Items for each work
----------------------
- task
    Simple description of original problem
- key point
    The key point (core idea) for me to solve the problem
- programming aspect
    Related programming concept
- class
    - mathematics: mathematical insights may be more important for the corresponding problem
    - programming: your programming skills outweighs the mathematics
- difficulty
    - ★: pretty easy, several minutes were enough
    - ★★: easy, within an hour
    - ★★★: medium, 1-3 hours
    - ★★★★: difficult, I needed to look up additional definitions, theorems and algorithms
    - ★★★★★: very difficult, it took me more than 1 day to master the underlying tricks

.. note:: You'll quickly find (or at least outline) a brute-force algorithm for many problems.
   It's not so easy to devise an elegant solution yet. However, that's the source of the real fun.

Combinations and permutations
----------------------------
Combinations and permutations play a vital role in mathematics and computer science. It's
prerequisite to Probability, Graph Theory, etc. Project Euler does include several problems in this
field.

- `Problem 24: Lexicographic permutations <gallery/Combinations-and-permutations/Problem-24.py>`_:
  
  - task
      What is the millionth lexicographic permutation of the digits 0-9?
  - key point
      Quite easy for Python using *itertools* standard library
  - programming aspect
      for loop
  - class
      programming
  - difficulty
      ★

- `Problem 29: Distinct powers <gallery/Combinations-and-permutations/Problem-29.py>`_:

  - task
      How many distinct numbers can a^b generate for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?
  - key point
      Two layers of loops, *set* for removing repeats
  - programming aspect
      for loop, data structure selection
  - class
      programming
  - difficulty
      ★

- `Problem 53: Combinatoric selections <gallery/Combinations-and-permutations/Problem-53.py>`_:

  - task
      How many values of nCr, for 1 ≤ n ≤ 100 and r ≤ n, are greater than 1000000?
  - key point
      factorial and combinatorics
  - programming aspect
      flow of the excution, *math* standard library
  - class
      programming
  - difficulty
      ★

- `Problem 90: Cube digit pairs <gallery/Combinations-and-permutations/Problem-90.py>`_:

  - task
      How many distinct arrangements of the two cubes allow for all of the square numbers to be
      displayed?
  - key point
      We need two function, one for iterating all combinations, another for square number checking.
  - programming aspect
      *itertools* standard library, data structure selection
  - class
      programming
  - difficulty
      ★

- `Problem 93: Arithmetic expressions <gallery/Combinations-and-permutations/Problem-93.py>`_:

  - task
      Using four distinct digits and rules of arithmetic, find the longest set of consecutive
      positive target integers
  - key point
      brute force
  - programming aspect
      data structure selection, string formatting operations, *itertools* standard library, *eval*
  - class
      programming
  - difficulty
      ★★★

- `Problem 100: Arranged probability <gallery/Combinations-and-permutations/Problem-100.py>`_:

  - task
      What is the first arrangement containing over 10^12 coloured(only blue and red) discs, so
      that there is exactly 50% chance of taking two blue discs at random?
  - key point
      quadratic Diophantine Equation(丢番图方程) with two variables
  - programming aspect
      while loop, multiple assignment
  - class
      mathematics
  - difficulty
      ★★★

Dynamic programming
--------------------
Dynamic programming is a widely used method for solving a complex problem by breaking it down
into a collection of subproblems. For each subproblem, one simply looks up the computed solution
of the previous subproblem, thereby saving computation time greatly. Dynamic programming, or the
thinking behind it fit for many problems in Project Euler.

- `Problem 15: Lattice paths <gallery/Dynamic-programming/Problem-15.py>`_:

  - task
      Count the number of routes through a 20×20 grid
  - key point
      the problem can be split into subproblems, and the result from the last stage can be passed
      to the current stage
  - programming aspect
      for loop, matrix representation and operation
  - class
      programming
  - difficulty
      ★★

- `Problem 18 and 67: Maximum path sum <gallery/Dynamic-programming/Problem-18/Problem-18.py>`_:

  - task
      Find the maximum total from top to bottom of the triangle
  - key point
      Classical example of dynamic programming
  - programming aspect
      flow of the excution, *list* and indices
  - class
      programming
  - difficulty
      ★★★

- `Problem 31, 76 and 77: Coin sums <gallery/Dynamic-programming/Problem-31.py>`_:

  - task
      Problems 31 asks how many different ways can £2 be made using any number of coins?
      And Problem 76 asks how many different ways can 100 be written as a sum of at least
      two positive integers. Problem 77 is the same as 76 except additional prime number
      limitation. Overall we need to find an algorithm for counting ways of partitioning
      numbers.
  - key point
      If I split 100 into 99 and 1, then the problem becomes a little smaller, and I ask
      myself how many ways can 99 be expressed as sum of much smaller integers? And then 98,
      then 97, ..., in the end, the problem turns out to be trivial, and all we need to anwser
      is how many ways to partition 2.
  - programming aspect
      for loop, *list*
  - class
      programming
  - difficulty
      ★★★

- `Problem 81: Path sum: two ways <gallery/Dynamic-programming/Problem-81/Problem-81.py>`_:

  - task
      Find the minimum path sum from the top left to the bottom right by only moving right and
      down.
  - key point
      Recall `Problem 18 <gallery/Dynamic-programming/Problem-18/Problem-18.py>`_
  - programming aspect
      flow of the excution, *list*, *map*
  - class
      programming
  - difficulty
      ★★★

- `Problem 82: Path sum: three ways <gallery/Dynamic-programming/Problem-82/Problem-82.py>`_:

  - task
      Find the minimum path sum from the left column to the right column by only moving up
      down, and right.
  - key point
      Recall `Problem 81 <gallery/Dynamic-programming/Problem-81/Problem-81.py>`_
  - programming aspect
      flow of the excution, *list*, *map*
  - class
      programming
  - difficulty
      ★★★

- `Problem 83: Path sum: four ways <gallery/Dynamic-programming/Problem-83/Problem-83.py>`_:

  - task
      Find the minimum path sum from the top left to the bottom right by moving left, right,
      up and down.
  - key point
      Although similar to `Problem 81 <gallery/Dynamic-programming/Problem-81/Problem-81.py>`_
      and `Problem 82 <gallery/Dynamic-programming/Problem-82/Problem-82.py>`_, this problem
      can not be translated into the dynamic programming pattern since we can move in any
      direction. Dijkstra's algorithm may be a good choice then.
  - programming aspect
      priority queue
  - class
      programming
  - difficulty
      ★★★★

Encryption and decryption
-------------------------
Passcode, encryption, and decryption are almost everywhere during modern information transmission.
Several problems have direct connections with this topic.

- `Problem 59: XOR decryption <gallery/Encryption-and-decryption/Problem-59/Problem-59.py>`_:

  - task
      Can you decrypt the XOR encrypted ASCII code given that the encryption key consists of three
      lower case characters?
  - key point
      The most frequent character in English is the space.
  - programming aspect
      Python XOR operation(^)
  - class
      programming
  - difficulty
      ★★★

- `Problem 79: Passcode derivation <gallery/Encryption-and-decryption/Problem-79/Problem-79.py>`_:

  - task
      Deduce the whole secret passcode by analysing historical login attempts.
  - key point
      topological sorting
  - programming aspect
      *set*, *dict*, *reduce*, *generator*
  - class
      programming
  - difficulty
      ★★★★


Figurate number
---------------
A figurate number is a number represented as a regular and discrete geometric pattern(e.g. dots) such
as polygonal number or a polyhedral number. Triangle, square, pentagonal, hexagonal, heptagonal, and
octagonal numbers are involved in Project Euler.

- `Problem 42: Coded triangle numbers <gallery/Figurate-number/Problem-42/Problem-42.py>`_:

  - task
      According to the definition given in the problem statement, how many triangle words does
      the list contain?
  - key point
      ascii_uppercase defined in *string* standard library
  - programming aspect
      *dict*, list comprehension, dot notation
  - class
      programming
  - difficulty
      ★★

- `Problem 44: Pentagon numbers <gallery/Figurate-number/Problem-44.py>`_:

  - task
      Find the pair of pentagonal numbers for which their sum and difference are also
      pentagonal and the difference is minimised.
  - key point
      the difference of the first eligible pair is minimised
  - programming aspect
      while loop, return statement, dead code
  - class
      programming
  - difficulty
      ★★

- `Problem 45: Triangular, pentagonal, and hexagonal <gallery/Figurate-number/Problem-45.py>`_:

  - task
      After 40755, find the next triangle number that is also pentagonal and hexagonal.
  - key point
      When n is odd, the triangle number is a hexagonal number.
  - programming aspect
      while loop, return statement, dead code
  - class
      programming
  - difficulty
      ★★

- `Problem 61: Cyclical figurate numbers <gallery/Figurate-number/Problem-61.py>`_:

  - task
      Find the sum of the only ordered set of six cyclic 4-digit numbers for which each polygonal
      type: triangle, square, pentagonal, hexagonal, heptagonal, and octagonal, is represented by
      a different number in the set.
  - key point
      brute force
  - programming aspect
      generator, flow of the excution
  - class
      programming
  - difficulty
      ★★★


Fraction and decimals
---------------------
As you might guess, this category is full of mathematics. You may feel a bit boring at the beginning,
just hold on, and a lot of wonders will come.

- `Problem 26: Reciprocal cycles <gallery/Fraction-and-decimals/Problem-26.py>`_:

  - task
      Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal
      fraction part.
  - key point
      Simulate the long division procedure and keep track of the remainders, recurring cycle can be
      easily obtained. Larger d may generate longer recurring cycle.
  - programming aspect
      flow of the excution
  - class
      programming
  - difficulty
      ★★★

- `Problem 57: Square root convergents <gallery/Fraction-and-decimals/Problem-57.py>`_:

  - task
      Investigate the expansions of the continued fraction of square root of 2, in the first 1000
      expansions, how many fractions contain a numerator with more digits than denominator?
  - key point
      Delve the calculation procedure of the iterations, and try to find some patterns for
      generating numerator and denominator recursively.
  - programming aspect
      for loop
  - class
      mathematics
  - difficulty
      ★★★

- `Problem 64: Odd period square roots <gallery/Fraction-and-decimals/Problem-64.py>`_:

  - task
      How many continued fractions for N ≤ 10000 have an odd period?
  - key point
      There's an iterative algorithm for non perfect squares to calculate continued fraction
      expansions
  - programming aspect
      flow of the excution
  - class
      mathematics
  - difficulty
      ★★★★

- `Problem 65: Convergents of e <gallery/Fraction-and-decimals/Problem-65.py>`_:

  - task
      Find the sum of digits in the numerator of the 100th convergent of the continued
      fraction for e.
  - key point
      I found a recursive formula about the numerator: n(k) = c(k) * n(k-1) + n(k-2)
  - programming aspect
      generator
  - class
      mathematics
  - difficulty
      ★★★

- `Problem 66: Diophantine equation <gallery/Fraction-and-decimals/Problem-66/Problem-66.py>`_:

  - task
      Investigate the Diophantine equation x^2 − Dy^2 = 1.
  - key point
      Fundamental solution of Pell's equation
  - programming aspect
      flow of the excution
  - class
      mathematics
  - difficulty
      ★★★★


Games
-----
Games excite us, and computing makes us crazy!

- `Problem 54: Poker hands <gallery/Games/Problem-54/Problem-54.py>`_:

  - task
      Game poker: how many hands does Player 1 win?
  - key point
      The rules are clear, just simulate the game.
  - programming aspect
      *class*, operator overloading
  - class
      programming
  - difficulty
      ★★★★

- `Problem 68: Magic 5-gon ring <gallery/Games/Problem-68.py>`_:

  - task
      What is the maximum 16-digit string for a “magic” 5-gon ring?
  - key point
      put 1,2,3,4,5 to the inner ring, and 6,7,8,9,10 to the outer ring
  - programming aspect
      *class*, *itertools* standard library
  - class
      programming
  - difficulty
      ★★★

- `Problem 84: Monopoly odds <gallery/Games/Problem-84.py>`_:

  - task
      In the game Monopoly(大富翁), find the three most frequent squares using 4-sided dice.
  - key point
      Simulation
  - programming aspect
      generator, recursive function, code, *random* and *collections* standard library
      dict comprehension
  - class
      programming
  - difficulty
      ★★★

- `Problem 96: Su Doku <gallery/Games/Problem-96/Problem-96.py>`_:

  - task
      Write a solver for 9×9 Su Doku(数独)
  - key point
      exact cover problem, Algorithm X
  - programming aspect
      recursive function, generator, *set*, *dict*, *list*, object serializarion
  - class
      programming
  - difficulty
      ★★★★★


Interesting number games
------------------------
Number theory, or in older usage, arithmetic is a branch of pure mathematics devoted primarily to
the study of integers. Many of us studied the related concepts in primary school. However, we can
never say we truly master them. From this section, you'll certainly find much more interesting
truth beneath the surface.

- `Problem 4: Largest palindrome product <gallery/Interesting-number-games/Problem-4.py>`_:

  - task
      Find the largest palindrome made from the product of two 3-digit numbers.
  - key point
      brute force
  - programming aspect
      for loop, string slices
  - class
      programming
  - difficulty
      ★

- `Problem 21: Amicable numbers <gallery/Interesting-number-games/Problem-21.py>`_:

  - task
      Evaluate the sum of all the amicable numbers under 10000.
  - key point
      brute force
  - programming aspect
      flow of the excution, mathematical operators
  - class
      programming
  - difficulty
      ★★

- `Problem 23: Non-abundant sums <gallery/Interesting-number-games/Problem-23.py>`_:

  - task
      Find the sum of all the positive integers which cannot be written as the sum of two abundant
      numbers.
  - key point
      brute force
  - programming aspect
      mathematical operators, bool array
  - class
      programming
  - difficulty
      ★★

- `Problem 30: Digit fifth powers <gallery/Interesting-number-games/Problem-30.py>`_:

  - task
      Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
  - key point
      the upper bound of the iteration, 5 * 9 ** 5 = 295245, 6 * 9 ** 5 = 354294
  - programming aspect
      for loop, mathematical operator
  - class
      mathematics
  - difficulty
      ★★

- `Problem 32: Pandigital products <gallery/Interesting-number-games/Problem-32.py>`_:

  - task
      Find the sum of all products whose multiplicand/multiplier/product identity can be written as a
      1 through 9 pandigital.
  - key point
      brute force, but limit the search space carefully, make a table showing the total digit number
      based on the digit number of the multiplier and the multiplicand.
  - programming aspect
      flow of the excution, string concatenation
  - class
      mathematics
  - difficulty
      ★★

- `Problem 33: Digit cancelling fractions <gallery/Interesting-number-games/Problem-33.py>`_:

  - task
      According to the cancelling operation, find all four fractions desired.
  - key point
      consider 4 possibilities: (10i + n) / (10i + d) = n / d, (10n + i) / (10d + i) = n / d,
      (10i + n) / (10d + i) = n / d, and (10n + i) / (10i + d) = n / d, where n < d.
  - programming aspect
      flow of the excution, mathematical operations
  - class
      mathematics
  - difficulty
      ★★★

- `Problem 34: Digit factorials <gallery/Interesting-number-games/Problem-34.py>`_:

  - task
      Find the sum of all numbers which are equal to the sum of the factorial of their digits.
  - key point
      upper bound determination, 6 * 9! = 2177280, 7 digits, 7 * 9! = 2540160, 7 digits,
      8 * 9! = 2903040, 7 digits
  - programming aspect
      for loop, *fractorial* function defined in *math* standard library
  - class
      mathematics
  - difficulty
      ★★

- `Problem 36: Double-base palindromes <gallery/Interesting-number-games/Problem-36.py>`_:

  - task
      Find the sum of all numbers, less than one million, which are palindromic in base 10 and
      base 2.
  - key point
      brute force
  - programming aspect
      flow of the excution, built-in *bin* function
  - class
      programming
  - difficulty
      ★★

- `Problem 38: Pandigital multiples <gallery/Interesting-number-games/Problem-38.py>`_:

  - task
      What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated
      product of an integer with (1,2, ... , n) where n > 1?
  - key point
      try to discover some features the fixed integer must have to limit the search space
  - programming aspect
      flow of the excution
  - class
      mathematics
  - difficulty
      ★★

- `Problem 43: Sub-string divisibility <gallery/Interesting-number-games/Problem-43.py>`_:

  - task
      Find the sum of all 0 to 9 pandigital numbers with the defined sub-string divisibility property.
  - key point
      *permutation* function defined in *itertools* standard library, brute force
  - programming aspect
      flow of the excution, *itertools* standard library, string slices, string concatenation
  - class
      programming
  - difficulty
      ★★

- `Problem 52: Permuted multiples <gallery/Interesting-number-games/Problem-52.py>`_:

  - task
      Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
  - key point
      the first 10*n/6 numbers for n = 1, 10, 100, ...
  - programming aspect
      flow of the excution
  - class
      programming
  - difficulty
      ★★

- `Problem 55: Lychrel numbers <gallery/Interesting-number-games/Problem-55.py>`_:

  - task
      How many Lychrel numbers are there below ten-thousand?
  - key point
      brute force
  - programming aspect
      flow of the excution
  - class
      programming
  - difficulty
      ★

- `Problem 62: Cubic permutations <gallery/Interesting-number-games/Problem-62.py>`_:

  - task
      Find the smallest cube for which exactly five permutations of its digits are cube.
  - key point
      Generate cubes, sort the digits to see if two cubes have the same composition
  - programming aspect
      *defaultdict* in *collections*, flow of the excution
  - class
      programming
  - difficulty
      ★★

- `Problem 63: Powerful digit counts <gallery/Interesting-number-games/Problem-63.py>`_:

  - task
      How many n-digit positive integers exist which are also an nth power?
  - key point
      10^(n-1) ≤ x^n < 10^n
  - programming aspect
      flow of the excution, mathematical operations
  - class
      mathematics
  - difficulty
      ★★

- `Problem 74: Digit factorial chains <gallery/Interesting-number-games/Problem-74.py>`_:

  - task
      According to the definition, how many factorial chains, with a starting number below one million,
      contain exactly sixty non-repeating terms?
  - key point
      brute fource, keep a cache *dict*
  - programming aspect
      *factorial* in *math*, *dict*, flow of the excution
  - class
      programming
  - difficulty
      ★★★

- `Problem 78: Coin partitions <gallery/Interesting-number-games/Problem-78.py>`_:

  - task
      Let p(n) represent the number of ways of partitioning n, find the least value of n for which p(n)
      is divisible by one million.
  - key point
      there's a recursive generating function for partition function
  - programming aspect
      generator, flow of the excution, mathematical operations
  - class
      mathematics
  - difficulty
      ★★★

- `Problem 88: Product-sum numbers <gallery/Interesting-number-games/Problem-88.py>`_:

  - task
      What is the sum of all the minimal product-sum numbers for 2≤k≤12000?
  - key point
      These two insights are critical for me to solve this problem: 1.Note that for any set of factors,
      we can always make it a valid product-sum by adding ones. 2.The upper bound of the minimal product-sum
      for k may be 2k.
  - programming aspect
      recursive function, *dict*, *set*
  - class
      programming
  - difficulty
      ★★★

- `Problem 92: Square digit chains <gallery/Interesting-number-games/Problem-92.py>`_:

  - task
      Investigate the square digit chains, and how many starting numbers below ten million will arrive
      at 89?
  - key point
      the order of the digits doesn't matter, keep a cache *dict*
  - programming aspect
      flow of the excution, list comprehension
  - class
      programming
  - difficulty
      ★★★

- `Problem 95: Amicable chains <gallery/Interesting-number-games/Problem-95.py>`_:

  - task
      Find the smallest member of the longest amicable chain with no element exceeding one million.
  - key point
      Prime Factorization, Sieve of Eratosthenes
  - programming aspect
      data structure selection, flow of the excution, interface design
  - class
      programming, mathematics
  - difficulty
      ★★★


Prime number related
--------------------
A prime number is a natural number greater than 1 that has no positive divisors other 1 and itself. Although
the simple definition, it occupies an important position in number theory, and the related theorems have become
the backbone of modern information security.

- `Problem 3: Largest prime factor <gallery/Prime-number-related/Problem-3.py>`_:

  - task
      What is the largest prime factor of the number 600851475143?
  - key point
      brute force, Fundamental Theorem of Arithmetic
  - programming aspect
      for loop, while loop, mathematical operations
  - class
      programming
  - difficulty
      ★★★

- `Problem 5: Smallest multiple <gallery/Prime-number-related/Problem-5.py>`_:

  - task
      What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
  - key point
      Sieve of Eratosthenes, Prime Factorization
  - programming aspect
      bool array, *dict*
  - class
      programming
  - difficulty
      ★★★

- `Problem 7: 10001st prime <gallery/Prime-number-related/Problem-7.py>`_:

  - task
      What is the 10 001st prime number?
  - key point
      brute force, trial division
  - programming aspect
      flow of the excution, *math*
  - class
      programming
  - difficulty
      ★

- `Problem 10: Summation of primes <gallery/Prime-number-related/Problem-10.py>`_:

  - task
      Find the sum of all the primes below two million.
  - key point
      Sieve of Eratosthenes
  - programming aspect
      bool array, for loop, long integer
  - class
      programming
  - difficulty
      ★★

- `Problem 27: Quadratic primes <gallery/Prime-number-related/Problem-27.py>`_:

  - task
      Find a quadratic formula producing the maximum number of primes for consecutive values of n,
      starting with n = 0.
  - key point
      brute force, Sieve of Eratosthenes
  - programming aspect
      bool array, *set*, flow of the excution
  - class
      programming
  - difficulty
      ★★

- `Problem 35: Circular primes <gallery/Prime-number-related/Problem-35.py>`_:

  - task
      According to the definition, how many circular primes are there below one million?
  - key point
      brute force, Sieve of Eratosthenes
  - programming aspect
      bool array, generator, *set*
  - class
      programming
  - difficulty
      ★★★

- `Problem 37: Truncatable primes <gallery/Prime-number-related/Problem-37.py>`_:

  - task
      Find the sum of the only eleven primes that are both truncatable from left to right and right
      to left.
  - key point
      brute force
  - programming aspect
      flow of the excution, dead code
  - class
      programming
  - difficulty
      ★★★

- `Problem 41: Pandigital prime <gallery/Prime-number-related/Problem-41.py>`_:

  - task
      What is the largest n-digit pandigital prime that exists?
  - key point
      Sieve of Eratosthenes, A number is divisible by 3 if the digit sum of the number is divisible
      by 3.
  - programming aspect
      bool array, *map*
  - class
      programming
  - difficulty
      ★★

- `Problem 46: Goldbach's other conjecture <gallery/Prime-number-related/Problem-46.py>`_:

  - task
      What is the smallest odd composite that cannot be written as the sum of a prime and twice a
      square?(与哥德巴赫的一个猜想有关)
  - key point
      brute force, Sieve of Eratosthenes
  - programming aspect
      bool array, *set*, flow of the excution
  - class
      programming
  - difficulty
      ★★★

- `Problem 47: Distinct primes factors <gallery/Prime-number-related/Problem-47.py>`_:

  - task
      Find the first four consecutive integers to have four distinct prime factors.
  - key point
      brute force, Sieve of Eratosthenes, Prime Factorization
  - programming aspect
      bool array, flow of the excution
  - class
      programming
  - difficulty
      ★★★

- `Problem 49: Prime permutations <gallery/Prime-number-related/Problem-49.py>`_:

  - task
      Find the defined arithmetic sequences, which are made of primes, and digits of each number
      are permutations of each other.
  - key point
      burte force, Sieve of Eratosthenes
  - programming aspect
      bool array, *set*, *list*, data structure selection
  - class
      programming
  - difficulty
      ★★★

- `Problem 50: Consecutive prime sum <gallery/Prime-number-related/Problem-50.py>`_:

  - task
      Which prime, below one-million, can be written as the sum of the most consecutive primes?
  - key point
      Sieve of Eratosthenes, cumulative sum
  - programming aspect
      numpy array, *set*, data structure selection
  - class
      programming
  - difficulty
      ★★★

- `Problem 51: Prime digit replacements <gallery/Prime-number-related/Problem-51.py>`_:

  - task
      Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits)
      with the same digit, is part of an eight prime value family.
  - key point
      Sieve of Eratosthenes, the repeating part must be 3 or multiple of 3, the repeating part cannot
      include the last digit, the repeating digit of the smallest prime must be 0, 1, or 2
  - programming aspect
      bool array, *set*, *itertools*, generator,string format operation
  - class
      programming, mathematics
  - difficulty
      ★★★★

- `Problem 58: Spiral primes <gallery/Prime-number-related/Problem-58.py>`_:

  - task
      Calculate the ratio of primes located on the diagonals of the spiral grid.
  - key point
      Sieve of Eratosthenes, trial division, Miller-Rabin primality test
  - programming aspect
      bool array, mathematical operations, *divmod*, interface design, refactoring
      time complexity
  - class
      programming, mathematics
  - difficulty
      ★★★★★

- `Problem 60: Prime pair sets <gallery/Prime-number-related/Problem-60.py>`_:

  - task
      Find the lowest sum for a set of five primes for which any two primes concatenate to produce
      another prime.
  - key point
      brute force, Sieve of Eratosthenes, Miller-Rabin primality test
  - programming aspect
      bool array, mathematical operations, *divmod*, interface design, refactoring, algorithm
      analysis, time and space complexity, data structure selection
  - class
      programming, mathematics
  - difficulty
      ★★★★★

- `Problem 87: Prime power triples <gallery/Prime-number-related/Problem-87.py>`_:

  - task
      How many numbers below fifty million can be expressed as the sum of a prime square, prime cube,
      and prime fourth power?
  - key point
      brute force, Sieve of Eratosthenes
  - programming aspect
      bool array, *set*, for loop
  - class
      programming
  - difficulty
      ★★

- `Problem 97: Large non-Mersenne prime <gallery/Prime-number-related/Problem-97.py>`_:

  - task
      Find the last ten digits of 28433×2^7830457+1.
  - key point
      Python is good for extremely big number calculation
  - programming aspect
      long integer
  - class
      programming
  - difficulty
      ★

Pythagorean triplet
-------------------
Pythagorean(毕达哥拉斯) triplet is one of the oldest achievements in the number theory. Project
Euler doesn't miss it.

- `Problem 9: Special Pythagorean triplet <gallery/Pythagorean-triplet/Problem-9.py>`_:

  - task
      There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.
  - key point
      Euclid's foluma, primitive solutions
  - programming aspect
      mathematical operations, flow of the excution
  - class
      mathematics
  - difficulty
      ★★★

- `Problem 39: Integer right triangles <gallery/Pythagorean-triplet/Problem-39.py>`_:

  - task
      If p is the perimeter of a right angle, for which value of p ≤ 1000, is the number of solutions
      maximised?
  - key point
      Euclid's foluma, primitive solutions
  - programming aspect
      mathematical operations, flow of the excution
  - class
      mathematics
  - difficulty
      ★★★

- `Problem 75: Singular integer right triangles <gallery/Pythagorean-triplet/Problem-75.py>`_:

  - task
      Given that L is the length of the wire, for how many values of L ≤ 1,500,000 can exactly one
      integer sided right angle triangle be formed?
  - key point
      Euclid's foluma, primitive solutions
  - programming aspect
      mathematical operations, flow of the excution
  - class
      mathematics
  - difficulty
      ★★★

- `Problem 86: Cuboid route <gallery/Pythagorean-triplet/Problem-86.py>`_:

  - task
      Find the shortest path from one corner of a cuboid to another.
  - key point
      Pythagorean triplet, for a cuboid with H ≤ W ≤ L,the shorest path S is given by sqrt(L^2+(W+H)^2)
      Binary search
  - programming aspect
      flow of the excution, mathematical operations, interface design
  - class
      mathematics, programming
  - difficulty
      ★★★★


Recursive definition
--------------------
In mathematics and computer science, recursion indicates such kind of definitions that contain a
reference to the thing being defined. For me, it's one of the most powerful but mysterious concept I
know.

- `Problem 2: Even Fibonacci numbers <gallery/Recursive-definition/Problem-2.py>`_:

  - task
      By considering the terms in the Fibonacci sequence whose values do not exceed four million, find
      the sum of the even-valued terms.
  - key point
      generator
  - programming aspect
      generator
  - class
      programming
  - difficulty
      ★

- `Problem 14: Longest Collatz sequence <gallery/Recursive-definition/Problem-14.py>`_:

  - task
      Which starting number, under one million, produces the longest Collatz sequence?
  - key point
      just follow the rule to generate the chain
  - programming aspect
      flow of the excution
  - class
      programming
  - difficulty
      ★★

- `Problem 25: 1000-digit Fibonacci number <gallery/Recursive-definition/Problem-25.py>`_:

  - task
      What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
  - key point
      generator
  - programming aspect
      generator
  - class
      programming
  - difficulty
      ★

- `Problem 28: Number spiral diagonals <gallery/Recursive-definition/Problem-28.py>`_:

  - task
      What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
  - key point
      f(0) = 1, f(n) = f(n-1) + 4*(2*n+1)^2 - 12*n, where n is the ring index
  - programming aspect
      generator
  - class
      mathematics, programming
  - difficulty
      ★★★

Totient function
----------------
In number theory, Euler's totient function counts the positive integers up to a given integer n that are
relatively prime to n. Although specific, nothing can cover its beauty.

- `Problem 69: Totient maximum <gallery/Totient-function/Problem-69.py>`_:

  - task
      If Euler's totient function is denoted as φ(n), find the value of n ≤ 1,000,000 for which
      n/φ(n) is a maximum.
  - key point
      Sieve of Eratosthenes, trial division
  - programming aspect
      bool array, mathematical operations, flow of the excution, interface design
  - class
      mathematics, programming
  - difficulty
      ★★★

- `Problem 70: Totient permutation <gallery/Totient-function/Problem-70.py>`_:

  - task
      If Euler's totient function is denoted as φ(n), find the value of n, 1 < n < 10^7, for which φ(n)
      is a permutation of n and the ratio n/φ(n) produces a minimum.
  - key point
      Since we need to minimize the n/φ(n), the prime factors of n should be large and the number of them
      should be as small as possible.
  - programming aspect
      interface design, numpy array
  - class
      mathematics, programming
  - difficulty
      ★★★

- `Problem 71: Ordered fractions <gallery/Totient-function/Problem-71.py>`_:

  - task
      By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending order of size, find the
      numerator of the fraction immediately to the left of 3/7.
  - key point
      Given max denominator, devise a general algorithm to search any fraction instead of 3/7. Denote this
      fraction as a/b, current denominator as q, numerator as p, then the largest p will be (a*q-1)//b, ...,
      lower q, and repeat the procedure
  - programming aspect
      mathematical operations, flow of the excution, algorithm design, interface design
  - class
      mathematics, programming
  - difficulty
      ★★★

- `Problem 72: Counting fractions <gallery/Totient-function/Problem-72.py>`_:

  - task
      How many elements would be contained in the set of reduced proper fractions for d ≤ 1,000,000?
  - key point
      Euler's totient function, modified Sieve of Eratosthenes
  - programming aspect
      algorithm design, mathematical operations
  - class
      mathematics, programming
  - difficulty
      ★★★★

- `Problem 73: Counting fractions in a range <gallery/Totient-function/Problem-73.py>`_:

  - task
      How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d ≤ 12,000?
  - key point
      Farey Sequence
  - programming aspect
      interface design, while loop
  - class
      mathematics
  - difficulty
      ★★★

Unclassified
------------
I can't find any uniform pattern shared by these problems, so I temporarily label them "Unclassified". Some
of them may be good materials for programming exercises yet.

- `Problem 1: Multiples of 3 and 5 <gallery/Unclassified/Problem-1.py>`_:

  - task
      Find the sum of all the multiples of 3 or 5 below 1000.
  - key point
      too simple
  - programming aspect
      for loop, update variables, unpack arguments, modulus operator
  - class
      programming
  - difficulty
      ★

- `Problem 6: Sum square difference <gallery/Unclassified/Problem-6.py>`_:

  - task
      Find the difference between the sum of the squares of the first one hundred natural numbers and the
      square of the sum.
  - key point
      folumas for sum of squares, and square of sum
  - programming aspect
      assignment, mathematical operaions
  - class
      mathematics
  - difficulty
      ★

- `Problem 8: Largest product in a series <gallery/Unclassified/Problem-8.py>`_:

  - task
      Find the thirteen adjacent digits in the given 1000-digit number that have the greatest product.
  - key point
      too simple
  - programming aspect
      string split, string concatenation, string slices and indices, *map*
  - class
      programming
  - difficulty
      ★

- `Problem 11: Largest product in a grid <gallery/Unclassified/Problem-11.py>`_:

  - task
      What is the greatest product of four adjacent numbers in the same direction (up, down, left, right,
      or diagonally) in given 20×20 grid?
  - key point
      straightforward
  - programming aspect
      numpy array, list comprehension, *map*
  - class
      programming
  - difficulty
      ★★

- `Problem 12: Highly divisible triangular number <gallery/Unclassified/Problem-12.py>`_:

  - task
      What is the value of the first triangle number to have over five hundred divisors?
  - key point
      brute force
  - programming aspect
      generator, mathematical operations, interface design
  - class
      programming
  - difficulty
      ★★

- `Problem 13: Large sum <gallery/Unclassified/Problem-13.py>`_:

  - task
      Work out the first ten digits of the sum of the given one-hundred 50-digit numbers.
  - key point
      trivial
  - programming aspect
      It's so easy that I only posted the problem statement in the script
  - class
      programming
  - difficulty
      ★

- `Problem 16: Power digit sum <gallery/Unclassified/Problem-16.py>`_:

  - task
      What is the sum of the digits of the number 2^1000?
  - key point
      trivial
  - programming aspect
      long integer
  - class
      programming
  - difficulty
      ★

- `Problem 17: Number letter counts <gallery/Unclassified/Problem-17.py>`_:

  - task
      If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many
      letters would be used?
  - key point
      treat it as an arithmetic problem
  - programming aspect
      assignment, *sum*
  - class
      mathematics
  - difficulty
      ★★

- `Problem 19: Counting Sundays <gallery/Unclassified/Problem-19.py>`_:

  - task
      How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec
      2000)?
  - key point
      *calendar* standard library
  - programming aspect
      for loop, function call
  - class
      programming
  - difficulty
      ★

- `Problem 20: Factorial digit sum <gallery/Unclassified/Problem-20.py>`_:

  - task
      Find the sum of the digits in the number 100!
  - key point
      *math* standard library
  - programming aspect
      It's so easy that I only posted the problem statement in the script
  - class
      programming
  - difficulty
      ★

- `Problem 22: Names scores <gallery/Unclassified/Problem-22/Problem-22.py>`_:

  - task
      According to the name score definition, what is the total of all the name scores in the file?
  - key point
      Quite straightforward
  - programming aspect
      *with* statement, *string* methods, *string* standard library, list comprehension, slices,
      iterator
  - class
      programming
  - difficulty
      ★★

- `Problem 40: Champernowne's constant <gallery/Unclassified/Problem-40.py>`_:

  - task
      Find the nth digit of the Champernowne's constant.
  - key point
      represent the number as a string
  - programming aspect
      string concatenation, interface design
  - class
      programming
  - difficulty
      ★★

- `Problem 48: Self powers <gallery/Unclassified/Problem-48.py>`_:

  - task
      Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
  - key point
      too simple
  - programming aspect
      It's so easy that I only posted the problem statement in the script
  - class
      programming
  - difficulty
      ★

- `Problem 56: Powerful digit sum <gallery/Unclassified/Problem-56.py>`_:

  - task
      Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?
  - key point
      no tricks
  - programming aspect
      number, sequence, *map*
  - class
      programming
  - difficulty
      ★

- `Problem 80: Square root digital expansion <gallery/Unclassified/Problem-80.py>`_:

  - task
      For the first one hundred natural numbers, find the total of the digital sums of the first one
      hundred decimal digits for all the irrational square roots.
  - key point
      *decimal* standard library
  - programming aspect
      context management, with statement
  - class
      programming
  - difficulty
      ★★

- `Problem 85: Counting rectangles <gallery/Unclassified/Problem-85.py>`_:

  - task
      Count the number of rectangles in a rectangular grid.
  - key point
      How many ways can we place two horizontal lines and two vertical lines? Combinatorics
  - programming aspect
      for loop
  - class
      mathematics
  - difficulty
      ★★

- `Problem 89: Roman numerals <gallery/Unclassified/Problem-89/Problem-89.py>`_:

  - task
      Try express Roman numerals in the minimal form.
  - key point
      a function converting Roman numerals to number, a function converting number into minimal Roman
      numerals
  - programming aspect
      for loop and while loop, interface design
  - class
      programming
  - difficulty
      ★★★

- `Problem 91: Right triangles with integer coordinates <gallery/Unclassified/Problem-91.py>`_:

  - task
      Count the number of right angle triangles with integer coordinates.
  - key point
      We can classify those right angle triangles into two cases: in the special case, the right angle
      is just on the axis, and in the regular case, the right angle lies in the first quadrant
  - programming aspect
      flow of the excution, mathematical operations
  - class
      mathematics, programming
  - difficulty
      ★★★★

- `Problem 98: Anagramic squares <gallery/Unclassified/Problem-98/Problem-98.py>`_:

  - task
      What is the largest square number formed by any anagramic pair of words given in the file？
  - key point
      Two-step brute force. First, find all anagramic word pairs in the file. Then, just check if both
      of them are squares. To speed up the square check, I precomputed all squares below some point and
      contained them in a *set*.
  - programming aspect
      data structure selection
  - class
      programming
  - dificulty
      ★★★

- `Problem 99: Largest exponential <gallery/Unclassified/Problem-99/Problem-99.py>`_:

  - task
      Which base/exponent pair in the file has the greatest numerical value?
  - key point
      logarithm
  - programming aspect
      with statement, *numpy*
  - class
      programming
  - difficulty
      ★

