#the history makers makevideos.py
#concatenates, transcodes, moves videos for The History Makers

import os
import subprocess
import sys
import glob
import re
import argparse
import ConfigParser
from distutils import spawn
blah = 'foo'
#Context manager for changing the current working directory
class cd:
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
		os.chdir(self.savedPath)


#check that we have required software installed
def dependencies():
	depends = ['ffmpeg','ffprobe']
	for d in depends:
		if spawn.find_executable(d) is None:
			print "Buddy, you gotta install " + d
			sys.exit()
	return

def makelist(rawCaptures):
	try:
		flist = {}
		#regex = re.compile("*")#.
		
		accessionlist = []
		for dirs, subdirs, files in os.walk(rawCaptures): #walk through capture directory
			for f in files:
				ayear, acc, rest = f.split("_",2)
				if not acc in accessionlist:
					accessionlist.append(acc)
			for a in accessionlist:
				result = []
				for f in files:
					match = re.search(r"A\d{4}_" + acc + "_\d{3}_\d{3}.mov",f)#
					if match:
						result.append(match.group(0))
				flist[a] = result	
		print flist
	except:
		foo = blah
		#send email to THM staff
	return flist

def ffproces(flist):
	try:
		foo = blah
		#iterate thru flist
		#concatenate startfiles into endfile.mov
		#transcode endfiles
			#endfile.flv + HistoryMakers watermark
			#endfile.mpeg + timecode
			#endfile.mp4 + timecode
	except:
		foo = blah
		#send email to THM staff
	return

def hashmove(flist,sunnas,xendata,fmConfig):
	try:
		foo = blah
		#iterate thru flist
			#hashmove endfile.mov and endfile.mpeg to LTO
				#send SHA1 hashes to FileMaker
			#hashmove endfile.mp4 to SUNNAS/Proxy
				#send SHA1 hash to FileMaker
			#hashmove endfile.flv to "SUNNAS/Digital Archive"
				#send SHA1 hash to FileMaker
	except:
		foo = blah
		
		#send email to THM staff
	return

def playback(flist):
	foo = blah
	#iterate thru flist
		#ffplay endfile.mov
		#ffplay endfile.mpeg
		#ffplay endfile.mp4
		#ffplay endfile.flv
	return

def main():
	#initialize a buncha stuff
	config = ConfigParser.ConfigParser()
	config.read(os.path.join(os.getcwd(),"video-post-process-config.txt"))
	scriptRepo = config.get('global','scriptRepo')
	watermark = config.get('transcode','watermark')
	rawCaptures = config.get('transcode','rawCaptureDir')
	#fileMakerLoc = config.get('fileMaker','location')
	#fileMakerlogin = config.get('fileMaker','login')
	#fileMakerpwd = config.get('fileMaker','password')
	#fmConfig = [fileMakerLoc,fileMakerlogin,FileMakerpwd]
	emailaddy = config.get('global','email')
	sunnas = config.get('fileDestinations','sunnas')
	xendata = config.get('fileDestinations','xendata')
	
	#grab args fromCLI
	parser = argparse.ArgumentParser(description="concatenates, transcodes, hashmvoes videos")
	parser.add_argument("-i","--ignore",action="store_true",default=False,help="ignore policy errors")
	parser.add_argument("-s","--single",help="single mode, only process a single accession takes full canonical filename as arg e.g.A2016_012_034_056")
	
	args = vars(parser.parse_args())
	

	#make a list of things to work on
	flist = makelist(rawCaptures)

	#ffprocess
	#ffprocess(flist,watermark)

	#hashmove
	#hashmove(flist,sunnas,xendata)

	#playback
	#playback(flist)

	return

dependencies()
main()