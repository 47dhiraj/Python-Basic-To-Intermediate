#first way
'''
from package1 import module1, module2

module1.module1_func()
module2.module2_func()
'''
 
'''
#second way
import package1.module1, package1.module2 
package1.module1.module1_func()
package1.module2.module2_func()
'''


'''
#THIRD way ,,, exact module ma vayeko function import garxa
from package1.module1 import module1_func
from package1.module2 import module2_func

module1_func()
module2_func()
'''


#Fourth way,,, imprt * will only import those modules mentioned in init.py
from package1 import*

module1.module1_func()
module2.module2_func()






