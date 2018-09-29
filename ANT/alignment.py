#!/usr/bin/python
import os
import json
def getpara():
    try:
    	with open(input("The path of the align json file:"),'r') as json_file:
    		print("json file read in correctly")
    except IOError as err:
    	print("File Error:"+str(err))
    	return -1
    else:
    	try:
    		parameter = json.load(json_file)
    	except ValueError as e:
    		print("json file content error")
    		return -2
    	else:
    		return parameter

def alignment_STAR():
	parameter = getpara()
	if not isinstance(parameter,int):
		
		cell_dir = parameter["CELL_DIR"]
		#mkdir for each output and then run STAR
		star_outpath = parameter["outFileNamePrefix"]
		os.sys("mkdir"+star_outpath)
		for file in os.listdir(cell_dir):
			if os.path.splitext(file)[1] == ".gz":
				mkdir_cmd = "mkdir "+star_outpath+"STAR_out_"+file[10:21]+"/"
				os.sys(mkdir_cmd)

				star_cmd = parameter["STAR"]["star"]+" --runThreadN "+parameter["NUM_THREADS"]
							+" --genomeDir "+parameter["STAR"]["genomeDir"]
							+" --readFileIn "+cell_dir+file +" --readFilesCommand zcat"
							+" --genomeLoad LoadAndKeep"+" --quantMode TranscriptomeSAM GeneCounts"
							+" --outFileNamePrefix "+star_outpath+"STAR_out_"+file[10:21]+"/"
    			print("Running STAR alignment on cell "+file[10:21]+'\n')
    			os.sys(star_cmd)

    	print("STAR alignment finished\n")

def main():
	alignment_STAR()

if __name__ == '__main__':
	main()

    
