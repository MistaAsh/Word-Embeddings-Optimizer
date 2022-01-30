import numpy as np

def read_glove_vecs(glovefile):
    with open(glovefile, 'r') as f:
        words = set()
        w2v_map = {}

        for line in f:
            line.strip().split()
            words.add(line[0])
            w2v_map[line[0]] = np.array(line[1:], dtype=np.float64)
        
    return words, w2v_map