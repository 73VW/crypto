Homework 4 Maël Pedretti
--------------------------

Exercise 1
==========

**p = 71**

**g = 7**

a)
  **a = 5**

  A = g^a mod p = 7^5 mod 71 = 51 (using modular exponent)

b)
  **b = 12**

  B = g^b mod p = 7^12 mod 71 = 4

c)
  Compute S:

  S = B^a mod p = 4^5 mod 71 = 30

  S = A^b mod p = 51^12 mod 71 = 30

Exercise 2
==========

**p = 23**

**g = 5**

a)
  **a = 6**

  A = g^a mod p = 5^6 mod 23 = 8

b)
  **b = 15**

  B = g^b mod p = 5^15 mod 23 = 19

c)
  Compute S:

  B^a mod p = 19^6 mod 23 = 2

  A^b mod p = 8^15 mod 23 = 2

Exercise 3
==========

**p = 11**

**g = 2**

a)
 - 2^0 mod 11 = 1
 - 2^1 mod 11 = 2
 - 2^2 mod 11 = 4
 - 2^3 mod 11 = 8
 - 2^4 mod 11 = 5
 - 2^5 mod 11 = 10
 - 2^6 mod 11 = 9
 - 2^7 mod 11 = 7
 - 2^8 mod 11 = 3
 - 2^9 mod 11 = 6

 -> all numbers from 0 to p-1 are present

b)
  A = g^a mod p = 2^a mod 11 = 9

  Find in list above which one is right.

  We find that 2^6 mod 11 = 9

  -> a = 6

c)
  B = 3

  S = B^a mod p = 3^6 mod 11 = 3

  S = A^b mod p = 9^8 mod 11 = 3

Exercise 4
==========

**p = 11**

**g = 3**

- 3^1 mod 11  = 3
- 3^2 mod 11  = 9
- 3^3 mod 11  = 5
- 3^4 mod 11  = 4
- 3^5 mod 11  = 1
- 3^6 mod 11  = 3
- 3^7 mod 11  = 9
- 3^8 mod 11  = 5
- 3^9 mod 11  = 4
- 3^10 mod 11  = 1
- 3^11 mod 11  = 3

  -> not all numbers from 0 to p-1 are present

  -> there are two values for e that match g^e mod p = 5

  -> 3 is not a primitive root of 11

Exercise 5
==========

two pairs:

    Someone in the middle intercepts g^a and g^b and sends g^a' and g^b' after generating two new pairs (one for each part)
    He now communicates with g^ab' and g^a'b. Both original believe they talk together but they in fact communicate with the man in the middle.

one pair:

    Let's take the example from exercise 1.

    **p = 71**

    **g = 7**

    **a = 5**

    **A = 51**

    **b = 12**

    **B = 4**

    Man in the middle new pair:

    a' = 7

    A' = g^a' mod p = 7^7 mod 71 = 14

    exchange with a:

    S = A'^a mod p = 14^5 mod 71 = 70

    S = A^a' mod p = 51^7 mod 71 = 70

    exchange with b:

    S = A'^b mod p = 14^12 mod 71 = 54

    S = B^a' mod p = 4^7 mod 71 = 54

    **-> Apparently it should also work with one pair.**
