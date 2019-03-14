import re
l="Beautiful is better than ugly."
matches=re.findall("beautiful",l,re.IGNORECASE) # third param is optional
print(matches)


zen="""Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

m=re.findall("^If", zen,re.MULTILINE)

print(m)


string="Two too."
r=re.findall("t[ow]o", string, re.IGNORECASE)
print(r) 


line= "123?34 hello?"

n=re.findall("\d", line, re.IGNORECASE)
print(n)


t="__one__ __two__ __three__"
found=re.findall("__.*?__",t)
for match in found:
    print(match)
print(found)


line="I love $"
r=re.findall("\\$", line, re.IGNORECASE)
print(r)

