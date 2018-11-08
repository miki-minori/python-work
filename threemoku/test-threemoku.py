from unittest import TestCase,main
from threemoku import hantei

class TestThreeMoku(TestCase):

    def test_hantei(self):
        self.assertFalse(hantei([['＊','＊','＊'],['＊','＊','＊'],['＊','＊','＊']], '〇'))
        self.assertTrue(hantei([['〇','＊','＊'],['〇','＊','＊'],['〇','＊','＊']], '〇'))

if __name__ == '__main__':
    main()
