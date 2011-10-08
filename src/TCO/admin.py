from models import *
import globale.admin


# ==== Fiche Logiciel 
from adminLogiciel import LogicielAdmin 
globale.admin.site.register(Logiciel, LogicielAdmin)

# ==== Fiche Image 
from adminImage import ImageAdmin 
globale.admin.site.register(Image, ImageAdmin)


# ==== Fiche Organisation  
from adminScenario import OrganisationAdmin
globale.admin.site.register(Organisation, OrganisationAdmin)

# ===== Prevoir plugin bibtex 
from adminBase import ReferenceAdmin
globale.admin.site.register(Reference, ReferenceAdmin) 


# ====  Maestros 
from adminBase import FamilleAdmin
globale.admin.site.register(Famille, FamilleAdmin)

from adminBase import TypeLogicielAdmin
globale.admin.site.register(TypeLogiciel, TypeLogicielAdmin)

from adminBase import NiveauAdmin
globale.admin.site.register(Niveau, NiveauAdmin)


#===============================================================================

# globale.admin.site.register(Scenario)
# globale.admin.site.register(CompositionScenario)
# globale.admin.site.register(TCO)
# globale.admin.site.register(SpecificationLogiciel)


