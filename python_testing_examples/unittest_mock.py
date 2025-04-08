# notifier.py
import smtplib

def send_email(recipient, message):
    server = smtplib.SMTP('smtp.example.com')
    server.sendmail("from@example.com", recipient, message)
    server.quit()


import unittest
from unittest.mock import patch

class TestEmailFunction(unittest.TestCase):
    @patch('smtplib.SMTP')
    def test_send_email(self, mock_smtp):
        mock_server = mock_smtp.return_value
        send_email("to@example.com", "Hello!")
        
        mock_smtp.assert_called_with('smtp.example.com')
        mock_server.sendmail.assert_called_once_with(
            "from@example.com", "to@example.com", "Hello!"
        )
        mock_server.quit.assert_called_once()

if __name__ == '__main__':
    unittest.main()
