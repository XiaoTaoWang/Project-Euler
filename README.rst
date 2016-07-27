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
I heard about Project Euler completely by accident. I was fascinated by the beauty features of
amicable numbers, and there happened to be a related problem(`Problem 21 <https://projecteuler.net/problem=21>`_)
distributed by Project Euler. However, what I have learned is far beyond what I expected.
A new world is open for me, a world of mathematics and algorithm, full of unknowns and miracles.
It's so attractive that I can't stop myself exporing it.

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
prerequisite to Probability, Graph Theory, etc. Project Euler do include several problems in this
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
  - programming
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
  - programming
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
  - programming
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
  - programming
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
  - programming
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
  - programming
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
  - programming
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
  - programming
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
  - programming
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
  - programming
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
  - programming
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
  - programming
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
  - programming
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
  - programming
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
  - programming
      flow of the excution
  - class
      mathematics
  - difficulty
      ★★★★


Games
-----
Games excite us, and computing make us crazy!

- `Problem 54: Poker hands <gallery/Games/Problem-54/Problem-54.py>`_:

  - task
      Game poker: how many hands does Player 1 win?
  - key point
      The rules are clear, just simulate the game.
  - programming
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
  - programming
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
  - programming
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
  - programming
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
  - programming
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
  - programming
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
  - programming
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
  - programming
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
  - programming
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
  - programming
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
  - programming
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
  - programming
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
  - programming
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
  - programming
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
  - programming
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
  - programming
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
  - programming
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
  - programming
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
  - programming
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
  - programming
      generator, flow of the excution, mathematical operations
  - class
      mathematics
  - difficulty
      ★★★

- `Problem 92: Square digit chains <gallery/Interesting-number-games/Problem-92.py>`_:

  - task
      Investigate the square digit chains, and how many starting numbers below ten million will arrive
      at 89?
  - key point
      the order of the digits doesn't matter, keep a cache *dict*
  - programming
      flow of the excution, list comprehension
  - class
      programming
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
  - programming
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
  - programming
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
  - programming
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
  - programming
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
  - programming
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
  - programming
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
  - programming
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
  - programming
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
  - programming
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
  - programming
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
  - programming
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
  - programming
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
  - programming
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
  - programming
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
  - programming
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
  - programming
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
  - programming
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
  - programming
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
  - programming
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
  - programming
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
  - programming
      flow of the excution, mathematical operations, interface design
  - class
      mathematics, programming
  - difficulty
      ★★★★


Recursive definition
--------------------

Totient function
----------------

Unclassified
------------
