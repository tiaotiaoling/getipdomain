#coding=utf-8
#author:跳跳龙
import optparse
global get,newfilename

def getdomain(filename):
	string=filename
	f=open(string,'r')
	
	while True:
		filecontent=f.readline()
		if filecontent:
			#print filecontent.split()[0]
			filelist.append(filecontent.split()[get])
		else:
			break	
	f.close()	

if __name__ == '__main__':
	parser=optparse.OptionParser('usage : program [option] targetfile')
	parser.add_option('-f','--file',help="the name of txt")
	parser.add_option('-p','--ip',help="if you want to get ip,like -p 1")
	parser.add_option('-d','--domain',help="if you want get domain,like -d 1")
	parser.add_option('-n','--newfile',help="the name of new file")
	(options,args)=parser.parse_args()
	#parser.print_help()
	filename=options.file
	ip=options.ip
	if ip:
		get=1
	domain=options.domain
	if domain:
		get=0
		
	newfilename=str(options.newfile)
	#print type(newfile)
	filelist=[]
	getdomain(filename)
	print filelist
	#print len(filelist)
	for i in range(len(filelist)):
		newfile=open(newfilename,'a')
		newfile.write(filelist[i]+'\n')
	newfile.close()
