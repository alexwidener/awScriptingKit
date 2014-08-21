#python
import webbrowser
browserURL = 'http://sdk.luxology.com/index.php?search=%s&button=&title=Special%3ASearch'

try:
    lx.eval("!user.defNew modoSDKSearchString string temporary")
    lx.eval("user.value modoSDKSearchString")
    replaceStringMSDK = lx.eval("user.value modoSDKSearchString ?")
    searchURLMSDK = browserURL.replace('%s', replaceStringMSDK)
    
    webbrowser.open(searchURLMSDK)
except:
    lx.eval("user.value modoSDKSearchString")
    replaceStringMSDK = lx.eval("user.value modoSDKSearchString ?")
    searchURLMSDK = browserURL.replace('%s', replaceStringMSDK)
    
    webbrowser.open(searchURLMSDK)
    