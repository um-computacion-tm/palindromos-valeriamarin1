import unittest
def is_palindrome(mystring):
    clean_string = ''.join(char.lower() for char in mystring if char.isalnum())
    return clean_string == clean_string[::-1]
class TestPalindrome(unittest.TestCase):
    def test_neuquen_1(self):
        resultado = is_palindrome('neuquen')
        self.assertEqual(resultado, True)
 
    def test_Neuquen_2(self):
        resultado = is_palindrome('Neuquen')
        self.assertEqual(resultado, True)
        
    def test_neuquen_3(self):
        resultado = is_palindrome('n euq uen')
        self.assertEqual(resultado, True)
    
    def test_neuquen_4(self):
        resultado = is_palindrome('@neuquen!')
        self.assertEqual(resultado, True)
    
    def test_neuquen_5(self):
        resultado = is_palindrome('neuqune')
        self.assertEqual(resultado, False)
    def test_neuquen_6(self):
        resultado = is_palindrome('neuqune')
        self.assertEqual(resultado, False)

unittest.main()

    