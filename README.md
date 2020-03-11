<pre>
                                                              __
█▀▀ █▀▀▄ █▀▀█ █░█ █▀▀ █▀▀ █▀▀█ █▀▀█ █▀▀ █▀▀       _______    /*_>-<
▀▀█ █░░█ █▄▄█ █▀▄ █▀▀ ▀▀█ █░░█ █▄▄█ █░░ █▀▀   ___/ _____ \__/ /
▀▀▀ ▀░░▀ ▀░░▀ ▀░▀ ▀▀▀ ▀▀▀ █▀▀▀ ▀░░▀ ▀▀▀ ▀▀▀  <____/     \____/
</pre>

[![Actions Status](https://github.com/cmrfrd/SnakeSpace/workflows/pypi/badge.svg)](https://github.com/cmrfrd/SnakeSpace/actions) [![codecov](https://codecov.io/gh/cmrfrd/SnakeSpace/branch/master/graph/badge.svg)](https://codecov.io/gh/cmrfrd/SnakeSpace) [![PyPI version](https://badge.fury.io/py/snakespace.svg)](https://badge.fury.io/py/snakespace)

# SnakeSpace

`SnakeSpace` is a module for building label namespaces from [attribute chaining](https://en.wikipedia.org/wiki/Method_chaining) and args/kwargs

### Why

Creating a good label for a file or a key is [hard](https://xkcd.com/1459/). In Python, labels are either made via string concatenation or [format strings](https://www.python.org/dev/peps/pep-0498/). Now format strings are great! However they can get pretty specialized, you also have to include those pesky `f` and `{}` characters. Now there is a better and easier way with `SnakeSpace`!

With `SnakeSpace` you type just what you want as a chain of attributes! The expression `S.yo.hey.woohoo` is totally valid! Now labels can be created with ease! Or at least in a different style...

### Installing

This repo uses setup.py, so it follows the standard Python install routine

``` shell
pip install -U snakespace
```

Or if you want to install from source

``` shell
git clone https://github.com/cmrfrd/SnakeSpace.git
cd SnakeSpace
python3 setup.py install
```

### Examples and Behavior

With `SnakeSpace` you can create label namespaces from chaining attributes.

``` python
from snakespace import SnakeSpace
S = SnakeSpace()

print(S.super.duper.cool) # -> 'super.duper.cool'
```

You can also use the `s` function to supply custom arguments

``` python
from snakespace import SnakeSpace
S = SnakeSpace()

print(S.my.favorite.number.s(1301)) # -> 'my.favorite.number.1301'

print(S.yay.kwargs.s(1, 2, third=3)) # -> 'yay.kwargs.1.2.3'

print(S.shoop.s('da').whoop) # -> 'shoop.da.whoop'
```

If you don't like using periods as the default separator, you can change it using the *special* attribute `separator`

``` python
from snakespace import SnakeSpace
S = SnakeSpace()

print(S.a.b.c)    # -> 'a.b.c'
S.separator = '/'
print(S.a.b.c)    # -> 'a/b/c'
```

~Note!~ You can't chain attributes with `.separator`


### Namespacing

`SnakeSpace` behaves in between a `str`, and it's own custom object.

`SnakeSpace` will behave like a `str` when being operated on with another `str` ex: `S.a + 'woop' # -> 'awoop`. However `SnakeSpace` have slightly different behavior when being operated on by other `SnakeSpace`s to support common namespacing operations

`SnakeSpace` can be used for composing and comparing other `SnakeSpace`s.

You can see if a `SnakeSpace` is a subspace of another by using `in`

``` python
from snakespace import SnakeSpace
S = SnakeSpace()

print(S.a.b.c in S.a)           # -> True
print(S.potato in S.a)          # -> False
print(S.data.s(1,2) in S.data)  # -> True
```

`SnakeSpace`s can be compared, composed, and operated on

``` python
from snakespace import SnakeSpace
S = SnakeSpace()

# order (lexicographic)
print(S.one < S.one.two)           # -> True
print(S.a.b.c > S.a.b > S.a)       # -> True

# equality
print(S.a == S.a)                  # -> True

# addition
print(S.a + S.b)                   # -> 'a.b'

# size
print(len(S.apple.bannana.cherry)) # -> 3

# items
print(S.a.b.c[1])                  # -> 'b'

# superspace
print(S.a % S.a.b.c)               # -> True
print(S.a.b.c.d % S.a.b.c)         # -> False
```

`Snakespace` also comes with multiple common python `str` methods that are applied element wise in a `Snakespace` opposed to being operated on the whole resulting string.

### Limitations

`SnakeSpace` objects have some reserved attributes that cannot be used to building namespace labels.

    1. `separator` which is used to configure what string will be used to separate spaces
    2. Any [dunder methods/attributes](https://stackoverflow.com/questions/1418825/where-is-the-python-documentation-for-the-special-methods-init-new)

It's best just to avoid building anything with a start of a double underscore

### Fun examples

Easily make a bunch of keys for a `dict`

``` python
from random import randint
from snakespace import SnakeSpace
S = SnakeSpace()
D = {}

for i in range(10):
    D[S.data.s(i)] = randint(0,10)


```
