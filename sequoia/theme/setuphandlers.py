from collective.grok import gs
from sequoia.theme import MessageFactory as _

@gs.importstep(
    name=u'sequoia.theme', 
    title=_('sequoia.theme import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('sequoia.theme.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
