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
                                              'review_state':'published',
                                              'sort_on':'created',
                                              'portal_type':'Document',
                                              'sort_order':'reverse'})[:3]
        return brains