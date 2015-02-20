from zope.interface import implements
from zope.schema.fieldproperty import FieldProperty
from zope.component import getUtility

from browser.interfaces import IIconbarConfiguration

from OFS.SimpleItem import SimpleItem

class IconbarConfiguration(SimpleItem):
    implements(IIconbarConfiguration)
    
    twitter = FieldProperty(IIconbarConfiguration['twitter'])
    facebook = FieldProperty(IIconbarConfiguration['facebook'])
    cofp = FieldProperty(IIconbarConfiguration['cofp'])
    core  = FieldProperty(IIconbarConfiguration['core'])
    power_school = FieldProperty(IIconbarConfiguration['power_school'])
    school_cash_net = FieldProperty(IIconbarConfiguration['school_cash_net'])
    koha = FieldProperty(IIconbarConfiguration['koha'])
    rvs_resource_collection = FieldProperty(IIconbarConfiguration['rvs_resource_collection'])
    groupwise = FieldProperty(IIconbarConfiguration['groupwise'])
    rvs_gmail = FieldProperty(IIconbarConfiguration['rvs_gmail'])
    google = FieldProperty(IIconbarConfiguration['google'])
    moodle = FieldProperty(IIconbarConfiguration['moodle'])
    moodle_hub = FieldProperty(IIconbarConfiguration['moodle_hub'])
    mahara = FieldProperty(IIconbarConfiguration['mahara'])
    epearl = FieldProperty(IIconbarConfiguration['epearl'])
    blogs = FieldProperty(IIconbarConfiguration['blogs'])
    student_blogs = FieldProperty(IIconbarConfiguration['student_blogs'])
    wiki = FieldProperty(IIconbarConfiguration['wiki'])
    youtube = FieldProperty(IIconbarConfiguration['youtube'])
    elluminate = FieldProperty(IIconbarConfiguration['elluminate'])
    d2l = FieldProperty(IIconbarConfiguration['d2l'])
    rvs_live_streaming = FieldProperty(IIconbarConfiguration['rvs_live_streaming'])
    rss = FieldProperty(IIconbarConfiguration['rss'])
    tech_support = FieldProperty(IIconbarConfiguration['tech_support'])
    donations = FieldProperty(IIconbarConfiguration['donations'])
    network = FieldProperty(IIconbarConfiguration['network'])

def form_adapter(context):
    return getUtility(IIconbarConfiguration, name='iconbar_config', context=context)
