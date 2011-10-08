from models import *
import globale.admin


class ReferenceAdmin(globale.admin.ModelAdmin):
    list_display = ('etiquette', 'description',)
    fieldsets = [
        (None, 
            {'fields': [('etiquette', 'description', ),
                        ('enregistrementBibTex')
                        ]
             }),
                 ]
    app_name = 'Base'

class FamilleAdmin(globale.admin.ModelAdmin):
    app_name = 'Base'

class TypeLogicielAdmin(globale.admin.ModelAdmin):
    app_name = 'Base'

class NiveauAdmin(globale.admin.ModelAdmin):
    app_name = 'Base'
