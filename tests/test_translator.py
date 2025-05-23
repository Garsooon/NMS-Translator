from translator.core import translate

def test_translation():
    test_dict = {'hello': 'hola', 'world': 'mundo'}
    assert translate('hello world', test_dict) == 'hola mundo'
    assert translate('unknown word', test_dict) == 'unknown word'