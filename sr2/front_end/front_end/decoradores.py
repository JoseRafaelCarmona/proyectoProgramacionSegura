from django.shortcuts import redirect
 
def esta_logueado(vista):
    def interna(request):
        if not request.session.get('logueado', False):
            return redirect('/login/')
        request.session.get('usuario', False)
        request.session.get('password', False)
        request.session.get('codigo', False)
        return vista(request)
    return interna
