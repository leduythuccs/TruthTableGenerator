# Truth Table Generator
This python code is auto generate truth table of  a Logical Epression (LE), such as (a v b) ^ (c v d). 

>(Vietnamese in [README-vi.md](README-vi.md))

# Supported Operations

My code supports 5 operators: 
- NOT: denoted as '!' or '-'. 
- AND: denoted as '^' or '.'.
- OR: denoted as 'v' or '+'.
- material implication: denoted as '->' or '>' .
- equivalence: denoted as '<->' or '~'.

**Order of operations**: NOT > AND = OR > material implication = equivalence
- The NOT operators will calculate first (highest priority)
- Then, The AND and OR operators.
- Last, The material implication and equivalence (lowest priority).
- It will calculate from left to right if 2 operators have the same order.

# How to use
Download [TruthTableGenerator.py](TruthTableGenerator.py) and run by command `python TruthTableGenerator.py`, then enter your logical epression, it will output a Truth Table of your LE.

You can use lower letter to represent variables, but don't use 'v' as variable, because it is an operator in my code. Therefore, you can use at most 25 variables.

# Example
My epression is: (p v (p ^ q)) ^ !p -> r
This is the generated truth table:
```
  p  |  q  |  r  |  (p v (p ^ q)) ^ !p -> r
  0  |  0  |  0  |  1
  0  |  0  |  1  |  1
  0  |  1  |  0  |  1
  0  |  1  |  1  |  1
  1  |  0  |  0  |  1
  1  |  0  |  1  |  1
  1  |  1  |  0  |  1
  1  |  1  |  1  |  1
```
