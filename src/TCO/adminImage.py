from models import *
import globale.admin

class CompositionImageline(globale.admin.TabularInline):
    model = CompositionImage
    fk_name = 'image'
    extra = 1
    readonly_fields = ('typeLogiciel', 'famille')
    fields = ('logiciel', 'commentaire', 'typeLogiciel', 'famille')

class DiscussionImageInline(globale.admin.TabularInline):
    model = DiscussionImage
    fk_name = 'image'
    extra = 1


class ImageAdmin(globale.admin.ModelAdmin):
    list_display = ('nom', 'description', )
    verbose_name_plural = 'Fiche Image'

    fieldsets = [
        (None, 
            {'fields': [('nom', 'description', ),]
             }),
                 ]
    inlines = [
        CompositionImageline,
        DiscussionImageInline, 
        ]
