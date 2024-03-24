import paho.mqtt.publish as pub
import numpy as np
import os
import time

#We use time.sleep to avoid the error Python socket.error: [Errno 111] Connection refused
#Which happens when we try to connect to the server before initiating the server itself
#Time.sleep gives enough time to initiate the server first before connecting to it
#https://stackoverflow.com/questions/11585377/python-socket-error-errno-111-connection-refused
time.sleep(5)

def generate(median=90, err=10, outlier_err=30, size=1000, outlier_size=10):
    errs = err * np.random.rand(size) * np.random.choice((-1, 1), size)
    data = median + errs

    lower_errs = outlier_err * np.random.rand(outlier_size)
    lower_outliers = median - err - lower_errs

    upper_errs = outlier_err * np.random.rand(outlier_size)
    upper_outliers = median + err + upper_errs

    data = np.concatenate((data, lower_outliers, upper_outliers))
    np.random.shuffle(data)

    return data

if __name__ == '__main__':
    # TODO: retrieve the environment variable values for the mqtt broker and the desired rate for the publisher
    broker = os.environ.get('BROKER')
    rate = os.environ.get('RATE')
    topic = os.environ.get('TOPIC')
    
    print("broker:",broker)
    print("rate:",rate)
    print("topic:",topic)
    
    # TODO: use the generate function to create a pool of values for the publisher    
    values = generate()

    # TODO: publish a msg with a value randomly sampled from the data array. 
    # make it so that there's a 10% chance the value sent is null to emulate a sensor failure
    # you should filter these null values in Node Red       
    #i = 0  
    while(True):
        if np.random.random() < 0.1:
            pub.single(topic, None, hostname=broker)
        else:
            #i+=1
            rand_value = values[np.random.randint(0,values.size)]
            pub.single(topic,rand_value,hostname = broker)
        time.sleep(int(rate))