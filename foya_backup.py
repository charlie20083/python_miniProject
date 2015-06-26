import os, time
from ftplib import FTP

def recursive (atpath,filename,istarget) :
    i=-1
    print atpath
    
    try:
        list_file=os.listdir(atpath)
        while i+1<len(list_file):
#           time.sleep(1)
            i=i+1
#           print '1 = ' + str(i) + ' list_file_max = ' + str(len(list_file))
#           print 'list_file[0:4] = ' + list_file[i][0:4]
#           print 'istarget = ' + str(list_file[i][0:4]=='vmwa' or list_file[i][0:4]=='test')
            recursive(atpath+'/'+list_file[i],list_file[i],list_file[i][0:4]=='vmwa' or list_file[i][0:4]=='vmwa')
#       print i
    except OSError:
        if istarget:
        	print 'Target found!'
#               print 'atpath = ' + atpath + ', filename = ' + filename
                os.system('cp ' + atpath + ' ./backup/' + filename)
        
#       print atpath + ' is not a folder'
        
    

#   expect OSError:
#           return

if __name__ == "__main__":
    os.system('mkdir backup')

    recursive('/tmp','tmp',0)

    os.system('tar -zcvf tmpbackup_' + time.strftime("%Y%m%d") + '.tar.gz ./backup')

    ftp = FTP('csie0.cs.ccu.edu.tw')
    ftp.login('ccy99u','edde4969')
#   ftp.mkd('backup')
    ftp.cwd('backup')
    fup = open('./tmpbackup_' + time.strftime("%Y%m%d") + '.tar.gz', "rb")
    ftp.storbinary('STOR ./tmpbackup_' + time.strftime("%Y%m%d") + '.tar.gz' , fup)
    fup.close()
    ftp.quit()
