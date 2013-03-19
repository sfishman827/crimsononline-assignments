import re
import lxml.html

def parse_links_regex(filename):
    """question 2a

    Using the re module, write a function that takes a path to an HTML file
    (assuming the HTML is well-formed) as input and returns a dictionary
    whose keys are the text of the links in the file and whose values are
    the URLs to which those links correspond. Be careful about how you handle
    the case in which the same text is used to link to different urls.
    
    For example:

        You can get file 1 <a href="1.file">here</a>.
        You can get file 2 <a href="2.file">here</a>.

    What does it make the most sense to do here? 
    """
    f = open(filename)
    text = f.read()
    tuples = re.findall(r'<a .*?href="(.*)".*?>(.*?)</a>', text, re.IGNORECASE)
    result = []
    for obj in tuples:
        result.append(obj[::-1])
    return result

def parse_links_xpath(filename):
    """question 2b

    Do the same using xpath and the lxml library from http://lxml.de rather
    than regular expressions.
    
    Which approach is better? (Hint: http://goo.gl/mzl9t)
    """
    result = []
    it = lxml.html.iterlinks(open(filename).read())
    for anchor in it:
        if not anchor[0].text == None:
            result.append((anchor[0].text, anchor[2]))
    return result
