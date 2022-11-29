from django.shortcuts import render
from .forms import NumForm

# Create your views here.

def index(request):
    form = NumForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            number1 = form.cleaned_data['number1']
            number2 = form.cleaned_data['number2']
            number3 = form.cleaned_data['number3']
            sum_1 = 0
            sum_2 = 0
            sum_3 = 0
            number1 = str(number1)
            number2 = str(number2)
            number3 = str(number3)

            for i in number1:
                sum_1 += int(i)        
            for j in number2:
                sum_2 += int(j)   
            for k in number3:
                sum_3 += int(k)
            
            if sum_1 > sum_2 > sum_3 or sum_1 > sum_3 > sum_2:
                max_value = sum_1
            elif sum_2 > sum_1 > sum_3 or sum_2 > sum_3 > sum_1:
                max_value = sum_2 
            else:
                max_value = sum_3 
            if sum_1 < sum_2 < sum_3 or sum_1 < sum_3 < sum_2:
                min_value = sum_1 
            elif sum_2 < sum_1 < sum_3 or sum_2 < sum_3 < sum_1:
                min_value = sum_2 
            else:
                min_value = sum_3 
            return render(request,'result.html', {'max_value':max_value,'min_value':min_value})
    return render(request, 'homepage.html', {'form': form})