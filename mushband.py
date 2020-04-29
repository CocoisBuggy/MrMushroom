import time
import psutil
import matplotlib.pyplot as plt
import numpy as np


log=open('log.txt', 'w+', encoding='utf8')
runtime=100
nparray=np.arange(runtime)

while True:
    log=open('log.txt', 'w+', encoding='utf8')
    runtime=100
    def main():
        old_value = 0

        perform=True
        performcount=0
        print('-- Cleared log.txt --')
        log.write('')

        while perform == True:
            new_value = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv

            if old_value:
                send_stat(new_value - old_value)
                log.write(str(new_value - old_value))
                if performcount<(runtime):
                    log.write(',')


            old_value = new_value
            performcount = performcount+1
            if performcount>runtime:
                print("--Break--")
                perform=False

                log.close()
                numlog=np.loadtxt(fname = 'log.txt',delimiter=',')
                loglist=numlog


                plt.ylabel('Data Logged (Bytes)')
                plt.plot(nparray, loglist, linewidth=2.0)
                plt.savefig('datausage.png')

            time.sleep(1)

    def convert_to_mbit(value):
        return value/1024./1024./1024.*8

    def send_stat(value):
        print ("%0.3f" % convert_to_mbit(value))

    main()
