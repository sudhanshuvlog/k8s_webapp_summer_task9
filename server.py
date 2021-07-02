#!/bin/python3
print("content-type:text/plain")
print("Access-Control-Allow-Origin: *")

print()
import os
import subprocess
import cgi
import spacy
data_taker=cgi.FieldStorage()
ch=data_taker.getvalue("speech")
#print(ch)
english=spacy.load('en_core_web_sm')
s1=english(ch)
array=[]
for i in s1:

    array.append(str(i))
if "launch" in ch:
    if "pods" in ch or "pod" in ch:
        i=0
        while i<len(array):
            if "deployment" in array[i] or "deployments" in array[i]:
                pod_name=array[i+1]
                print(pod_name)
                break
            i=i+1
        i=0
        while i<len(array):
            if "image" in a[i] or "Image" in array[i]:
                image_name=array[i+1]
                print(image_name)
                break
            i=i+1
        cmd="sudo kubectl create deployment "+deployment_name+" --image="+image_name
        output=subprocess.getoutput(cmd)
        print(output)

             
            
    elif "deployment" in ch:
        i=0
        while i<len(array):
            if "deployment" in array[i] or "deployments" in array[i]:
                deployment_name=array[i+1]
                print(deployment_name)
                break
            i=i+1
        i=0
        while i<len(array):
            if "image" in array[i] or "Image" in array[i]:
                image_name=array[i+1]
                print(image_name)
                break
            i=i+1        
        cmd="sudo kubectl create deployment "+deployment_name+" --image="+image_name
        output=subprocess.getoutput(cmd)
        print(output)
    
elif "delete" in ch:
    #print("delete")
    if "deployment" in ch:
       # print("delete deployment")
        i=0
        while i<len(array):
           # print(i)
            if "deployments" in array[i] or "deployment" in array[i]:
                deployment_name=array[i+1]
                print(deployment_name)
                break
            i=i+1
    cmd="sudo kubectl delete deployment "+ deployment_name
    output=subprocess.getoutput(cmd)
    print(output)
        
elif "scale" in ch:
    i=0
    while i<len(array):
        if "replica" in array[i] or "Replica" in array[i]:
            replica_no=array[i+1]
            print(replica_no)
        i=i+1
    i=0
    while i<len(array):
        if "deployment" in array[i] or "deployments" in array[i]:
            deployment_name=array[i+1]
            print(deployment_name)
        i=i+1
            
    cmd="sudo kubectl scale deployment "+ deployment_name +" --replicas="+replica_no
    output=subprocess.getoutput(cmd)
    print(output)
            
elif "expose" in ch:
    i=0
    while i<len(array):
        if "port" in array[i] or "Port" in array[i]:
            port_number=array[i+1]
            print(port_number)
            break
        i=i+1
    i=0
    while i<len(array):
        if "deployments" in array[i] or "deployment" in array[i]:
            deployment_name=array[i+1]
            print(deployment_name)
            break
        i=i+1
    cmd="sudo kubectl expose deployment "+ deployment_name +" --port="+port_number+" --type=NodePort"
    output=subprocess.getoutput(cmd)
    print(output)
        
elif "get" in ch or "show" in ch :
    i=0
    while i<len(array):
        if "pods" in ch or "pod" in ch:
            output=subprocess.getoutput("sudo kubectl get pods")
            print(output)
            break
        i=i+1
    i=0
    while i<len(array):
        if "deployment" in ch or "Deployments" in ch or "deployments" in ch:
            output=subprocess.getoutput("sudo kubectl get deployment") # --kubeconfig admin.conf
            #output=subprocess.getoutput("sudo docker ps -a")
            print(output)
            break
        i=i+1
    i=0
    while i<len(array):
        if "svc" in ch or "service" in ch:
            output=subprocess.getoutput("sudo kubectl get svc")
            print(output)
            break
        i=i+1

elif "describe" in ch:
    i=0
    while i<len(array):
        if "deployments" in array[i] or "deployment" in array[i]:
            deployment_name=array[i+1]
            print(deployment_name)
            break
        i=i+1
    cmd="sudo kubectl describe deployment "+ deployment_name
    output=subprocess.getoutput(cmd)
    print(output)


else:
    print("Wrong Command entered!!!")
