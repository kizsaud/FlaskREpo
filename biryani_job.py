'''

pyats run job biryani_job.py \
--testbed-file biryani_testbed.yaml \
--datafile biryani_datafile.yaml \
--device_under_test 'a1' \
--operation 'reload_fast'
--target 'xe1763' \
--ixiacfg 'biryani_Topo1_XFSU_change_OSPF_March.ixncfg'


# xFSU on A1 
pyats run job biryani_job.py \
--testbed-file biryani_testbed.yaml \
--ixianame 'ixia1' \
--datafile biryani_datafile.yaml \
--device_under_test 'a1' \
--operation 'reload_fast' \
--target 'xe1763' \
--ixiacfg '/ws/shmandal-sjc/biryani/ixia/biryani_Topo1_XFSU_change_OSPF_March.ixncfg'

# To run the job:
# easypy ./job/gnmi_job.py -testbed_file ./etc/testbed.yaml --uut_name <device_name>
#
# To specify a specific testcase:
# easypy ./job/gnmi_job.py -testbed_file ./etc/testbed.yaml --uut_name <device_name> --testcase "['sanity_70_dean_2',]"

# 
pyats run job interface_loop_detect_via_template_job.py --testbed-file hpotta_testbed.yaml --datafile datafile.yaml

# Runs with datafile by default
pyats run job interface_loop_detect_via_template_job.py --testbed-file hpotta_testbed.yaml

# All plugins turned on 
pyats run job interface_loop_detect_via_template_job.py --testbed-file hpotta_testbed.yaml \
--btrace --crft \
--health-checks cpu memory logging core

# With explicit different --datafile
pyats run job interface_loop_detect_via_template_job.py --testbed-file hpotta_testbed.yaml --datafile datafile2.yaml

# Normal Run
pyats run job interface_loop_detect_via_template_job.py --testbed-file hpotta_testbed.yaml \
--btrace --crft \
--health-checks cpu memory logging core 

# With Clean
pyats run job interface_loop_detect_via_template_job.py --testbed-file hpotta_testbed.yaml \
--btrace --crft \
--health-checks cpu memory logging core \
--invoke-clean \
--clean-file clean-nyquist1.yaml \
--clean-device-image nyquist1-sjc24:/auto/tftp-sjc-users6/shmandal/cat9k_iosxe.BLD_V1612_THROTTLE_LATEST_20210715_230143.SSA.bin

'''

import os, argparse
from ats.easypy import run
from ats import topology
import os
from ats.easypy import run
from ats.datastructures.logic import And, Not, Or
import ast
import shutil 

def main (runtime):
    ''' 
    https://pubhub.devnetcloud.com/media/pyats/docs/easypy/behavior.html#runtime
    '''
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--testcase', dest='testcase', default="")
    parser.add_argument('--loops', dest='loops', required=False, default='1')
    parser.add_argument('--target', dest='target', required=True, default='xe1762')
    parser.add_argument('--device_under_test', dest='device_under_test', required=True, default='d1')
    parser.add_argument('--ixianame', dest='ixianame', required=True, default='ixia1')
    parser.add_argument('--ixiacfg', dest='ixiacfg', required=True, default='/ws/shmandal-sjc/biryani/ixia/biryani_D2.ixncfg')
    parser.add_argument('--operation', dest='operation', required=True, default='issu')
    parser.add_argument('--config_change_list', dest='config_change_list', type=str, required=False, default='', nargs="+")
    # --config_change_list "ospfv2_ospfv3_split"
    parser.add_argument('--access', dest='access', required=False, default='')
    parser.add_argument('--distribution', dest='distribution', required=False, default='')
    parser.add_argument('--core', dest='core', required=False, default='')

    args, unknown = parser.parse_known_args()

    testcase = str(args.testcase)
    if testcase:
        testcase = ast.literal_eval(testcase)

    loops = int(args.loops)
    target = str(args.target)
    device_under_test = str(args.device_under_test)
    ixianame = str(args.ixianame)
    ixiacfg = str(args.ixiacfg)
    operation = str(args.operation)
    #config_change = str(args.config_change)
    config_change_list = args.config_change_list
    access = str(args.access)
    distribution = str(args.distribution)
    core = str(args.core)

    print("Job file args")
    print(args)

    testscript = os.path.join('biryani.py')
    datafile = os.path.join('biryani_datafile.yaml')
    # Save datafile to runtime.directory so it is visible online
    datafile_path = os.path.join(runtime.directory, datafile)
    shutil.copyfile(datafile, datafile_path)  

    for loop_counter in range(0, loops):
        # Run All
        if testcase == '':
            run(testscript = testscript,
            loops=loops,
            target=target,
            device_under_test=device_under_test,
            ixianame=ixianame,
            ixiacfg=ixiacfg,
            operation=operation,
            config_change_list=config_change_list,
            access=access,
            distribution=distribution,
            core=core,
            datafile=datafile)	
        else:
            testcase_list = testcase
            uids = ['common_setup', ] + testcase_list + ['common_cleanup', ]
            run(testscript = testscript,
            loops=loops,
            target=target,
            device_under_test=device_under_test,
            ixianame=ixianame,
            ixiacfg=ixiacfg,
            operation=operation,
            config_change_list=config_change_list,
            access=access,
            distribution=distribution,
            core=core,
            datafile=datafile,
            uids=Or(*uids))
