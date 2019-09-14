#!/usr/bin/env python

import sys
import importlib
import time


if __name__=="__main__":
    sys.path.append('/home/support/import_test')
    
    while 1:
        path = "py_package.child"
        imported_module = importlib.import_module(
           path.strip('.'), package=path.strip(".")
        )
    
    
        imported__module = importlib.reload(
            imported_module
        ) 
        
        #print(dir(imported_module))
        #file_import = getattr(imported_module, ".child")
        method  = getattr(imported_module, "some_method")
        method()
  
        time.sleep(10)
