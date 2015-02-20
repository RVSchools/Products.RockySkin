## Script (Python) "preloadBanners"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=Insert javascript banner preloader function
##
request = container.REQUEST
RESPONSE =  request.RESPONSE

results = context.portal_catalog.searchResults(REQUEST=request,
                                              path = '/Plone/logos',
                                              Type = 'Image')

L = []
L.append("%s/logo.jpg" % context.portal_url())
for brain in results:
    L.append(brain.getURL())
    #print "Logo: " , brain.getURL()

A = []
R = []
c = 0

skel = "pic%s = new Image(1000,220);\npic%s.src = '%s';"
for it in L:
    c+=1
    R.append(skel % (c,c,it))
    A.append("pic%s" % c)

print "function randInt( lo, hi ) {return lo + Math.floor((hi-lo+1) * Math.random());}"
print "\n"
print "\n".join(R)
print "\nimgs = [%s];" % ",".join(A)
print """\nfunction rotate() 
{
    var idx = randInt(0,imgs.length-1);
    document['banner'].src = imgs[idx].src;
}

setInterval(rotate,7500);"""

return printed