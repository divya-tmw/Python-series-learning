#variable length keyword arguements

def student(**details):
    for key,value in details.items():
        print(key,"=",value)


student(name="Divya",age=19,city="Mumbai",course="bsc it")