from zope.interface import Interface
from zope import schema
from plone.theme.interfaces import IDefaultPloneLayer

class IThemeSpecific(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 skin layer bound to a Skin
       Selection in portal_skins.
       If you need to register a viewlet only for the "RockySkin"
       skin, this is the interface that must be used for the layer attribute
       in RockySkin/browser/configure.zcml.
    """

class IIconbarConfiguration(Interface):
    "Plone configlet form"
    twitter = schema.TextLine(title=u"Twitter",
                              required=False,
                              default=u"http://twitter.com/rvsed")
    facebook = schema.TextLine(title=u"Facebook",
                              required=False,
                              default=u"http://www.facebook.com/pages/Rocky-View-Schools/166268840087518")
    cofp = schema.TextLine(title=u"Communities of Practice",
                              required=False,
                               default=u"http://cofp.rockyview.ab.ca")
    core = schema.TextLine(title=u"CORE",
                              required=False,
                               default=u"")
    power_school = schema.TextLine(title=u"Power School",
                              required=False,
                                              default=u"")
    school_cash_net = schema.TextLine(title=u"School Cash Net",
                              required=False,
                                default=u"")
    koha = schema.TextLine(title=u"Koha",
                              required=False,
                                              default=u"")
    rvs_resource_collection = schema.TextLine(title=u"RVS Resource Collection",
                              required=False,
                                              default=u"")
    groupwise = schema.TextLine(title=u"Groupwise",
                              required=False,
                                              default=u"")
    rvs_gmail = schema.TextLine(title=u"RVS Gmail",
                              required=False,
                              default=u"http://gmail.rvschools.ab.ca/")
    google = schema.TextLine(title=u"Google",
                              required=False,
                             default=u"")
    moodle = schema.TextLine(title=u"Moodle",
                              required=False,
                             default=u"http://moodle.rockyview.ab.ca")
    moodle_hub = schema.TextLine(title=u"Moodle Hub",
                              required=False,
                                 default=u"")
    mahara = schema.TextLine(title=u"Mahara",
                              required=False,
                             default=u"https://mahara.rockyview.ab.ca")
    epearl = schema.TextLine(title=u"Epearl",
                              required=False,
                             default=u"https://epearl.rockyview.ab.ca/login/pages/user.php")
    blogs = schema.TextLine(title=u"RVS Blogs",
                              required=False,
                                default=u"http://blogs.rockyview.ab.ca")
    student_blogs = schema.TextLine(title=u"Student Blogs",
                              required=False,
                                              default=u"")
    wiki = schema.TextLine(title=u"Wiki",
                              required=False,
                            default=u"http://wikis.rockyview.ab.ca")
    youtube = schema.TextLine(title=u"YouTube",
                              required=False,
                                              default=u"")
    elluminate = schema.TextLine(title=u"Elluminate",
                              required=False,
                                 default=u"")
    d2l = schema.TextLine(title=u"D2L",
                              required=False,
                                              default=u"")
    rvs_live_streaming = schema.TextLine(title=u"RVS Tube",
                              required=False,
                               default=u"")
    rss = schema.TextLine(title=u"RSS",
                              required=False,
                          default=u"")
    tech_support = schema.TextLine(title=u"Tech Support",
                              required=False,
                               default=u"")
    donations = schema.TextLine(title=u"Donations",
                              required=False,
                                          default=u"")
    network = schema.TextLine(title=u"netWORK",
                              required=False,
                                          default=u"")

