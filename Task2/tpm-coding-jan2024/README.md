# Team Processing Mapping Coding Task
Welcome to the coding task for the Team Process Mapping project! Before you begin, please make sure to read through the full instructions [here](https://docs.google.com/document/d/1_FZ-N-7Qr9_CXK-fX9vdcMhkaDzmRXyUh1aHEHjL1hs/edit).

## Packages and Requirements
The packages required for you to complete the task are listed in `requirements.txt`. You can use a virtual environment for managing the dependencies associated with this project.

## Your Goal
To complete this assignment, you will need to modify 4 different files:
- features/word_count.py: `count_words(text)`
- features/type_token_ratio.py: `get_word_ttr(text)`
- features/politeness_features.py: `get_politeness_strategies(text)`
- utils/calculate_chat_level_features.py (For calling the functions; you only need to modify `apply_politeness()`).

## Your Deliverables
At the end of Part 2, we will need the following:
- A link to your GitHub cloned repository. This should contain:
  1. Your Python code;
  2. Your Part 2 Reflection (directly edit this README!).
- A copy of your chat-level CSV that contains columns for the features you generated. **Note: this should be reproducible!** We should be able to get the same results by running your code from the GitHub link you submit.

# Part 2 Reflection
Please answer the following four questions:

## 1. Sanity Check
Open up your output CSV and look at the columns you generated for each of the three features. Do the values “make sense” intuitively? Why or why not?
Although I was not able to get apply_politeness to work, my values for the other functions make sense. When I count the words in the first few rows for the "message" column it matches up with num_words. Moreover, the values for word_TTR are between 0 and 1 which seems reasonable. 

## 2. Testing
How would you implement tests for these features?
I would use pytest and implement multiple use cases and edge cases. For the use cases, I would test what would be typically given to my features, such as a sentence in string form. For my edge cases I would test the case of unusual sentences, such as a sentence only having one word, a sentence having all of the same word, or an empty string. By testing a variety of cases I can make sure that my features work, even in instances where the input is abnormal from what it should be. 

## 3. Overall Experience
In the beginning, understanding different paths and where to call my functions was new to me. I also had difficulty implementing apply_politeness and I would be interested in learning more about how I can fix my code to make it work. It was interesting working with a variety of messages and I enjoyed coding features that engaged me with these messages.


## 4. Time Required
I spent around 6 hours on Tasks 1 and 2 combined. 
