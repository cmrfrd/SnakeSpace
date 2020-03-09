``` text
  ____              _        ____
 / ___| _ __   __ _| | _____/ ___| _ __   __ _  ___ ___                    __
 \___ \| '_ \ / _` | |/ / _ \___ \| '_ \ / _` |/ __/ _ \       _______    /*_>-<
  ___) | | | | (_| |   <  __/___) | |_) | (_| | (_|  __/   ___/ _____ \__/ /
 |____/|_| |_|\__,_|_|\_\___|____/| .__/ \__,_|\___\___|  <____/     \____/
                                  |_|
```

# SnakeSpace

`SnakeSpace` is a module for building for composable namespace identifiers from [attribute chaining](https://en.wikipedia.org/wiki/Method_chaining) and args/kwargs

### Examples and Behavior

With `SnakeSpace` you can create namespace identifiers from chaining attributes.

``` text
from snakespace import SnakeSpace
S = SnakeSpace()

print(S.super.duper.cool) # -> 'super.duper.cool'
```

You can also use the `s` function to supply custom arguments to be added

``` text
from snakespace import SnakeSpace
S = SnakeSpace()

print(S.my.favorite.number.s(1301)) # -> 'my.favorite.number.1301'

print(S.yay.kwargs.s(1, 2, third=3)) # -> 'yay.kwargs.1.2.3'
```

If you don't like using periods as the default seperator, you can change it using the special attribute `seperator`

``` text
from snakespace import SnakeSpace
S = SnakeSpace()

print(S.a.b.c)    # -> 'a.b.c'
S.seperator = '/'
print(S.a.b.c)    # -> 'a/b/c'
```

### Namespacing

`SnakeSpace` will behave like a `str` when being operated on with a `str`. However `SnakeSpace` have slightly different behavior when being operated on by other `SnakeSpace`s to support common namespacing operations

`SnakeSpace` can also be used for composing and comparing other `SnakeSpace`s.

You can see if a `SnakeSpace` is a subspace of another by using `in`

``` text
from snakespace import SnakeSpace
S = SnakeSpace()

print(S.a.b.c in S.a)           # -> True
print(S.potato in S.a)          # -> False
print(S.data.s(1,2) in S.data)  # -> True
```

`SnakeSpace`s can be compared and composed

``` text
from snakespace import SnakeSpace
S = SnakeSpace()

print(S.one < S.one.two)      # -> True
print(S.a.b.c > S.a.b > S.a)  # -> True
print(S.a == S.a)             # -> True
print(S.a + S.b)              # -> 'a.b'
```

### Fun examples



### Limitations

*Special attributes:* SnakeSpace objects have some special attributes that cannot be used to build labels.

    1. `seperator` which is used to configure what string will be used to seperate spaces
    2. Any [dunder methods/attributes](https://stackoverflow.com/questions/1418825/where-is-the-python-documentation-for-the-special-methods-init-new)

It's best just to avoid building anything with a start of a double underscore
