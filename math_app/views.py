import select
from django.views.generic import TemplateView, CreateView
from django.shortcuts import render, redirect


# Create your views here.


class Physics_page(TemplateView):
    template_name = 'physics.html'
    selected_menu = 2
    def dispatch(self, request):
        
        if request.method == 'POST':
            return redirect('/math/')
        return render(request, self.template_name,
        context= {'menu_num':self.selected_menu})

class Chemistry_page(TemplateView):
    template_name = 'physics.html'
    selected_menu = 3
    def dispatch(self, request):
        if request.method == 'POST':
            return redirect('/math/')
        return render(request, self.template_name,
        context= {'menu_num':self.selected_menu})

class Math_page(TemplateView):
    template_name = 'math.html'
    selected_menu = 1
    def dispatch(self, request):
        if request.method == 'POST':
            if request.POST.get('number_button') == '1':
                return redirect('/math/task1')
        return render(request, self.template_name, 
        context= {'menu_num':self.selected_menu})
class Math_task1(TemplateView):
    template_name = 'math_task1.html'
    selected_menu = 1
    
    def dispatch(self, request):
        x1 = None
        x2 = None
        total = False
        d = None
        d1 = None
        k1, k2, k3 = None, None, None
        if request.method == 'POST':
            try:
                k1 = int(request.POST.get('k1'))
                k2 = int(request.POST.get('k2'))
                k3 = int(request.POST.get('k3'))
                d = k2 ** 2 - 4 * k1 * k3
                d1 = d
                d = d ** 0.5

                x1 = (k2 * -1 + d) / ( 2 * k1)
                x2 = (k2 * -1 - d) / ( 2 * k1)
                total = True
            except:
                pass

            



        return render(request, self.template_name,context= {'menu_num':self.selected_menu,
        'x1':x1,'x2':x2,'c1': k1, 'c2': k2, 'c3': k3, 'D':d1, 'Ds':d, 'total':total})

def start_page(request):
    return redirect('/physics/')

