from zope.formlib import form

from five.formlib import formbase

from interfaces import IIconbarConfiguration

class IconbarConfigurationForm(formbase.EditFormBase):
    form_fields = form.Fields(IIconbarConfiguration)
    label = "Rocky View icon bar settings form"

    def setUpWidgets(self, ignore_request=False):
        super(IconbarConfigurationForm, self).setUpWidgets(ignore_request)
        for widget in self.widgets:
            widget.displayWidth = 60
