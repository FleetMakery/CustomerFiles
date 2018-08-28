
hitpoints = 1

import sys
import time
if hitpoints <= 0:
    print("Your hero is dead")
    sys.exit(0)
else:
    print ('your hero will be healed')
    hitpoints = 0
    time.sleep(4)
    print("Your hero is dead")
    sys.exit(0)
