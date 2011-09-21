from neo.core.baseneo import BaseNeo

import numpy as np
import quantities as pq

class EventArray(BaseNeo):
    """
    Array of events. Introduced for performance reasons.
    An :class:`EventArray` is prefered to a list of :class:`Event` objects.
    
    *Usage*:
        TODO
    
    *Required attributes/properties*:
        :times: (quantity array 1D)
        :labels: (numpy.array 1D dtype='S')
    
    *Recommended attributes/properties*:
        :name:
        :description:
        :file_origin:            
    
    """
    def __init__(self, times = np.array([ ]) * pq.s , labels = np.array([ ] , dtype = 'S'), **kargs):
        BaseNeo.__init__(self, **kargs)
        self.times = times
        self.labels = labels

