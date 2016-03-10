

import os  
def generateCSV(target, directory):
    header = 'x,y,major,minor,pressure,orientation,instance,instance, user'+ '\n'
    targetfile = open(target, 'w')
    targetfile.write(header)
    for user in os.listdir(directory):
        
        if user != '.DS_Store':
            for instance in os.listdir(directory+'/'+user):
                if instance != '.DS_Store':
                    f = open(directory+'/'+user+'/'+instance+'/touch.csv', "r")
                    lines = f.readlines()
                    targetfile.write(lines[1].strip().replace('\n', '')+',' +instance+','+user + '\n')
                    f.close()
    targetfile.close()
    print('generated:'+target)

#generate traindata csv
generateCSV('/Users/sbapodara/Desktop/QeexoMLChallenge/task_data/train.csv','/Users/sbapodara/Desktop/QeexoMLChallenge/task_data/train' )               

#generate test data csv
generateCSV('/Users/sbapodara/Desktop/QeexoMLChallenge/task_data/test.csv','/Users/sbapodara/Desktop/QeexoMLChallenge/task_data/test' )               





