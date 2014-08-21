#python

import webbrowser
browserURL = 'https://docs.python.org/2.7/search.html?q=%s&check_keywords=yes&area=default'

try:
    lx.eval("!user.defNew pythonSearchString string temporary")
    lx.eval("user.value pythonSearchString")
    replaceString = lx.eval("user.value pythonSearchString ?")
    searchURL = browserURL.replace('%s', replaceString)
    
    webbrowser.open(searchURL)
except:
    lx.eval("user.value pythonSearchString")
    replaceString = lx.eval("user.value pythonSearchString ?")
    searchURL = browserURL.replace('%s', replaceString)
    
    webbrowser.open(searchURL)
    