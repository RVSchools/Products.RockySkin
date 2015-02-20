from browser.interfaces import IIconbarConfiguration
from config import IconbarConfiguration

def setup_various(context):
    if context.readDataFile('Products.RockySkin_various.txt') is None:
        return
    portal = context.getSite()
    sm = portal.getSiteManager()
    if not sm.queryUtility(IIconbarConfiguration, name='iconbar_config'):
        sm.registerUtility(IconbarConfiguration(),
                           IIconbarConfiguration,
                           'iconbar_config')
