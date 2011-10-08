from dajaxice.decorators import dajaxice_register
from dajax.core import Dajax
from django.template.loader import render_to_string



@dajaxice_register
def zoomReturn(request, option, id):
    if id == 'Logiciel':

        dajax = Dajax()

        from models import Logiciel 
        _logiciel = Logiciel.objects.get(pk = option )
        _famille = _logiciel.Famille
        options = Logiciel.objects.filter( Famille = _famille  )
        
        out = ""
        for o in options:
            out = '%s<option value="#">%s</option>' % (out, o)
 
 
        dajax.assign('#id_LogicielRef', 'innerHTML', out)
        dajax.assign('#id_famille', 'value', _famille.Nom  )
        
        
        
        return dajax.json()

    else:
        pass
    
