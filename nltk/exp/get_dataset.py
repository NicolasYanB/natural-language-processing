import os
from random import shuffle
def dataset():
    content = []
    dirs = ['1_Ensino_Fundamental_I', '2_Ensino_Fundamental_II', '3_Ensino_Medio', '4_Ensino_Superior']
    path = './corpus_readability_nlp_portuguese-master/'
    for directory in dirs:
        full_path = path+directory
        list_dir = os.listdir(full_path)
        for file in list_dir:
            with open(full_path+f'/{file}') as f:
                text = f.read()
                if not any([text == item[0] for item in content]):
                    content.append((text, directory))
    shuffle(content)
    return content
