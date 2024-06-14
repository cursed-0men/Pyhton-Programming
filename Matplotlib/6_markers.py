'''
You can use the keyword argument marker 
to emphasize each point with a specified marker:
'''

import matplotlib.pyplot as plt
import numpy as np

y = np.array([3,8,1,10])
# x = 0,1,2,3

plt.plot(y,marker = 'o')
#plt.plot(y)
plt.show()


'''
Marker	Description

'o'	      Circle	
'*'	      Star	
'.'	      Point	
','	      Pixel	
'x'	      X	
'X'	      X (filled)	
'+'	      Plus	
'P'	      Plus (filled)	
's'	      Square	
'D'	      Diamond	
'd'	      Diamond (thin)	
'p'	      Pentagon	
'H'	      Hexagon	
'h'	      Hexagon	
'v'	      Triangle Down	
'^'	      Triangle Up	
'<'	      Triangle Left	
'>'	      Triangle Right	
'1'	      Tri Down	
'2'	      Tri Up	
'3'	      Tri Left	
'4'	      Tri Right	
'|'	      Vline	
'_'	      Hline

'''