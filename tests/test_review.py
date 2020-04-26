import unittest
from app.models import Review

class ReviewTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_review = Review(1234,'Python Must Be Crazy Review','','This was whack')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_review,Review))