
import re
class geterror:
    def file(file):
        file=open('results.txt','r')
        f=file.read()
        
        ERRORED_FROM='ERRORED FROM:.:.The result of section(.*).is.+.ERRORED'
        ERRORED_FROM_FINDER=re.findall(ERRORED_FROM,f)
        file.close()
        print(ERRORED_FROM_FINDER)

geterror.file('results.txt')