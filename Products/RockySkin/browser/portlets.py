from plone.app.portlets.portlets.rss import Renderer as RSSRenderer

from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile


class RockySkinRSSRenderer(RSSRenderer):

    render_full = ZopeTwoPageTemplateFile('templates/rss_portlet.pt')

    @property
    def url(self):
        url = super(RockySkinRSSRenderer, self).url
        # this is pretty plone-specific, so test for presence before replacing
        if url.lower().endswith('/rss'):
            url = url[:-4]
        # ensure that we return an http url, not a feed url
        return url.replace('feed://', 'http://')
