class printer:
    def setup(testcase,result,sreason,ereason,Section,sectionfailed,errored,blocked,abortreason,failedonly,pre,post,errorsection,ar,blocklist,blockreason,sectionfailedreasonreason,secretefailedreasons):
        finalfile=open('results.txt','w+')
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
        errorsectioniter=0
        sfd=0
        blocklistiter=0
        bbb=0
        aaa=0
        nnn=0
        print("FROM METHOD SETUP")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        if (len(testcase))==0:
            finalfile.write(str(ar))
            finalfile.write("\n")
            finalfile.write("THIS PROGRAM WAS ABORTED\n")
            finalfile.write("Caught keyboard interrupt (ctrl+c): aborting script run immediately\n")
        else:
            finalfile.write("FROM METHOD SETUP\n")
            finalfile.write("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")


            
        print("hi:")
        print(ar)
        for x in range(len(testcase)):
            if (len(testcase))==0:
                finalfile.write(ar)
            print(result[x])
            finalfile.write(result[x])
            if "PASSED"  in result[x]:
                finalfile.write("Preason:None\n")
                finalfile.write("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
                print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            else:
                pass
            if "BLOCKED" in result[x]:
                if blockedreason:
                    finalfile.write("Block reason:" +blockreason[bbb])
                    finalfile.write("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
                    
                print(blockedreasoniter)
                print(blockreason[bbb])
                bbb+=1
            if "ERRORED" in result[x]:
                if ereason:
                    print(ereason[y])
                    finalfile.write(ereason[y])
                    finalfile.write("Errored-w reason:is given\n")

                elif errored:
                    finalfile.write("ERRORED REASON:"+errored[y])
                    print("__________________ERORO")
                    print( errorsectioniter)
                    finalfile.write("ERRORED FROM:"+errorsection[y])

                    
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
                if failedonly:
                    finalfile.write("FAIL DUE TO:"+failedonly[failed])
                elif pre:
                    finalfile.write("FAIL DUE TO:" +pre[preiter])
                    finalfile.write("Failed reason: none found\n")
                elif post:
                    finalfile.write("FAIL DUE TO:"+post[postiter])
                    finalfile.write("Failed reason:none found\n")
                
                elif sectionfailedreasonreason:
                    finalfile.write("FAIL DUE TO:"+sectionfailedreasonreason[failed])
                    finalfile.write("Failed reason:None found\n" )

                #elif secretfailedreason:
                 #   finalfile.write("Failure reason:"+secretfailedreasons[sfd])
                #else:
                 #   finalfile.write("UKNOWN SECTION \n")
                finalfile.write("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
                
                print("This testcase failed due to Section:",end='')
                if failedonly:
                    print(failedonly[failed],end='')
                else:
                    print("uknown\n")
                print("The reason why testcase failed is due to:",end='')
                if sectionfailedreason:
                    print(sectionfailedreason[failed])
                   # finalfile.write("Failed reason:"+secretfailedreasons[failed])
                else:
                    print("Failed reason:None found\n" )
                    print("UKNOWN SECTION\n")
                print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                failed+=1
                preiter+=1
                postiter+=1
                seciter+=1
                errorsectioniter+=1
                sfd+=1
            
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        finalfile.close()
                  
            
            
            
            