class getme:
    def grabVersion(filename):
        versionget=open('versiongit.txt','w')
        with open(filename) as logfile:
            for line in logfile:
                if 'Switch Ports Model' in line:
                    
                    
                    versionget.write(line)
                    nextline=next(logfile)
                    if '------ ' in nextline:
                        nextline=next(logfile)
                    
                    versionget.write(nextline)
                    nextline=next(logfile)
                    versionget.write(nextline)
                    break
        versionget.close()
                
