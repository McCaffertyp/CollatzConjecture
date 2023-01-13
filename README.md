# Collatz Conjecture Analysis
## by Paul McCafferty
### v4.4
Happening across a TikTok that explained the situation of Collatz Conjecture and it being unsolved,
Paul took an immediate liking to the mathematical problem and decided to check it out.

## Description
Collatz Conjecture is a graphing problem: [Link to Online Description](https://www.scirp.org/journal/paperinformation.aspx?paperid=109243#return4).
This problem analyzes a pattern based off only positive integers.
For odd, positive integers: 3 * x + 1 (Written as 3x + 1 for the docs), and for even, positive integers: x / 2.
The premise is that all graphs following this pattern eventually come back to 1.

## Preface
1) We will be using x and N as variables interchangeably for the most part. Some situations N is completely separate from x.
2) We will refer to the calculation for odd, positive integers as EQO, where EQO = 3 * x + 1.
3) We will refer to the calculation for even, positive integers as EQE, where EQE = x / 2.
4) We will refer to a positive, odd integer (N >= 1 && N % 2 == 1) as POI.
5) We will refer to a positive, even integer (N >= 2 && N % 2 == 0) as PEI.

## Questionable Theorems
A) We know that any odd number multiplied by an odd number will be odd ([Link of Proof](https://www.splashlearn.com/math-vocabulary/number-sense/even-and-odd-numbers)).<br />
B) We know that any even number divided by 2 may be either even or odd, as we are strictly working with integers.<br />
C) Based on (A), we know that anytime we get a POI, the result will be (B) (We _will_ do EQE).<br />
D) Based on (B), we know that anytime we get a PEI, the result may be either (A) or (B).<br />
E) If log<sub>2</sub>(n) is an integer, then n is a power of 2.<br />

### Loosely a Fundamental Statement from the Above
A fundamental statement that could be made, that would be that due to the "recursive waterfall" nature we can
observe above with conditions A-D, is the following:
"Should the number be odd, we are guaranteed to do an even calculation (which decreases the number's value).
Should the number be even, we are _not_ guaranteed to do an odd calculation (which increases the number's value)"

## Visual Tests (Sub-Point for 20-Group Theorem)
C1) Looking at the following even numbers:
2, 4, 6, 8, 10
if we divide 2 by 2, we get 1 (odd), 4 / 2 = 2 (even), 6 / 2 = 3 (odd), 8 / 2 = 4 (even), 10 / 2 = 5 (odd).

C2) Now let's add 10 to each:
12, 14, 16, 18, 20
if we divide 12 by 2, we get 6 (even), 14 / 2 = 7 (odd), 16 / 2 = 8 (even), 18 / 2 = 9 (odd), 20 / 2 = 10 (even).

C3) Now add another 10 to each:
22, 24, 26, 28, 30
if we divide 22 by 2, we get 11 (odd), 24 / 2 = 12 (even), 26 / 2 = 13 (odd), 28 / 2 = 14 (even), 30 / 2 = 15 (odd).

C4) What if we start dividing numbers that alternate every other for even/odd or all of one type?
286, 412, 518, 734, 804
if we divide 286 by 2, we get 143 (odd), 412 / 2 = 206 (even), 518 / 2 = 259 (odd), 734 / 2 = 367 (odd), 804 / 2 = 402 (even)

From the above, even just from the 2-20 with a step of (2), we can observe a perfect 50-50 split of getting a POI
or PEI when dividing by 2 (EQE). Furthering looking into this, that means that we're looking at a breakdown for every
20 numbers, not a massive integer.

For every 20 numbers, there are 10 odd numbers (1, 3, 5, 7, 9, 11, 13, 15, 17, 19) that will use EQO, and end up
resulting in an even number (refer to (A) above). There are 10 even numbers (2, 4, 6, 8, 10, 12, 14, 16, 18, 20) that
have a 50-50 for ending up an even or odd number (refer to (B) above).

Using the 20 number grouping, let's look at group (C4) from above: 286, 412, 518, 734, 804.
286 can be split into 200, 80 and 6. 200 is a 20 group, so we can ignore, 80 is a 20 group, so we can ignore, 6 / 2 = 3, which is odd.
412 can be split into 400 and 12. 400 is a 20 group, so we can ignore. 12 / 2 = 6, which is even.
518 can be split into 500 and 18. 500 is a 20 group, so we can ignore. 18 / 2 = 9, which is odd.
734 can be split into 700, 20, and 14. 700 is a 20 group, so we can ignore, 20 is a 20 group, so we can ignore, 14 / 2 = 7, which is odd.
804 can be split into 800 and 4. 800 is a 20 group, so we can ignore. 4 / 2 = 2, which is even.

To summarize, for every 20 numbers (20-group, which will be referred to as 20G), there is a 50% chance that we get
a POI, use the EQO and end up with an even number. With an even number, there is a 50% it will result in an even.
If it results in an odd, we use EQO, but then are guaranteed to use EQE next for another 50-50 of an odd or even.

## Thoughts
As an observable fact, we know that every POI will result in a PEI, which has a 50% (as in 1/2) of resulting in either
a POI or another PEI. So we have a base of two routes:
POI -> PEI -> 50/50 POI or PEI

Based on the above observable fact, there is a 100% chance a POI will lead to a PEI, which will have EQE done on it.
This means that every POI will only ever have roughly a 152% increase. Every PEI has a 50% (that is a 1/2) chance of
next resulting in either a POI or PEI, but decrements the current PEI by 50%. If it was a true 50-50 split, then we would
be getting an equal occurrence of both POI and PEI, as well as constantly be increasing, not approaching the constant
value of 1.

We know that certain PEI's, that is power's of 2, will always result in going to constant value of 1 (refer to P2F).
We will only ever encounter a P2F number for x when that number is either the starting value fed into Collatz Conjecture,
or we encounter an odd number that leads to it (refer to P4R).

## Observations
1) Since we know every POI will result in a PEI, which we will use EQE on, we can make the following statement:
All POI will have their two-step value result in the combination of EQO and EQE, thus EQO can have a sibling equation,
which will henceforth be EQOA = (3 * x + 1) / 2. EQE shall remain the same of EQE = x / 2

2) Since the current Collatz Conjecture always converges on 1, and that's gotten to by dividing by 2, we know
that the previous number before 1 was 2 since 2 / 2 = 1. We also know that 3 * 1 + 1 = 4, which is a PEI and would have
EQE performed on it. Due to this, we have the "4 Loop" which will be referred to as 4L. We can backtrack from
1 to 2 to 4 to etc... These are all powers of 2. Thus, we are now also brought to the conclusion that once a power
of 2 is hit in the equation process with EQO, we have met the condition to get into the 4L.
Let us call this the "Power of 2 Fall" which will be referred to as P2F.

3) Some odd numbers which lead to the P2F: 1, 5, 21, 85, 341, 1365, 5461, 21845, 87381, 349525, 1398101, 5592405<br />
For the directly above numbers which lead to a P2F, they're all the powers of 4 away from each other.
5 - 1 = 4, 21 - 5 = 16, 85 - 21 = 64, 341 - 85 = 256, etc.
Let us call this the "Power of 4 Rule" which will be referred to as P4R.

## Glossary
1) EQO = (3 * x + 1)
2) EQOA = ((3 * x + 1) / 2)
3) EQE = (x / 2)
4) POI = (N >= 1 && N % 2 == 1)
5) PEI = (N >= 2 && N % 2 == 0)
6) 20G = ((N >= 1 && N <= 20) && N % 2 == 0)
7) 4L = if (N == 4), we will end up in a 4, 2, 1, 4, 2, 1, etc. loop.
8) P2F = if (2^N), we will end up in 4L.
9) P4R = all odd numbers which lead to P2F will be some power of 4 away from another P4R number.

## Other
### Interesting Numbers to Run Through Program
1) 96667
2) 78360