from unittest import result


class logmaker:
    def logmake():
        prevline='a'
        with open('regularlog.txt','r+')as logfile:
            with open ('regularlog2.txt','w') as resultfile:
                f=logfile.readlines()
                
                for line in f:
                    
                    if 'result of testcase' in line:
                        resultfile.write(line)
                        resultfile.write("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                        resultfile.write("\n")
                        resultfile.write("\n")
                    else:
                        resultfile.write(line)
                prevline=line
        filefile=open('regularlog.txt','r')
        ff=filefile.read()
        nana=ff.split('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        return nana

