import sys

import pkg1.pkg2.module1

print("pkg1.pkg2" in globals(), "pkg1.pkg2" in sys.modules)

pkg1.pkg2.module1.greet()