from cgi import test
from operator import index
import re

from unittest import TestResult, result
from importlib_metadata import Sectioned

from numpy import short




global zack
zack=0
global sectionfailedreasonreason
sectionfailedreasonreason=[]

global blockedreason
blockedreason=[]
global errorsection
errorsection=[]
global sectionfailedreason
sectionfailedreason=[]
global abortreason
abortreason=[]
global secretfailedreasons
secretfailedreasons=[]
global errorsectioniter
global steplist
global sectionfailed
sectionfailed=[]
steplist=[]
class printer:
    def setup(testcase,result,sreason,ereason,Section,sectionfailed,errored,blocked,abortreason,failedonly,pre,post,errorsection,ar,blocklist,blockreason,sectionfailedreasonreason,steplist):
        finalfile=open('results.txt','w+')
        errorsectioniter=0

        y=0
        z=0
        w=0
        sf=0
        b=0
        z=0
        n=0
        danger=0
        failed=0
        error=0
        preiter=0
        postiter=0
        seciter=0
        sfd=0
        blocklistiter=0
        bbb=0
        aaa=0
        nnn=0
        secfailiter=0
        ind=1
        ind2=1
        line2=[]
        txt2='.Starting testcase.'
        txt='.Starting.'
        testcase=testcase
        result=result
        table ={}
        Section=[]
        sectionresult=[]
        failedreason=[]
        skippedreason=[]
        testcaseerrorreason=[]
        Sectionblockedreason=[]
        erroredreason=[]
        
        failedsections=[]
        ind=0
        ind2=0
        ind3=0
        skipind=0
        erroriter=0
        blockiter=0
        prevline=""
        abortiter=0
        findex=0
        testcaseerrorindex=0
        secindex=0
        postpreind=0
        pre=[]
        preind=0
        abortrare=[]
        abortrareiter=0
        blockedlist=[]
        blocediter=0
        blockedreasoniter=0
        sectionfailedreasonreasoniteriter=0
        zack=0
       
        if (len(testcase))==0:
            finalfile.write(str(ar))
            finalfile.write("\n")
            if testcase:
                finalfile.write(testcase[0])
            
            finalfile.write("Caught keyboard interrupt (ctrl+c): aborting script run immediately\n")
        else:
            finalfile.write("FROM METHOD SETUP\n")
            finalfile.write("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")


            
        
        for x in range(len(testcase)):
            
                
            if (len(testcase))==0:
                finalfile.write(ar)
            finalfile.write(result[x])
            if (len(result))==1 and 'Passed' in result[0]:
                finalfile.write("Preason:None\n")
                finalfile.write("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            if "PASSED"  in result[x]:
                finalfile.write("Preason:None\n")
                finalfile.write("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
                print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            else:
                pass
            if "BLOCKED" in result[x]:
                
                finalfile.write("Block reason:" +blockreason[bbb])
                print("KAKAKAKA"+blockreason[bbb])
                finalfile.write("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

                print(blockedreasoniter)
                print(blockreason[bbb])
                bbb+=1
            if "ERRORED" in result[x]:
                if ereason:
                    print("DADDDY"+ereason[y])
                    finalfile.write(ereason[y])
                    finalfile.write("Errored-w reason:is given\n")
                elif errored:
                    finalfile.write("ERRORED REASON:"+errored[y])

                    finalfile.write("ERRORED FROM:"+errorsection[y])

           
                
                print("__________________ERORO")
                print( errorsectioniter)
                        
                    
               

                    
                #else:
                 #   print(errored[error])
                finalfile.write("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
                print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                y+=1
                errorsectioniter+=1

            if "SKIPPED" in result[x]:
                finalfile.write("Testcase was skipped\n")
                finalfile.write(sreason[z])
                
                finalfile.write("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
                print(sreason[z])
                print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                z+=1
            if "ABORTED" in result[x]:
                finalfile.write("THIS testcase was aborted, we found the section for the aborting:\n")
                finalfile.write(abortreason[n])
                print("THIS testcase was aborted, we found the section for the aborting:",end=' ')
                print(abortreason[n])
                finalfile.write("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
            
            if "FAILED" in result[x]:
                if sectionfailed:
                    finalfile.write(sectionfailed[aaa])
                    #finalfile.write(sectionfailedreasonreason[nnn])
                    print(sectionfailed[aaa])
                    aaa+=1
                    nnn+=1
                if failedsections:
                    finalfile.write(failedsections[secfailiter])
                    secfailiter+=1
                        
                    
                if failedonly:
                    finalfile.write("FAIL DUE TO:"+failedonly[failed])
                    failed+=1
                    if secretfailedreasons:
                        pass
                        #finalfile.write("Fail reasson:"+secretfailedreasons[sfd])
                    elif secretfailedreasons or sectionfailedreason or sectionfailedreasonreason  :
                        finalfile.write("Fail reason: none found\n")
                elif pre:
                    finalfile.write("FAIL DUE TO:" +pre[preiter])
                    finalfile.write("Failed reason: none found\n")
                elif post:
                    finalfile.write("FAIL DUE TO:"+post[postiter])
                    finalfile.write("Failed reason:none found\n")
                
                elif sectionfailedreason:
                    finalfile.write("FAIL DUE TO:"+sectionfailedreason[failed])
                    finalfile.write("Failed reason:None found\n" )

                elif secretfailedreasons:
                    finalfile.write("Failure reason:"+secretfailedreasons[sfd])
                #else:
                 #   finalfile.write("UKNOWN SECTION \n")
                finalfile.write("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
                
                print("This testcase failed due to Section:",end='')
                
                #failed+=1
                preiter+=1
                postiter+=1
                seciter+=1
                errorsectioniter+=1
                sfd+=1
                
                zack+=1
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        finalfile.close()
                  
            
            
            
            
            #enter log here
            

    def gettestcase(testcase):
        return testcase
        
    def poop():
        #now we read in the file, and we look to find if it states starting testcase!
        ind=1
        ind2=1
        line2=[]
        txt2='.Starting testcase.'
        txt='.Starting.'
        testcase=[]
        result=[]
        table ={}
        Section=[]
        sectionresult=[]
        failedreason=[]
        skippedreason=[]
        testcaseerrorreason=[]
        Sectionblockedreason=[]
        sectionfailedreason=[]
        erroredreason=[]
        blockedreason=[]
        abortreason=[]
        failedsections=[]
        ind=0
        ind2=0
        ind3=0
        skipind=0
        erroriter=0
        blockiter=0
        prevline=""
        abortiter=0
        findex=0
        testcaseerrorindex=0
        secretfailedreasons=[]
        secindex=0
        post=[]
        errorsection=[]
        postpreind=0
        pre=[]
        preind=0
        abortrare=[]
        abortrareiter=0
        blockedlist=[]
        blocediter=0
        blockedreason=[]
        blockedreasoniter=0
        sectionfailedreasonreason=[]
        sectionfailedreasonreasoniteriter=0
        steplist=[]
        stepiter=0
        with open('new.txt','r') as log3:
            count=1
            for line in log3:
                if "subsection" in line:
                    if "ABORTED" in line:
                        abortrare.insert(0,line)
                        
                if "Starting testcase" in line or "Starting execution of testcase" in line:
                    testcase.insert(ind,line.strip('\n'))
                    ind+=1
                    
                if "Failed reason" in line:
                    secretfailedreasons.insert(secindex,line)
                    secindex+=1
                        
                if "The result of section"  in line or "result for section" in line:
                    Section.insert(ind,line)
                    ind+=1
                    
                    if "FAILED" in line:
                        failedsections.insert(findex,line)
                        if "reason" in prevline:
                            sectionfailedreason.insert(ind2,prevline)
                        else:
                            sectionfailedreasonreason.insert(sectionfailedreasonreasoniteriter,"no fail reason found\n")
                        ind2+=1
                        findex+=1
                        sectionfailedreasonreasoniteriter+=1
                        print(prevline)
                    if "ERRORED" in line:
                        errorsection.insert(erroriter,line)
                        erroredreason.insert(erroriter,prevline.strip('pyATS Health Check get_devices '))
                        erroriter+=1
                        print(prevline)
                    if "BLOCKED" in line and "reason" in prevline:
                        blockedreason.insert(blockiter,prevline)
                        
                if 'The result of STEP' in line:
                    if 'errored' in line:
                        steplist.insert(stepiter,line)
                            
                if 'The result of Post'  in line:
                    if "FAILED" in line:
                        
                        post.insert(postpreind,line)
                        postpreind+=1
                if 'The result of Pre'in line:
                    if "FAILED" in line:
                        pre.insert(preind,line)
                        preind+=1   
                if "result of testcase" in line or "Testcase result for" in line:
                    result.insert(ind3,line)
                    ind3+=1
                    if "BLOCKED" in line:
                        blockedlist.insert(blocediter,line)
                        blocediter+=1
                        if "Blocking" in prevline:
                            blockedreason.insert(blockedreasoniter,prevline)
                            blockedreasoniter+=1
                            
                        
                    if "SKIPPED" in line:
                        skippedreason.insert(skipind,prevline)    
                        skipind+=1
                    if "ERRORED" in line and "reason" in prevline:
                        erororor=0
                        for x in range(len(testcase)):
                            Section[x]
                            if "ERRORED" in Section[x]:
                                testcaseerrorreason.insert(testcaseerrorindex,Section[x])
                            else:
                                break
                        ti=0
                        if "PASSED" not in prevline:
                            testcaseerrorreason.insert(erororor,prevline)
                        else:
                            for x in range (len(erroredreason)):
                                testcaseerrorreason.insert(ti,erroredreason[x])
                                ti+=1

                    if "ABORTED" in line:
                        for x in range(len(Section)):
                            Section[x]
                            if "ABORTED" in Section[x]:
                                abortreason.insert(abortiter,"ABORTED DUE TO:" + Section[x])
                        
                    #if "FAILED" in line:
                    #   skippedreason.insert()
                prevline=line
        #print(testcaseerrorreason)
        #print(blockedreason)
        #nt(len(erroredreason))
        #print(sectionfailed)
        print(testcase)
        print(result)
        printer.setup(testcase,result,skippedreason,testcaseerrorreason,Section,sectionfailedreason,erroredreason,blockedreason,abortreason,failedsections,pre,post,errorsection,abortrare,blockedlist,blockedreason,sectionfailedreasonreason,steplist)
        #print(pre)
        #print(post)
        #print(erroredreason)
        #print("hi")
        #print(sectionfailedreason)
        #print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
        #print("hi")
        #print(secretfailedreasons)
        #print(errorsection[0])
        #dict={}
        #dict=loglinkdata.loglinkdatamethod()
        #print("+++++++++++++++++++++++++++++++++++++++++++++===______________+++++++++++++")
        #print(dict[1])
        #tablemaker.tablemaker()
            
