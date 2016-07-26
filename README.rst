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
      Write a solver for 9×9 Su Doku
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

Prime number related
--------------------

Pythagorean triplet
-------------------

Recursive definition
--------------------

Totient function
----------------

Unclassified
------------
