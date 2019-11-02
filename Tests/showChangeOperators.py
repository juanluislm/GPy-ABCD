from matplotlib import pyplot as plt
from Util.util import sampleCurves
from baseKernels import *


## Direct Sigmoidal effects on a given kernel

kBase = kSE

# # Ascending Sigmoid
# k_asc = kBase * SigmoidalKernel(1, True)
# k_asc.plot()
# print(k_asc)
# sampleCurves(k_asc)
#
# # Descending Sigmoid
# k_desc = kBase * SigmoidalKernel(1, False)
# k_desc.plot()
# print(k_desc)
# sampleCurves(k_desc)
#
# # Peak Sigmoid
# k_peak = kBase * SigmoidalIndicatorKernel(1, True)
# k_peak.plot()
# print(k_peak)
# sampleCurves(k_peak)
#
# # Hole Sigmoid
# k_hole = kBase * SigmoidalIndicatorKernel(1, False)
# k_hole.plot()
# print(k_hole)
# sampleCurves(k_hole)


plt.show()



## Change Operators

k_CP = kCP(kLIN, kPER)
k_CP.plot()
print(k_CP)
sampleCurves(k_CP)

k_CW = kCW(kLIN, kPER)
k_CW.plot()
print(k_CW)
sampleCurves(k_CW)


plt.show()
