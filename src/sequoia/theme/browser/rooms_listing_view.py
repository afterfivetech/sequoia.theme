from five import grok
from Products.CMFCore.utils import getToolByName
from Products.ATContentTypes.interface import IATFolder
from plone.app.contenttypes.interfaces import IFolder
from Products.CMFCore.interfaces import ISiteRoot

grok.templatedir('templates')

#Note add this view name on the list of available view methods

class rooms_listing_view(grok.View):
    grok.context(IFolder)
    grok.require('zope2.View')
    
    def contents(self):
        brains = self.context.portal_catalog({'path':{'query':'/'.join(self.context.getPhysicalPath()),
                                                      'depth':1},
                                              'sort_on':'created',
                                              'portal_type':'Document'})
        return brains
    
    def description_val(self, desc):
        if desc:
            desc_arr = desc.split(' ')
            if len(desc_arr) <= 40:
                return desc
            else:
                return ' '.join(desc_arr[:40])+' ...'
        return ''