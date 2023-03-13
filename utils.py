def read_conll_file(fn, min_length=0):
    '''
    Read tagged data fron CONLL file.
    
    Returns a table of sequences of tokens with POS tags and IOB NER tags.
    '''

    data = []
    with open(fn, 'rt') as f:
        buf = []
    
        for line in f.readlines():
        
            if line.find('DOCSTART') != -1: continue
            
            if len(line) == 1:
                if len(buf) > 0:
                    if min_length == 0 or len(buf) >= min_length:
                        data.append(buf.copy())
                    buf = []
            else:
                # print(i, line.strip())
                a, b, c, d = line.strip().split()
                # print('     >>>>', a, d)
                buf.append((a,b,d))
    return data