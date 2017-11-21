import itertools
import sys

_py_major, _py_minor, _py_release, _py_level, _py_serial = sys.version_info


class Stream(object):
    '''
    classdocs
    TODO
    '''

    def __init__(self, itr):
        '''
        Constructor
        '''
        self._itr = iter(itr)

    def __iter__(self):
        return self._itr

    def __next__(self):
        return next(self._itr)

    def next(self):
        # Python 2
        return self.__next__()

    def map(self, func):
        """
            Create a new :class:`Stream` that is every value from this stream
            with a given function run over them.
            ::

                wrap(['cat', 'moose', 'bird']).map(len) #[3, 5, 4]

            :param func: The function to run
            :type func: callable
            :return: A stream of wrapped values
            :rtype: :class:`Stream`
        """
        if _py_major < 3:
            return wrap(itertools.imap(func, self._itr))
        else:
            return wrap(map(func, self._itr))

    def limit(self, length):
        return wrap(itertools.islice(self._itr, length))

    def filter(self, func):
        if _py_major < 3:
            return wrap(itertools.ifilter(func, self._itr))
        else:
            return wrap(filter(func, self._itr))

    def flatten(self):
        return wrap(itertools.chain.from_iterable(self._itr))

    def paginate(self, pageSize):
        """
            TODO
        """
        # Based on https://stackoverflow.com/a/46107096/686041
        def pager():
            page = []
            for i in self._itr:
                page.append(i)
                if len(page) == pageSize:
                    yield wrap(page)
                    page = []
            if page:
                yield wrap(page)

        return wrap(pager())

    def zip(self, *other):
        """
            Combine this stream with another Iterator so that it produces a new
            stream of tuples with a value from each stream, in order.
            ::

              wrap(['a', 'b', 'c']).zip([1,2,3]) #[('a', 1),('b', 2),('c', 3)]

            .. warning:: This method is a bit eager. It prematurely consumes
                some of the elements from the iterator

            :param other: One or more Iterator objects to zip with
            :type other: Iterator
            :return: The combined stream
            :rtype: :class:`Stream` of tuples
        """
        # should be  in 2.X
        if _py_major < 3:
            return wrap(itertools.izip(self._itr, *other))
        else:
            return wrap(zip(self._itr, *other))


def wrap(itr):
    return Stream(itr)
