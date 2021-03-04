def display_arguments(a,b,*args,default_arg = "Default Argument", **kwargs):
    return [a,b,args,default_arg,kwargs]

print(display_arguments("a","b","C","d",name = "Prithvi" , color = "black"))