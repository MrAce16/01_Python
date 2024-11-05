# foo
# posn args
# kwargs
# foo
 
# foo(1,2,3,name="Test")
 
# OUTPUT
#  (6, {"name" : "Test"} )


def foo(*args, **kwargs):
    posn_args_sum = sum(args)

    for i in args:
        if not isinstance(i,(int,float)):
            raise ValueError

    return posn_args_sum,kwargs


 
 