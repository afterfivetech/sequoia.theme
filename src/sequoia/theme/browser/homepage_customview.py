from five import grok
from Products.CMFCore.utils import getToolByName
from Products.ATContentTypes.interface import IATFolder
from Products.CMFCore.interfaces import ISiteRoot

grok.templatedir('templates')

class homepage_customview(grok.View):
    grok.context(ISiteRoot)
    grok.require('zope2.View')
    
    def contents(self):
        brains = self.context.portal_catalog({'path':{'query':'/'.join(self.context.getPhysicalPath()),
                                                      'depth':1},
                                              'sort_on':'created',
                                              'portal_type':'Folder',
                                              'id': ('ombu-chicken-house', 'amenities', 'rooms'),
                                              'sort_order':'reverse'})
        return brains