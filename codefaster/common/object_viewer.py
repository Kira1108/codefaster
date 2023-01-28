import inspect
import re
import types
from dataclasses import dataclass
from typing import Union, Any

@dataclass
class ObjectViewer:
    
    pattern:str = None
    print_doc:bool = False
    constructor_doc:bool = False
    remove_private:Union[bool,str] = True
    
    def __post_init__(self):
        self.pattern = re.compile(self.pattern) if self.pattern else re.compile(".*")
        
    def _valid(self,attr:str):
        r = self.pattern.search(attr)
        
        if isinstance(self.remove_private, str):
            p = not attr.startswith(self.remove_private)
            
        else:
            p = not attr.startswith("_")
            
        if attr in ['__iter__',"__getitem__","__call__"]:
            p = True
            
        return r and p
    
    def _member_type(self, obj, attr):
        
        if inspect.ismethod(getattr(obj, attr)) or inspect.isfunction(getattr(obj,attr)):
            
            if isinstance(getattr(obj, attr),types.FunctionType):
                mtype = '[*****]static method'
            elif getattr(obj, attr).__self__  == obj:
                mtype =  'instance method'
            else:
                mtype =  "[*****]class method"
            
            return mtype, getattr(obj, attr).__doc__
        else:
            return "attribute", None
        

    def __call__(self, obj):
        print("Class", type(obj))
        print("Callable: ", callable(obj))
        print("-"*100)
        
        for attr in dir(obj):
            if not self._valid(attr):
                continue
                
            mtype, doc = self._member_type(obj, attr)
            
            print(f"{attr}: {mtype}")
            
            if doc and self.print_doc:
                print("-"*30)
                print(doc)
            
            print("-"*100)
            
            if self.constructor_doc:
                print("Constructor Documentation: ")
                print(obj.__class__.__doc__)
                print("-"*100)
                
                
def view(obj:Any, pattern = None, print_doc = False, constructor_doc = False, remove_private = True) -> None:
    viewer = ObjectViewer(
        pattern, print_doc, constructor_doc = constructor_doc, 
        remove_private=remove_private)
    viewer(obj)
    