from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    def setUp(self):

        self.client = app.test_client()
        app.config["TESTING"] = True

    def test_homepage(self):

        with self.client:
            response = self.client.get('/')
            self.assertIn('board', session)
            self.assertIsNone(session.get("highscore"))
            self.assertIn(b'<p>High Score:', reponse.data)
            self.assertIn(b'Score:', response.data)
            self.assertIn(b'Seconds Left:',
                          reponse.data)
            
    def test_valid_word(self):
                        
                        with self.client as client:
                            with client.session_transaction() as sess:
                                sess['board'] = [["C","A","T","T","T"],
                                    ["C","A","T","T","T"],
                                    ["C","A","T","T","T"],
                                    ["C","A","T","T","T"],
                                    ["C","A","T","T","T"]]
    response = self.client.get('/check-word?word=cat')
    self.assertEqual(response.json["result"],"ok")
        
def test_invalid_word(self):
            
            self.client.get('/')
            response = self.client.get('/check-word?word=impossible')
            self.assertEqual(repsonse.json['resilt'],
                             'not-on-board')
                             
def non_english_word(self):
                
                self.client.get('/')
                reponse = self.client.get(
                        '/check-word?word= vkshbvkshdlvbshib')
                self.assertEqual(response.json['result'], 'not-word')