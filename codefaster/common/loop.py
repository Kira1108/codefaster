def what_dict(obj, stop = 5, sep_length = 60):
    if hasattr(obj, "items"):
        i = 0
        for k,v in obj.items():
            print(f"Key({type(k)}): ", k)
            print(f"Value({type(v)}): ")
            print(v)
            i+=1
            if i == stop:
                break
            print("="*sep_length)
            
def what_list(obj, stop = 5, sep_length = 60):
    if hasattr(obj, "__iter__"):
        for i, v in enumerate(obj):
            print(f"Index: ", i)
            print(f"Value({type(v)}): ")
            print(v)
            if i == stop:
                break
            print("="*sep_length)

def what_container(obj, stop = 5, sep_length = 60):
    if hasattr(obj, "items"):
        print("Dictionary Like Object:")
        print("="*60)
        what_dict(obj, stop, sep_length)
    elif hasattr(obj, "__iter__"):
        print("List Like Object:")
        print("="*60)
        what_list(obj, stop, sep_length)
        
        
def show(obj, stop = 5, sep_length = 60):
    what_container(obj, stop, sep_length)