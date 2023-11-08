import sys
import management
import checker



if sys.argv[1] == "management":
    management.main()
elif sys.argv[1] == "check":
    checker.main()
else:
    print("verkeerde invoer")
    
    