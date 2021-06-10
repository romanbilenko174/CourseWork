from hostlist import expand_hostlist, collect_hostlist 
from subprocess import Popen, PIPE 
import sys, re, random 
def execute(cmd):
    p = Popen(cmd, stdout=PIPE, stdin=PIPE)
    stdout, stderr = p.communicate()
    return str(stdout).rstrip('\n') 
def getNodeStates():
    result = []
    cmd = ['sinfo','-Node','--partition=vm', '--Format','nodelist:12,statecompact:7,memory:7,allocmem:10,freemem:10,cpusstate:15,cpusload:10,gres:100']
    sinfo = execute(cmd)
    for line in sinfo.split('\n'):
	if line:
		result.append(line)
    return result

def getJobStates():
    result_jobs = []
    jobs_cmd = ['squeue']
    squeue = execute(jobs_cmd)
    for jobs_line in squeue.split('\n'):
        if jobs_line:
                result_jobs.append(jobs_line)
    return result_jobs

def getPCOCCImageList(user):
    result_image = []
    image_cmd = ['runuser','-l',user,'-c pcocc image list']
    pil = execute(image_cmd)
    for image_line in pil.split('\n'):
        if image_line:
                result_image.append(image_line)
    return result_image
def get_templates(user):
    result_templates = []
    templates_cmd = ['runuser','-l',user,'-c pcocc template list']
    pit = execute(templates_cmd)
    for templates_line in pit.split('\n'):
        if templates_line:
                result_templates.append(templates_line)
    return result_templates

def pcocc_import_image(user,PATH,image_name):
    result_upload = []
    import_command = "-c pcocc image import vm "+PATH+" user:"+image_name 
    upload_cmd = ['runuser','-l',user,command]
    piu = execute(upload_cmd)
    for upload_line in piu.split('\n'):
        if upload_line:
                result_upload.append(upload_line)
    remove_cmd = ['rm','-rf',PATH]
    print(remove_cmd)
    removal = execute(remove_cmd)
    return result_upload
def pcocc_remove_image(user,image_name):
    result_delete = []
    delete_command = "-c pcocc image delete  user:"+image_name
    delete_cmd = ['runuser','-l',user,delete_command]
    pid = execute(delete_cmd)
    for delete_line in pid.split('\n'):
        if delete_line:
                result_delete.append(delete_line)
    return result_delete

def pcocc_show(user,template_name):
    result_show = []
    show_command = "-c pcocc template show "+template_name
    show_cmd = ['runuser','-l',user,show_command]
    pis = execute(show_cmd)
    for show_line in pis.split('\n'):
        if show_line:
                result_show.append(show_line)
    return result_show

