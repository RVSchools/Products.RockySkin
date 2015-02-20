from zope.component import queryUtility
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase

from interfaces import IIconbarConfiguration

class MemberMenu(ViewletBase):
    render = ViewPageTemplateFile('templates/member_menu_viewlet.pt')

    def update(self):
        # set here the values that you need to grab from the template.
        self.menu_items = list(['Dumb1','Dumber1','Dumbest1'])
        
    def isMember(self):
        # flag to indicate if user is a member
        return not self.context.portal_membership.isAnonymousUser()
        
    def getMenuItems(self):
        #path = '/'.join(self.context.getPhysicalPath())
        #if path=='/Plone/news-home':
        #    path = '/Plone'
        #path='/Plone'
        #tail = self.context.portal_url().split('/')[-1]
        #path = '/%s' % tail
        
        # VHM fix - Nov 2008
        root = self.context.portal_url.getPortalObject()
        path = '/%s' % root.getId()
        
        cat = self.context.portal_catalog
        return cat.searchResults(review_state='members',
                                 path={'query':path, 'depth':1},
                                 sort_on='getObjPositionInParent'
                                 )

class IconBar(ViewletBase):
    render = ViewPageTemplateFile('templates/iconbar.pt')

    def get_icons(self):
        "get icon information from storage utility"
        icons = queryUtility(IIconbarConfiguration,
                           name='iconbar_config',
                           context=self.context) 
        return icons
