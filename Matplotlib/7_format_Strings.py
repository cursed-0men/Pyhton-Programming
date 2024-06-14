# Format Strings 

# Line Reference
'''

Line Syntax	      Description

'-'	            Solid line	
':'	            Dotted line	
'--'	            Dashed line	
'-.'	            Dashed/dotted line

'''


# Color Reference
'''
Color Syntax	Description

'r'	            Red	
'g'	            Green	
'b'	            Blue	
'c'	            Cyan	
'm'	            Magenta	
'y'	            Yellow	
'k'	            Black	
'w'	            White



'''


# NOTE : Format syntax : marker|line|color

import numpy as np
import matplotlib.pyplot as plt

y = np.array([3,8,1,10])

plt.plot(y,'o--m')
plt.show()
