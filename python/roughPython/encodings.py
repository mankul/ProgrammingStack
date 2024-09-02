from sklearn.preprocessing import LabelEncoder
import numpy as np
import re
from sklearn.preprocessing import OneHotEncoder


def stringToArray(sequence):
    sequence = re.sub('[^a-z]','', sequence)
    sequence = list(sequence)
    return sequence



def labelEncode():
    labelEncoder = LabelEncoder()
    labelEncoder.fit(np.array(list(map(chr, range(97,123)))))
    return labelEncoder

def ordinalSequencing(labelEncoder, sequence):
    int_encoded = labelEncoder.transform(sequence)
    print(int_encoded)
    float_encoded = int_encoded.astype(float)
    for i in range(26):
        float_encoded[float_encoded==i] = i/26
    return float_encoded
def oneHotEncoding(label_encoder, sequence):
    oneHotEncoder = OneHotEncoder(sparse_output=False, dtype=int)
    int_encoder = label_encoder.transform(sequence)
    int_encoder = int_encoder.reshape(len(int_encoder),1)
    oneHotEncode = oneHotEncoder.fit_transform(int_encoder)
    return oneHotEncode
string = "abcdefghijkaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
sequence = stringToArray(string)
print(sequence)
labelEncode = labelEncode()
print(ordinalSequencing(labelEncode, sequence))
print(oneHotEncoding(labelEncode, sequence))
