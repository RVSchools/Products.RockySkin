#
# Skeleton RockySkinTestCase
#

from Products.PloneTestCase import PloneTestCase

PloneTestCase.installProduct('RockySkin')
PloneTestCase.setupPloneSite(products=['RockySkin'])


class TestSomething(PloneTestCase.PloneTestCase):


    def afterSetUp(self):
        pass

    def testSomething(self):
        # Test something
        self.assertEqual(1+1, 2)


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestSomething))
    return suite
