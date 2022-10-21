from django.shortcuts import render

'''
reder Lê e renderiza um arquivo
render recebe recebe um http request(request...) e o template name(...,'home. 
nesse caso nosso arquivo é do tipo html').
'''


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'Teste': 'Teste template',
    })
