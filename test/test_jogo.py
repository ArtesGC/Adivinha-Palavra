from unittest import TestCase
from ap_qt import J3A7P6
import string

class jogo(TestCase):

    def setUp(self):
        self.app = J3A7P6()

    def test_verifi_palavra(self):
        self.assertTrue(self.app.palavras)
        print(self.app.palavras)

    def test_historico(self):
        db = open("historico.txt","a+")
        with db:
            n=100
            eng2sp="{'pontos':100},"
            db.write(eng2sp)
            db.close()
        self.assertTrue(db)

    def test_read_historico(self):
        def process_file(filename):
            hist = dict()
            fp = open(filename)
            for line in fp:
                process_line(line, hist)
            
            print(hist)

        def process_line(line, hist):
            line = line.replace('-', ' ')
            for word in line.split():
                word = word.strip(string.punctuation + string.whitespace)
                word = word.lower()
                hist[word] = hist.get(word)
                
                
        hist = process_file('historico.txt')
        self.assertIsNone(hist)