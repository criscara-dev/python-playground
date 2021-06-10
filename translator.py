from translate import Translator

try:
    with open('./english.txt',mode='r') as original:
        translator = Translator(to_lang="zh")   
        text = original.read()
        # print(text)   
        translation = translator.translate(text)
        with open('./new.txt',mode='w') as new_file:
            new_file.write(translation)
        # print(translation)
except FileNotFoundError as err:
    print('File does not exist')
    raise err
except IOError as err:
    print('IOError')
    raise err