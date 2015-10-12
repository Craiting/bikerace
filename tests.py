import unittest
from Observer import Observer
from Racer import Racer

class TestObserverMethods(unittest.TestCase):

    def test_subscribe_to_racer(self):
        racer = Racer('Craig', 'Tingey', 123)
        observer = Observer('Agro')
        observer.subscribe(racer)
        self.assertTrue(observer.subscribedtolist[0] == racer)

    def test_unsubscribe_to_racer(self):
        racer = Racer('Craig', 'Tingey', 123)
        observer = Observer('Agro')
        observer.subscribe(racer)
        observer.unsubscribe(racer)
        self.assertTrue(len(observer.subscribedtolist) == 0)


if __name__ == '__main__':
    unittest.main()
