#Create a list the contains Chula faculty number
faculty_num = ["01","02","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","51","53","55","58"]

#Input the code as a string
code = str(input())

#Check if the code is in the list
#if yes, output "OK" but if not, output "Error" 
if(code in faculty_num):
    print("OK")
else:
    print("Error")