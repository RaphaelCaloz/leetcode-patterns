# Useful functions for bit manipulation questions

# Integer to binary string:
# Use bin(my_int)
        

# Get number of 1 bits in positive integer:
def bit_len(int_type):
    length = 0
    while (int_type):
        int_type >>= 1
        length += 1
    return(length)

# Get bit at position
# (Starts at 0th position)
def get_ith_bit(num: int, i):
    return (num >> i) & 1

# Set bit at ith position
def set_bit(num: int, i):
    return num | (1<<i)

def clear_bit(num: int, i):
    return num & ~(1<<i)

'''
Relevant theory.

Bitwise operations that are just a boolean operator applied between corresponding bits of the operands follow laws analogous to the laws of Boolean algebra, for example:

AND (&) : Commutative, Associative, Identity (0xFF), Annihilator (0x00), Idempotent
OR  (|) : Commutative, Associative, Identity (0x00), Annihilator (0xFF), Idempotent
XOR (^) : Commutative, Associative, Identity (0x00), Inverse (itself)
NOT (~) : Inverse (itself)
AND and OR absorb each other:

a & (a | b) = a
a | (a & b) = a
There are some pairs of distributive operators, such as:

AND over OR: a & (b | c) = (a & b) | (a & c)
AND over XOR: a & (b ^ c) = (a & b) ^ (a & c)
OR over AND: a | (b & c) = (a | b) & (a | c)
Note however that XOR does not distribute over AND or OR, and neither does OR distribute over XOR.

DeMorgans law applies in its various forms:

~(a & b) = ~a | ~b
~(a | b) = ~a & ~b
Some laws that relate XOR and AND can be found by reasoning about the field ℤ/2ℤ, in which addition corresponds to XOR and multiplication to AND:

AND distributes over XOR
Working out products of sums: (a ^ b) & (c ^ d) = (a & c) ^ (a & d) ^ (b & c) ^ (b & d)
There are some laws that combine arithmetic and bitwise operations:

Subtract by adding: a - b = ~(~a + b)
Add carries separately: a + b = (a ^ b) + ((a & b) << 1)
Turn min into max and vice versa: min(a, b) = ~max(~a, ~b), max(a, b) = ~min(~a, ~b)
Shifts have no inverse because of the "destruction" of bits pushed to the edge

left shift  (<<) : Associative, Distributive, Identity (0x00)

right shift (>>) : Associative, Distributive, Identity (0x00)

rotate left  (rl) : Associative, Distributive, Identity (0x00), Inverse (rr)

rotate right (rr) : Associative, Distributive, Identity (0x00), Inverse (rl)

While shifts have no inverse, some expressions involving shifts do have inverses as consequence of other laws, for example:

x + (x << k) has an inverse, because it is effectively a multiplication by an odd number and odd numbers have an modular multiplicative inverse modulo a power of two. For x + (x << 1) = x * 3, the inverse is x * 0xAAAAAAAB (for 32 bits, adjust the constant for other sizes)
x ^ (x << k) has an inverse for a similar reason, but through the correspondence with carryless multiplication.
Similarly x ^ (x >> k) (with unsigned right shift) has an inverse, it's just the "mirror image" of the above.
'''