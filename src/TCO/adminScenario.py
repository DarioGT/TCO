from models import *
import globale.admin

class SIOInline(globale.admin.TabularInline):
    model = SIO
    fk_name = 'organisation'
    extra = 1

class OrganisationAdmin(globale.admin.ModelAdmin):
    list_display = ('nom', 'description', )
    verbose_name_plural = 'Fiche Organisation'

    fieldsets = [
        (None, 
            {'fields': [('nom', 'description', ),]
             }),
                 ]
    inlines = [
        SIOInline,
        ]
