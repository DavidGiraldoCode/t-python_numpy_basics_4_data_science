# Python

## How data behaves in python:
- Variables in Python are dynamically inferred.
- Variables store more data than just their values.

## Why is so dynamic?
Python under the hood is written in C.

Python int<br>
`x = 1`

#C int representing the Python int <br>
    `struct _longobject {
        long ob_refcnt; ??
        PyTypeObject *ob_type;
        size_t ob_size;
        long ob_digit[1];
    };`

Int in C is a position in memory whose bytes represent an integer

Any Int i Python is a pointer to a position in memory with the Python Objetc information, including the bytes that represent the interger.

### To consider:

| Data type   |      Description      |
|-------------|---------------------|
|bool_	    |Boolean (True or False) stored as a byte
|int_	    |Default integer type (same as C long; normally either int64 or int32)
|intc	    |Identical to C int (normally int32 or int64)
|intp	    |Integer used for indexing (same as C ssize_t; normally either int32 or int64)
|int8	    |Byte (-128 to 127)
|int16	    |Integer (-32768 to 32767)
|int32	    |Integer (-2147483648 to 2147483647)
|int64	    |Integer (-9223372036854775808 to 9223372036854775807)
|uint8	    |Unsigned integer (0 to 255)
|uint16	    |Unsigned integer (0 to 65535)
|uint32	    |Unsigned integer (0 to 4294967295)
|uint64	    |Unsigned integer (0 to 18446744073709551615)
|float_	    |Shorthand for float64.
|float16	|Half precision float: sign bit, 5 bits exponent, 10 bits mantissa
|float32	|Single precision float: sign bit, 8 bits exponent, 23 bits mantissa
|float64	|Double precision float: sign bit, 11 bits exponent, 52 bits mantissa
|complex_	|Shorthand for complex128.
|complex64	|Complex number, represented by two 32-bit floats
|complex128	|Complex number, represented by two 64-bit floats
