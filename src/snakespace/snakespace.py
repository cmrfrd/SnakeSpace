import sys
import _collections_abc
from functools import wraps

class SnakeSpace(_collections_abc.Sequence):
    """
    SnakeSpace is a class that constructs strings from attributes, args, and kwargs

    SnakeSpaces can also be operated on with other SnakeSpaces like namespaces
    """
    
    def __init__(self, seq=[], seperator='.'):
        """Initialize a SnakeSpace object
        """
        self.___data = [] + seq
        self.__seperator = seperator

    @property
    def seperator(self):
        """seperator is the value between each piece of data
        """
        return self.__seperator
    
    @seperator.setter
    def seperator(self, val):
        """set the value for the seperator
        """
        self.__seperator = val
    
    @property
    def __data(self):
        """Accessing the data joins it as a string
        """
        return self.__seperator.join(self.___data)
        
    def __getattr__(self, attr):
        """Getting an attribute creates a new copy of SnakeSpace adding the attribute
        """
        return SnakeSpace(self.___data + [attr], self.__seperator)
        
    def s(self, *args, **kwargs):
        """Create a new SnakeSpace adding the string representation of args/kwargs
        """
        result_str = list(args) + list(kwargs.values())
        if len(result_str):
            return SnakeSpace(self.___data + [self.__seperator.join(map(str, result_str))], self.__seperator)
        return SnakeSpace(self.___data, self.__seperator)
    
    def __str__(self):
        """Return the string representation of the data
        """
        return str(self.__data)

    def __repr__(self):
        """Return the representation of the data
        """
        return repr(self.__data)

    def __int__(self):
        """Return the int representation of the data
        """
        return int(self.__data)

    def __float__(self):
        """Return the float representation of the data
        """
        return float(self.__data)

    def __complex__(self):
        """Return the complex representation of the data
        """
        return complex(self.__data)

    def __hash__(self):
        """Return the hash representation of the data
        """
        return hash(self.__data)
    
    def __getnewargs__(self):
        return (self.__data[:],)

    def __eq__(self, string):
        """Equate SnakeSpace data or the string
        """
        if isinstance(string, SnakeSpace):
            return self.__data == string.__data
        return self.__data == string

    def __ne__(self, string):
        """Opposite of eq
        """
        return not (self.__data == string)
    
    def __lt__(self, string):
        """Compare SnakeSpace data or string
        """
        if isinstance(string, SnakeSpace):
            return self.__data < string.__data
        return self.__data < string
    
    def __le__(self, string):
        """Compare SnakeSpace data or string
        """
        if isinstance(string, SnakeSpace):
            return self.__data <= string.__data
        return self.__data <= string
    
    def __gt__(self, string):
        """Compare SnakeSpace data or string
        """
        if isinstance(string, SnakeSpace):
            return self.__data > string.__data
        return self.__data > string
    
    def __ge__(self, string):
        """Compare SnakeSpace data or string
        """
        if isinstance(string, SnakeSpace):
            return self.__data >= string.__data
        return self.__data >= string
    
    def __contains__(self, char):
        """Compare SnakeSpace data or string
        """
        if isinstance(char, SnakeSpace):
            return self.___data == char.___data[:len(self.___data)]
        return char in self.__data

    def __len__(self):
        """Get the length not of the string, but of the underlying data
        """
        return len(self.___data)
    
    def __getitem__(self, index):
        """Get the item not of the string but the underlying data
        """
        return self.___data[index]
    
    def __add__(self, other):
        """Add SnakeSpace data together, otherwise string concat
        """
        if isinstance(other, SnakeSpace):
            return SnakeSpace(self.___data + other.___data, self.__seperator)
        return self.__data + str(other)

    def __radd__(self, other):
        if isinstance(other, SnakeSpace):
            return SnakeSpace(other.___data + self.___data, self.__seperator)
        return str(other) + self.__data

    def __mul__(self, n):
        return self.__class__(self.__data*n)
    __rmul__ = __mul__

    def __mod__(self, args):
        return self.__data.startswith(str(args))

    def __rmod__(self, template):
        return str(template) % self
    
    # the following methods are defined in alphabetical order:
    def capitalize(self):
        return self.__class__(self.__data.capitalize())

    def casefold(self):
        return self.__class__(self.__data.casefold())

    def center(self, width, *args):
        return self.__class__(self.__data.center(width, *args))

    def count(self, sub, start=0, end=sys.maxsize):
        if isinstance(sub, SnakeSpace):
            sub = sub.__data
        return self.__data.count(sub, start, end)

    def encode(self, encoding='utf-8', errors='strict'):
        encoding = 'utf-8' if encoding is None else encoding
        errors = 'strict' if errors is None else errors
        return self.__data.encode(encoding, errors)

    def endswith(self, suffix, start=0, end=sys.maxsize):
        return self.__data.endswith(suffix, start, end)

    def expandtabs(self, tabsize=8):
        return self.__class__(self.__data.expandtabs(tabsize))

    def find(self, sub, start=0, end=sys.maxsize):
        if isinstance(sub, SnakeSpace):
            sub = sub.__data
        return self.__data.find(sub, start, end)

    def format(self, /, *args, **kwds):
        return self.__data.format(*args, **kwds)

    def format_map(self, mapping):
        return self.__data.format_map(mapping)

    def index(self, sub, start=0, end=sys.maxsize):
        return self.__data.index(sub, start, end)

    def isalpha(self): return self.__data.isalpha()

    def isalnum(self): return self.__data.isalnum()

    def isascii(self): return self.__data.isascii()

    def isdecimal(self): return self.__data.isdecimal()

    def isdigit(self): return self.__data.isdigit()

    def isidentifier(self): return self.__data.isidentifier()

    def islower(self): return self.__data.islower()

    def isnumeric(self): return self.__data.isnumeric()

    def isprintable(self): return self.__data.isprintable()

    def isspace(self): return self.__data.isspace()

    def istitle(self): return self.__data.istitle()

    def isupper(self): return self.__data.isupper()

    def join(self, seq): return self.__data.join(seq)

    def ljust(self, width, *args):
        return self.__class__(self.__data.ljust(width, *args))

    def lower(self): return self.__class__(self.__data.lower())

    def lstrip(self, chars=None): return self.__class__(self.__data.lstrip(chars))

    maketrans = str.maketrans

    def partition(self, sep):
        return self.__data.partition(sep)

    def replace(self, old, new, maxsplit=-1):
        if isinstance(old, SnakeSpace):
            old = old.__data
        if isinstance(new, SnakeSpace):
            new = new.__data
        return self.__class__(self.__data.replace(old, new, maxsplit))

    def rfind(self, sub, start=0, end=sys.maxsize):
        if isinstance(sub, SnakeSpace):
            sub = sub.__data
        return self.__data.rfind(sub, start, end)

    def rindex(self, sub, start=0, end=sys.maxsize):
        return self.__data.rindex(sub, start, end)

    def rjust(self, width, *args):
        return self.__class__(self.__data.rjust(width, *args))

    def rpartition(self, sep):
        return self.__data.rpartition(sep)

    def rstrip(self, chars=None):
        return self.__class__(self.__data.rstrip(chars))

    def split(self, sep=None, maxsplit=-1):
        return self.__data.split(sep, maxsplit)

    def rsplit(self, sep=None, maxsplit=-1):
        return self.__data.rsplit(sep, maxsplit)
    def splitlines(self, keepends=False): return self.__data.splitlines(keepends)
    

    def startswith(self, prefix, start=0, end=sys.maxsize):
        return self.__data.startswith(prefix, start, end)

    def strip(self, chars=None): return self.__class__(self.__data.strip(chars))

    def swapcase(self): return self.__class__(self.__data.swapcase())

    def title(self): return self.__class__(self.__data.title())

    def translate(self, *args):
        return self.__class__(self.__data.translate(*args))

    def upper(self): return self.__class__(self.__data.upper())

    def zfill(self, width): return self.__class__(self.__data.zfill(width))
