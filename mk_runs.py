#! /usr/bin/env python
#

import os
import sys

from lmtoy import runs

project="2024-S1-MX-3"

#        obsnums per source (make it negative if not added to the final combination)
on = {}
on["IDF_SCUBA2_05"] = \
    [ 113240, 113241, 113242, 113244, 113245, 113246, 117245, 117246, 117247,
      117249, 117250, 117251, 117604, 117605, 117606, 117608, 117609, 117610,
      117612, 117613, 117614, 117618, 117619, 117620, 117622, 117623, 117624,
      117626, 117627, 117628, -117655, 117656, 117657, 117659, 117660, 117661,
      117663, 117664, 117665, -117899, 117900, 117901,
      119098, -119099, 119100, 119102, 119103, 119104, 119106, 119107, 119108,
      119111, 119112, 119113, 119117, 119118, 119119, 119121, 119122, 119123,
      119171, 119172, 119173, 119175, 119176, 119177, 119179, 119180, 119181,
      119183, 119184, 119185, 119421, 119422, 119423, 119425, 119426, 119427,
      119429, 119430, 119431, 119434, 119435, 119436, 
      127576, 127577, 127578, 127580, 127581, 127582, 127584, 127585, 127586,
      127765, 127766, 127767, 127769, 127770, 127771, 128059, 128060, 128459,
      128460, 128461, 128463, 128464, 128465, 128467, 128468, 128469]



#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
pars1["IDF_SCUBA2_05"] = ""


#        common parameters per source on subsequent runs (run1b, run2b), e.g. bank=0 for WARES
pars2 = {}
pars2["IDF_SCUBA2_05"] = ""


#        common parameters per source on subsequent runs (run1c, run2c), e.g. bank=1 for WARES
pars3 = {}
pars3["IDF_SCUBA2_05"] = ""


if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, pars3, sys.argv)
