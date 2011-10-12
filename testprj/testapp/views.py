from decorators import render_test

from forms import Test001ChildForm


@render_test
def test001(request):
    
    if request.method == 'POST':
        form = Test001ChildForm(request.POST)
        
        if form.is_valid():
            form.save()
        
    else:
        form = Test001ChildForm()
    
    return {'form': form}
