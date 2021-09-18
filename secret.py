import string
import random

class Secret(object):

  def __init__(self):

    self.ascii=string.ascii_letters
    self.digits=string.digits
    self.p=string.punctuation
    
  
  def get_chars(self):
  
  # Get ascii Characters numbers and punctuation (minus quote characters as they could terminate string).
    chars = ''.join([self.ascii, self.digits, self.p]).replace('\'', '').replace('"', '').replace('\\', '')
    
    return chars
  
  def get_secret(self):
                     
    SECRET_KEY = ''.join([random.SystemRandom().choice(self.get_chars()) for i in range(100)])

    return SECRET_KEY
                     
if __name__ == '__main__':
  
    secret=Secret()
    print(secret.get_secret())



