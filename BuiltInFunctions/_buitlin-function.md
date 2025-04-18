# Python Built-in Functions (v3.13.3)

This document lists all 69 built-in functions in Python 3.13.3, categorized by their primary use cases.

# Table of Contents

- [Python Built-in Functions (v3.13.3)](#python-built-in-functions-v3133)
  - [Type Conversion / Casting](#type-conversion--casting)
    - [bool()](#bool)
    - [bytearray()](#bytearray)
    - [bytes()](#bytes)
    - [complex()](#complex)
    - [dict()](#dict)
    - [float()](#float)
    - [frozenset()](#frozenset)
    - [int()](#int)
    - [list()](#list)
    - [set()](#set)
    - [str()](#str)
    - [tuple()](#tuple)
    - [memoryview()](#memoryview)
  - [Input & Output](#input--output)
    - [input()](#input)
    - [open()](#open)
    - [print()](#print)
  - [Mathematical Operations](#mathematical-operations)
    - [abs()](#abs)
    - [divmod()](#divmod)
    - [max()](#max)
    - [min()](#min)
    - [pow()](#pow)
    - [round()](#round)
    - [sum()](#sum)
  - [Iterables & Iterations](#iterables--iterations)
    - [all()](#all)
    - [any()](#any)
    - [enumerate()](#enumerate)
    - [filter()](#filter)
    - [iter()](#iter)
    - [len()](#len)
    - [map()](#map)
    - [next()](#next)
    - [range()](#range)
    - [reversed()](#reversed)
    - [slice()](#slice)
    - [sorted()](#sorted)
    - [zip()](#zip)
  - [Object Introspection](#object-introspection)
    - [callable()](#callable)
    - [dir()](#dir)
    - [getattr()](#getattr)
    - [hasattr()](#hasattr)
    - [id()](#id)
    - [isinstance()](#isinstance)
    - [issubclass()](#issubclass)
    - [type()](#type)
    - [vars()](#vars)
  - [String Operations](#string-operations)
    - [ascii()](#ascii)
    - [bin()](#bin)
    - [chr()](#chr)
    - [format()](#format)
    - [hex()](#hex)
    - [oct()](#oct)
    - [ord()](#ord)
    - [repr()](#repr)
  - [Functional Programming](#functional-programming)
    - [eval()](#eval)
    - [exec()](#exec)
  - [Debugging and Development](#debugging-and-development)
    - [breakpoint()](#breakpoint)
    - [compile()](#compile)
    - [help()](#help)
  - [Memory & Scope](#memory--scope)
    - [globals()](#globals)
    - [hash()](#hash)
    - [locals()](#locals)
  - [Class & Object Management](#class--object-management)
    - [classmethod()](#classmethod)
    - [delattr()](#delattr)
    - [object()](#object)
    - [property()](#property)
    - [setattr()](#setattr)
    - [staticmethod()](#staticmethod)
    - [super()](#super)
  - [Miscellaneous](#miscellaneous)
    - [\_\_import\_\_()](#__import__)


## Type Conversion / Casting

### bool()
```python
bool([x])
```
Returns a Boolean value, either `True` or `False`. If `x` is false or omitted, this returns `False`; otherwise, it returns `True`.

### bytearray()
```python
bytearray([source[, encoding[, errors]]])
```
Returns a new array of bytes. The `bytearray` class is a mutable sequence of integers in the range 0 <= x < 256.

### bytes()
```python
bytes([source[, encoding[, errors]]])
```
Returns a new "bytes" object, which is an immutable sequence of integers in the range 0 <= x < 256.

### complex()
```python
complex([real[, imag]])
```
Creates a complex number with the value `real + imag*1j` or converts a string or number to a complex number.

### dict()
```python
dict(**kwarg)
dict(mapping, **kwarg)
dict(iterable, **kwarg)
```
Creates a new dictionary. The `dict` object is the dictionary class.

### float()
```python
float([x])
```
Converts a string or number to a floating point number.

### frozenset()
```python
frozenset([iterable])
```
Returns a new frozenset object, optionally with elements taken from iterable.

### int()
```python
int([x[, base=10]])
```
Converts a number or string to an integer, or returns 0 if no arguments are given.

### list()
```python
list([iterable])
```
Returns a list whose items are the same and in the same order as iterable's items.

### set()
```python
set([iterable])
```
Returns a new set object, optionally with elements taken from iterable.

### str()
```python
str(object='')
str(object=b'', encoding='utf-8', errors='strict')
```
Returns a string version of object.

### tuple()
```python
tuple([iterable])
```
Returns a tuple whose items are the same and in the same order as iterable's items.

### memoryview()
```python
memoryview(obj)
```
Returns a "memory view" object created from the given argument.

## Input & Output

### input()
```python
input([prompt])
```
Reads a line from input, converts it to a string (stripping a trailing newline), and returns that.

### open()
```python
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
```
Opens file and returns a corresponding file object.

### print()
```python
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
```
Prints objects to the text stream file, separated by sep and followed by end.

## Mathematical Operations

### abs()
```python
abs(x)
```
Returns the absolute value of a number. The argument may be an integer, a floating point number, or an object implementing `__abs__()`.

### divmod()
```python
divmod(a, b)
```
Returns a tuple of the quotient and remainder when dividing `a` by `b`.

### max()
```python
max(iterable, *[, key, default])
max(arg1, arg2, *args[, key])
```
Returns the largest item in an iterable or the largest of two or more arguments.

### min()
```python
min(iterable, *[, key, default])
min(arg1, arg2, *args[, key])
```
Returns the smallest item in an iterable or the smallest of two or more arguments.

### pow()
```python
pow(base, exp[, mod])
```
Returns base to the power exp; if mod is present, returns base to the power exp, modulo mod.

### round()
```python
round(number[, ndigits])
```
Returns number rounded to ndigits precision after the decimal point.

### sum()
```python
sum(iterable, /, start=0)
```
Sums start and the items of an iterable from left to right and returns the total.

## Iterables & Iterations

### all()
```python
all(iterable)
```
Returns `True` if all elements of the iterable are true (or if the iterable is empty).

### any()
```python
any(iterable)
```
Returns `True` if any element of the iterable is true. If the iterable is empty, returns `False`.

### enumerate()
```python
enumerate(iterable, start=0)
```
Returns an enumerate object. Iterable must be a sequence, an iterator, or some other object which supports iteration.

### filter()
```python
filter(function, iterable)
```
Constructs an iterator from elements of iterable for which function returns true.

### iter()
```python
iter(object[, sentinel])
```
Returns an iterator object.

### len()
```python
len(s)
```
Returns the length (the number of items) of an object.

### map()
```python
map(function, iterable, ...)
```
Returns an iterator that applies function to every item of iterable, yielding the results.

### next()
```python
next(iterator[, default])
```
Retrieves the next item from the iterator. If default is given, it is returned if the iterator is exhausted.

### range()
```python
range(stop)
range(start, stop[, step])
```
Returns an immutable sequence of numbers in the specified range.

### reversed()
```python
reversed(seq)
```
Returns a reverse iterator over the values of the given sequence.

### slice()
```python
slice(stop)
slice(start, stop[, step])
```
Returns a slice object representing the set of indices specified by range(start, stop, step).

### sorted()
```python
sorted(iterable, *, key=None, reverse=False)
```
Returns a new sorted list from the items in iterable.

### zip()
```python
zip(*iterables)
```
Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables.

## Object Introspection

### callable()
```python
callable(object)
```
Returns `True` if the object argument appears callable, `False` if not.

### dir()
```python
dir([object])
```
Without arguments, returns the list of names in the current local scope. With an argument, returns an alphabetized list of names comprising (some of) the object's attributes.

### getattr()
```python
getattr(object, name[, default])
```
Returns the value of the named attribute of object. name must be a string.

### hasattr()
```python
hasattr(object, name)
```
Returns `True` if the object has the named attribute, `False` if not. name must be a string.

### id()
```python
id(object)
```
Returns the "identity" of an object. This is an integer which is guaranteed to be unique and constant for this object during its lifetime.

### isinstance()
```python
isinstance(object, classinfo)
```
Returns `True` if the object argument is an instance of the classinfo argument.

### issubclass()
```python
issubclass(class, classinfo)
```
Returns `True` if class is a subclass (direct, indirect, or virtual) of classinfo.

### type()
```python
type(object)
type(name, bases, dict)
```
With one argument, returns the type of an object. With three arguments, returns a new type object.

### vars()
```python
vars([object])
```
Returns the __dict__ attribute for a module, class, instance, or any other object with a __dict__ attribute.

## String Operations

### ascii()
```python
ascii(object)
```
Returns a string containing a printable representation of an object, with non-ASCII characters escaped.

### bin()
```python
bin(x)
```
Converts an integer to a binary string prefixed with "0b".

### chr()
```python
chr(i)
```
Returns the string representing a character whose Unicode code point is the integer `i`.

### format()
```python
format(value[, format_spec])
```
Converts a value to a "formatted" representation, as controlled by format_spec.

### hex()
```python
hex(x)
```
Converts an integer to a hexadecimal string prefixed with "0x".

### oct()
```python
oct(x)
```
Converts an integer to an octal string prefixed with "0o".

### ord()
```python
ord(c)
```
Returns an integer representing the Unicode code point for the given Unicode character.

### repr()
```python
repr(object)
```
Returns a string containing a printable representation of an object.

## Functional Programming

### eval()
```python
eval(expression[, globals[, locals]])
```
Evaluates the given expression in the context of globals and locals and returns the result.

### exec()
```python
exec(object[, globals[, locals]])
```
Executes the given source in the context of globals and locals, source can be a string or a code object.

## Debugging and Development

### breakpoint()
```python
breakpoint(*args, **kws)
```
Drops you into the debugger at the call site. Specifically, it calls `sys.breakpointhook()`.

### compile()
```python
compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)
```
Compiles the source into a code or AST object. Code objects can be executed by exec() or eval().

### help()
```python
help([object])
```
Invokes the built-in help system. If no argument is given, the interactive help system starts on the interpreter console.

## Memory & Scope

### globals()
```python
globals()
```
Returns a dictionary representing the current global symbol table.

### hash()
```python
hash(object)
```
Returns the hash value of the object (if it has one). Hash values are integers.

### locals()
```python
locals()
```
Returns a dictionary representing the current local symbol table.

## Class & Object Management

### classmethod()
```python
classmethod(function)
```
Returns a class method for the given function.

### delattr()
```python
delattr(object, name)
```
Deletes the named attribute from the object, equivalent to `del object.name`.

### object()
```python
object()
```
Returns a new featureless object. Object is a base for all classes.

### property()
```python
property(fget=None, fset=None, fdel=None, doc=None)
```
Returns a property attribute for new-style classes.

### setattr()
```python
setattr(object, name, value)
```
Sets the named attribute on the given object to the specified value.

### staticmethod()
```python
staticmethod(function)
```
Returns a static method for function.

### super()
```python
super([type[, object-or-type]])
```
Returns a proxy object that delegates method calls to a parent or sibling class.

## Miscellaneous

### __import__()
```python
__import__(name, globals=None, locals=None, fromlist=(), level=0)
```
This function is invoked by the import statement. It's primarily used in the implementation of import and should generally not be used directly.
