import itertools

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
    
    def map(self, func):
        return wrap(map(func, self._itr))
    
    def limit(self, length):
        return wrap(itertools.islice(self._itr, length))
    
    def filter(self, func):
        return wrap(filter(func, self._itr))
    
    def flatten(self):
        return wrap(itertools.chain.from_iterable(self._itr))
    
    def paginate(self, pageSize):
        #Based on https://stackoverflow.com/a/46107096/686041
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
            stream of tuples with a value from each stream, in order.::
            
                wrap(['a', 'b', 'c']).zip([1,2,3]) #[('a', 1), ('b', 2), ('c', 3)]
            
            .. warning:: This method is a bit eager. It prematurely consumes some of the elements from the iterator
            
            :param other: One or more Iterator objects to zip with
            :type other: Iterator
        """
        #should be itertools.izip in 2.X
        return wrap(zip(self._itr, *other))

def wrap(itr):
    return Stream(itr)