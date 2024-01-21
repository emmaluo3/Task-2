"""
file: politeness_features.py
---
Defines a feature that calls the PolitenessStrategies from ConvoKit
and returns them as 21 columns (for each message).

Link to Politness Documentation: https://convokit.cornell.edu/documentation/politenessStrategies.html
Link to ConvoKit GitHub examples: https://github.com/CornellNLP/ConvoKit/tree/master/examples/politeness-strategies

You should follow the samples to create the appropriate imports, process the data, and call the function.
"""


"""
function: get_politeness_strategies
(Chat-level function)

This gets the politeness annotations of each message, with some fields 
including HASHEDGE, Factuality, Deference, Gratitude, Apologizing, etc.
"""

import convokit
import spacy
import pandas as pd



from convokit import Corpus, Speaker, Utterance
from convokit import download
from convokit import TextParser
from convokit import PolitenessStrategies

spacy.cli.download("en_core_web_sm")

def get_politeness_strategies(text):
     ps = PolitenessStrategies()
     spacy_nlp = spacy.load('en_core_web_sm', disable=['ner'])
     utt = ps.transform_utterance(text, spacy_nlp=spacy_nlp)
     result_dict = utt.meta['politeness_strategies']
     if not result_dict:  # Check if the dictionary is empty
        return pd.DataFrame()
     new_dict = {}
     cleaned_dict = {key.replace("feature_politeness_==", "").replace("==", ""): value for key, value in result_dict.items()}
     df = pd.DataFrame([cleaned_dict], columns=cleaned_dict.keys())
     return (df)
     


