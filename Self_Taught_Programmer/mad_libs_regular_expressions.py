#mad libs
import re
text= """Giraffes have aroused the curiosity of __PLURAL_NOUN__
    since earliest times. The giraffe is the tallest of all living
    living __Plural_Noun__, but scientests are unable to explain how it got its
    long __PART_OF_THE_BODY__. The giraffes tremendous height, whoch might reach
    __NUMBER__ __PLURAL_NOUN__, comes from its legs and __BODYPART__.
    """
def mad_libs(mls):
    """
    :param mls: string with parts the user should fill out surrounded by double
    undrscores. underscores cannot be inside hint e.g, no _hint_hint only
    _hint_.
    """
    hints=re.findall("__.*?__", mls)# we end insertions with two underscores to capture everything within
    if hints is not None:# until no more matches
        for word in hints:# word gets the iterable of list, so the first match?
            q="enter a {}". format(word)# assign the value word gets and place it in the prompt
            new=input(q) #assign q good steps in programmign consolidating 
            mls=mls.replace(word,new,1)
        print('\n')
        mls=mls.replace("\n|", "")
        print(mls)
    else:
        print("invalid mls")
mad_libs(text)
