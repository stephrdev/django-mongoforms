from django.shortcuts import render_to_response


def render_test(func):
    
    def wrapper(request, *args, **kwargs):
        result = func(request, *args, **kwargs)        
        return (isinstance(result, dict) and
            render_to_response('test_template.html', result) or result)
    
    return wrapper
