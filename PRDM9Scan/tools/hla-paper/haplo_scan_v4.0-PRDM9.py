#!usr/bin/env python2.7
#hla_scan_v4.0.py

import sys
import os
import subprocess
import time
import shutil
from multiprocessing import Process
import random


#PROGRAMS
PROG_BAMTOFASTQ = "./ghaplo_scan"
PROG_BWA = "./bwa"
PROG_FILTEREDBAM = "./allele_count_cpu"
PROG_SAMTOOLS = "./samtools"
PROG_HLASCAN = "./haplo_scan_v4.0"

#INPUT
BAM_FILE = sys.argv[1]
#print 'BAM'+BAM_FILE
name=BAM_FILE.split('.')[0]
#print 'nomID'+ name
couverture=BAM_FILE.split('.')[5]
pop=BAM_FILE.split('.')[4]

GENE_FILE = sys.argv[2] #
OUTPUT_PATH = sys.argv[3]

ALIGN = True
if len(sys.argv) == 5:
	if sys.argv[4] == "1":
		ALIGN = False

if ALIGN == True:

	if os.path.isdir(OUTPUT_PATH):
		shutil.rmtree(OUTPUT_PATH)
	print 'out '+OUTPUT_PATH
	os.system('mkdir -p '+OUTPUT_PATH)




#DATABASE
FA_FILE = "../hla-ref-5gene/IMGT_HLA/"						#fixed
SGENE = ""			#fixed
GENE_634 = ""			#fixed
EXON_7255 = ""		#fixed
GENE_BOUND = "../hla-ref-5gene/exn/"

#PARAMETER
THREAD = 16
FASTQ_CLASS1 = OUTPUT_PATH + "/class1.fastq"
FASTQ_CLASS2 = OUTPUT_PATH + "/class2.fastq"
FASTQ_KIR = OUTPUT_PATH + "/kir.fastq"
FASTQ_OTHER = OUTPUT_PATH + "/"

CUTOFF_SCORE = "200"
CONSTANT = "30"
DEBUG = "1"


PER = 100

def Alignment(m_gene, m_Fa, m_Fastq):

	sam = OUTPUT_PATH + "/" + m_gene + "/" + m_Fa.split('.')[-2].split('/')[-1] + ".sam"
	bam =  OUTPUT_PATH + "/" + m_gene + "/" + m_Fa.split('.')[-2].split('/')[-1] + ".bam"

	#bwa-mem
	BAM_HEADER = "@RG\tID:foo\tLB:bar\tPL:illumina\tPU:illumina\tSM:bar"

	p = subprocess.Popen([PROG_BWA,'mem',m_Fa,m_Fastq,'-R',BAM_HEADER], stdout = subprocess.PIPE)#aligner
	with open(sam, "w") as f:
		for line in p.stdout.readlines():
			f.write(line)

	#sam to bam
	subprocess.call([PROG_SAMTOOLS, 'view', '-F', '0x800', '-bSh', sam, '-o', bam])#convertir

	#filtering
	subprocess.call([PROG_FILTEREDBAM, '-s', bam, '-x', m_Fa])

	#sorting
	sorted_bam = OUTPUT_PATH + "/" + m_gene + "/" + m_Fa.split('.')[-2].split('/')[-1] + ".sorted"
	sorted_bam_file = OUTPUT_PATH + "/" + m_gene + "/" + m_Fa.split('.')[-2].split('/')[-1] + ".sorted.bam"
	subprocess.call([PROG_SAMTOOLS, 'sort', bam + ".filtered", sorted_bam])
	subprocess.call([PROG_SAMTOOLS, 'index', sorted_bam_file])

	#remove
	subprocess.call(['rm', '-f', sam])
	subprocess.call(['rm', '-f', bam])





####################################### main ####################################
if __name__ == '__main__':
	#read gene list
	gene_list = []
	with open(GENE_FILE, "r") as f:
		for line in f.readlines():
			if line[0] == '#':
				continue
			gene_list.append(line.split()[0])

	if SGENE:
		sgene = []
		with open(SGENE, "r") as f:
			for line in f.readlines():
				sgene.append(line)

	if GENE_634:
		gene_634 = []
		with open(GENE_634, "r") as f:
			for line in f.readlines():
				gene_634.append(line)

	if EXON_7255:
		exon_7255 = []
		with open(EXON_7255, "r") as f:
			for line in f.readlines():
				exon_7255.append(line)

	if ALIGN == True:
		#Extract Reads in class1, class2
		t_start = time.time()

		idx = 0
		count = 0
		"""
		p = subprocess.Popen([PROG_BAMTOFASTQ,'-a',BAM_FILE,'-c','chr6','-s','29690241','-e','29695184'], stdout=subprocess.PIPE) #F
		with open(FASTQ_CLASS1, "w") as f:
			for line in p.stdout.readlines():
				rand = random.randint(1,100)
				if (idx%4 == 0 and rand <= PER) or count != 0:
					f.write(line)
					count = count+1
					if count == 4:	count = 0
				idx = idx+1

		p = subprocess.Popen([PROG_BAMTOFASTQ,'-a',BAM_FILE,'-c','chr6','-s','29794622','-e','29799159'], stdout=subprocess.PIPE) #G
		with open(FASTQ_CLASS1, "a") as f:
			for line in p.stdout.readlines():
				rand = random.randint(1,100)
				if (idx%4 == 0 and rand <= PER) or count != 0:
					f.write(line)
					count = count+1
					if count == 4:	count = 0
				idx = idx+1
		"""
		"""
		pe a garder
		p = subprocess.Popen([PROG_BAMTOFASTQ,'-a',BAM_FILE,'-c','chr6','-s','29909331','-e','29914232'], stdout=subprocess.PIPE) #A
		with open(FASTQ_CLASS1, "a") as f:
			for line in p.stdout.readlines():
				rand = random.randint(1,100)
				if (idx%4 == 0 and rand <= PER) or count != 0:
					f.write(line)
					count = count+1
					if count == 4:	count = 0
				idx = idx+1
		"""
		"""
		p = subprocess.Popen([PROG_BAMTOFASTQ,'-a',BAM_FILE,'-c','chr6','-s','30456309','-e','30461358'], stdout=subprocess.PIPE) #E
		with open(FASTQ_CLASS1, "a") as f:
			for line in p.stdout.readlines():
				rand = random.randint(1,100)
				if (idx%4 == 0 and rand <= PER) or count != 0:
					f.write(line)
					count = count+1
					if count == 4:	count = 0
				idx = idx+1


		"""
		"""
		pe a garder
		p = subprocess.Popen([PROG_BAMTOFASTQ,'-a',BAM_FILE,'-c','chr6','-s','31235946','-e','31240848'], stdout=subprocess.PIPE) #C
		with open(FASTQ_CLASS1, "a") as f:
			for line in p.stdout.readlines():
				rand = random.randint(1,100)
				if (idx%4 == 0 and rand <= PER) or count != 0:
					f.write(line)
					count = count+1
					if count == 4:	count = 0
				idx = idx+1


		p = subprocess.Popen([PROG_BAMTOFASTQ,'-a',BAM_FILE,'-c','chr6','-s','31321260','-e','31325935'], stdout=subprocess.PIPE) #B
		with open(FASTQ_CLASS1, "a") as f:
			for line in p.stdout.readlines():
				rand = random.randint(1,100)
				if (idx%4 == 0 and rand <= PER) or count != 0:
					f.write(line)
					count = count+1
					if count == 4:	count = 0
				idx = idx+1
		"""
		p = subprocess.Popen([PROG_BAMTOFASTQ,'-a',BAM_FILE,'-c','chr5','-s','23526233','-e','23527773'], stdout=subprocess.PIPE) #PRDM9
		with open(FASTQ_CLASS1, "a") as f:
			for line in p.stdout.readlines():
				rand = random.randint(1,100)
				if (idx%4 == 0 and rand <= PER) or count != 0:
					f.write(line)
					count = count+1
					if count == 4:	count = 0
				idx = idx+1

		"""
		p = subprocess.Popen([PROG_BAMTOFASTQ,'-a',BAM_FILE,'-c','chr6','-s','31370410','-e','31383916'], stdout=subprocess.PIPE)#MICA
		with open(FASTQ_CLASS1, "a") as f:
			for line in p.stdout.readlines():
				rand = random.randint(1,100)
				if (idx%4 == 0 and rand <= PER) or count != 0:
					f.write(line)
					count = count+1
					if count == 4:	count = 0
				idx = idx+1


		p = subprocess.Popen([PROG_BAMTOFASTQ,'-a',BAM_FILE,'-c','chr6','-s','31464971','-e','31478686'], stdout=subprocess.PIPE)#MICB
		with open(FASTQ_CLASS1, "a") as f:
			for line in p.stdout.readlines():
				rand = random.randint(1,100)
				if (idx%4 == 0 and rand <= PER) or count != 0:
					f.write(line)
					count = count+1
					if count == 4:	count = 0
				idx = idx+1


		#class 2
		p = subprocess.Popen([PROG_BAMTOFASTQ,'-a',BAM_FILE,'-c','chr6','-s','32406728','-e','32412687'], stdout=subprocess.PIPE)#DRA
		with open(FASTQ_CLASS2, "w") as f:
			for line in p.stdout.readlines():
				rand = random.randint(1,100)
				if (idx%4 == 0 and rand <= PER) or count != 0:
					f.write(line)
					count = count+1
					if count == 4:	count = 0
				idx = idx+1


		p = subprocess.Popen([PROG_BAMTOFASTQ,'-a',BAM_FILE,'-c','chr6','-s','32484516','-e','32499001'], stdout=subprocess.PIPE)#DRB5
		with open(FASTQ_CLASS2, "a") as f:
			for line in p.stdout.readlines():
				rand = random.randint(1,100)
				if (idx%4 == 0 and rand <= PER) or count != 0:
					f.write(line)
					count = count+1
					if count == 4:	count = 0
				idx = idx+1

		"""
		p = subprocess.Popen([PROG_BAMTOFASTQ,'-a',BAM_FILE,'-c','chr6','-s','32545868','-e','32558519'], stdout=subprocess.PIPE)#DRB1
		with open(FASTQ_CLASS2, "a") as f:
			for line in p.stdout.readlines():
				rand = random.randint(1,100)
				if (idx%4 == 0 and rand <= PER) or count != 0:
					f.write(line)
					count = count+1
					if count == 4:	count = 0
				idx = idx+1

		"""
		p = subprocess.Popen([PROG_BAMTOFASTQ,'-a',BAM_FILE,'-c','chr6','-s','32604236','-e','32611541'], stdout=subprocess.PIPE)#DQA1
		with open(FASTQ_CLASS2, "a") as f:
			for line in p.stdout.readlines():
				rand = random.randint(1,100)
				if (idx%4 == 0 and rand <= PER) or count != 0:
					f.write(line)
					count = count+1
					if count == 4:	count = 0
				idx = idx+1

		"""
		p = subprocess.Popen([PROG_BAMTOFASTQ,'-a',BAM_FILE,'-c','chr6','-s','32627013','-e','32635384'], stdout=subprocess.PIPE)#DQB1
		with open(FASTQ_CLASS2, "a") as f:
			for line in p.stdout.readlines():
				rand = random.randint(1,100)
				if (idx%4 == 0 and rand <= PER) or count != 0:
					f.write(line)
					count = count+1
					if count == 4:	count = 0
				idx = idx+1

		"""
		p = subprocess.Popen([PROG_BAMTOFASTQ,'-a',BAM_FILE,'-c','chr6','-s','32779992','-e','32785728'], stdout=subprocess.PIPE)#DOB
		with open(FASTQ_CLASS2, "a") as f:
			for line in p.stdout.readlines():
				rand = random.randint(1,100)
				if (idx%4 == 0 and rand <= PER) or count != 0:
					f.write(line)
					count = count+1
					if count == 4:	count = 0
				idx = idx+1


		p = subprocess.Popen([PROG_BAMTOFASTQ,'-a',BAM_FILE,'-c','chr6','-s','32795632','-e','32807010'], stdout=subprocess.PIPE)#TAP2
		with open(FASTQ_CLASS2, "a") as f:
			for line in p.stdout.readlines():
				rand = random.randint(1,100)
				if (idx%4 == 0 and rand <= PER) or count != 0:
					f.write(line)
					count = count+1
					if count == 4:	count = 0
				idx = idx+1


		p = subprocess.Popen([PROG_BAMTOFASTQ,'-a',BAM_FILE,'-c','chr6','-s','32812356','-e','32822413'], stdout=subprocess.PIPE)#TAP1
		with open(FASTQ_CLASS2, "a") as f:
			for line in p.stdout.readlines():
				rand = random.randint(1,100)
				if (idx%4 == 0 and rand <= PER) or count != 0:
					f.write(line)
					count = count+1
					if count == 4:	count = 0
				idx = idx+1


		p = subprocess.Popen([PROG_BAMTOFASTQ,'-a',BAM_FILE,'-c','chr6','-s','32901748','-e','32909584'], stdout=subprocess.PIPE)#DMB
		with open(FASTQ_CLASS2, "a") as f:
			for line in p.stdout.readlines():
				rand = random.randint(1,100)
				if (idx%4 == 0 and rand <= PER) or count != 0:
					f.write(line)
					count = count+1
					if count == 4:	count = 0
				idx = idx+1


		p = subprocess.Popen([PROG_BAMTOFASTQ,'-a',BAM_FILE,'-c','chr6','-s','32915641','-e','32921813'], stdout=subprocess.PIPE)#DMA
		with open(FASTQ_CLASS2, "a") as f:
			for line in p.stdout.readlines():
				rand = random.randint(1,100)
				if (idx%4 == 0 and rand <= PER) or count != 0:
					f.write(line)
					count = count+1
					if count == 4:	count = 0
				idx = idx+1


		p = subprocess.Popen([PROG_BAMTOFASTQ,'-a',BAM_FILE,'-c','chr6','-s','32973615','-e','32978313'], stdout=subprocess.PIPE)#DOA
		with open(FASTQ_CLASS2, "a") as f:
			for line in p.stdout.readlines():
				rand = random.randint(1,100)
				if (idx%4 == 0 and rand <= PER) or count != 0:
					f.write(line)
					count = count+1
					if count == 4:	count = 0
				idx = idx+1


		p = subprocess.Popen([PROG_BAMTOFASTQ,'-a',BAM_FILE,'-c','chr6','-s','33035427','-e','33042347'], stdout=subprocess.PIPE)#DPA1
		with open(FASTQ_CLASS2, "a") as f:
			for line in p.stdout.readlines():
				rand = random.randint(1,100)
				if (idx%4 == 0 and rand <= PER) or count != 0:
					f.write(line)
					count = count+1
					if count == 4:	count = 0
				idx = idx+1


		p = subprocess.Popen([PROG_BAMTOFASTQ,'-a',BAM_FILE,'-c','chr6','-s','33042819','-e','33055015'], stdout=subprocess.PIPE)#DPB1
		with open(FASTQ_CLASS2, "a") as f:
			for line in p.stdout.readlines():
				rand = random.randint(1,100)
				if (idx%4 == 0 and rand <= PER) or count != 0:
					f.write(line)
					count = count+1
					if count == 4:	count = 0
				idx = idx+1



		#KIR
		p = subprocess.Popen([PROG_BAMTOFASTQ,'-a',BAM_FILE,'-c','chr19','-s','55280303','-e','55296265'], stdout=subprocess.PIPE)#KIR2DL1
		with open(FASTQ_KIR, "w") as f:
			for line in p.stdout.readlines():
				f.write(line)

		p = subprocess.Popen([PROG_BAMTOFASTQ,'-a',BAM_FILE,'-c','chr19','-s','55249011','-e','55264971'], stdout=subprocess.PIPE)#KIR2DL3
		with open(FASTQ_KIR, "a") as f:
			for line in p.stdout.readlines():
				f.write(line)

		p = subprocess.Popen([PROG_BAMTOFASTQ,'-a',BAM_FILE,'-c','chr19','-s','55314107','-e','55326566'], stdout=subprocess.PIPE)#KIR2DL4
		with open(FASTQ_KIR, "a") as f:
			for line in p.stdout.readlines():
				f.write(line)

		p = subprocess.Popen([PROG_BAMTOFASTQ,'-a',BAM_FILE,'-c','chr19','-s','55265475','-e','55279823'], stdout=subprocess.PIPE)#KIR2DP1
		with open(FASTQ_KIR, "a") as f:
			for line in p.stdout.readlines():
				f.write(line)

		p = subprocess.Popen([PROG_BAMTOFASTQ,'-a',BAM_FILE,'-c','chr19','-s','55343220','-e','55360398'], stdout=subprocess.PIPE)#KIR2DS4
		with open(FASTQ_KIR, "a") as f:
			for line in p.stdout.readlines():
				f.write(line)

		p = subprocess.Popen([PROG_BAMTOFASTQ,'-a',BAM_FILE,'-c','chr19','-s','55326956','-e','55342730'], stdout=subprocess.PIPE)#KIR3DL1
		with open(FASTQ_KIR, "a") as f:
			for line in p.stdout.readlines():
				f.write(line)

		p = subprocess.Popen([PROG_BAMTOFASTQ,'-a',BAM_FILE,'-c','chr19','-s','55360931','-e','55379186'], stdout=subprocess.PIPE)#KIR3DL2
		with open(FASTQ_KIR, "a") as f:
			for line in p.stdout.readlines():
				f.write(line)

		p = subprocess.Popen([PROG_BAMTOFASTQ,'-a',BAM_FILE,'-c','chr19','-s','55235002','-e','55248563'], stdout=subprocess.PIPE)#KIR3DL3
		with open(FASTQ_KIR, "a") as f:
			for line in p.stdout.readlines():
				f.write(line)

		p = subprocess.Popen([PROG_BAMTOFASTQ,'-a',BAM_FILE,'-c','chr19','-s','55296807','-e','55302770'], stdout=subprocess.PIPE)#KIR3DP1
		with open(FASTQ_KIR, "a") as f:
			for line in p.stdout.readlines():
				f.write(line)

		p = subprocess.Popen([PROG_BAMTOFASTQ,'-a',BAM_FILE,'-c','NT_113949.1','-s','20940','-e','36938'], stdout=subprocess.PIPE)#KIR2DL2
		with open(FASTQ_KIR, "a") as f:
			for line in p.stdout.readlines():
				f.write(line)

		p = subprocess.Popen([PROG_BAMTOFASTQ,'-a',BAM_FILE,'-c','NT_113949.1','-s','85746','-e','96742'], stdout=subprocess.PIPE)#KIR2DL5A
		with open(FASTQ_KIR, "a") as f:
			for line in p.stdout.readlines():
				f.write(line)

		p = subprocess.Popen([PROG_BAMTOFASTQ,'-a',BAM_FILE,'-c','NT_187636.1','-s','165925','-e','176937'], stdout=subprocess.PIPE)#KIR2DL5B
		with open(FASTQ_KIR, "a") as f:
			for line in p.stdout.readlines():
				f.write(line)

		p = subprocess.Popen([PROG_BAMTOFASTQ,'-a',BAM_FILE,'-c','NT_113949.1','-s','114112','-e','129940'], stdout=subprocess.PIPE)#KIR2DS1
		with open(FASTQ_KIR, "a") as f:
			for line in p.stdout.readlines():
				f.write(line)
		p = subprocess.Popen([PROG_BAMTOFASTQ,'-a',BAM_FILE,'-c','NT_113949.1','-s','130468','-e','146120'], stdout=subprocess.PIPE)#KIR2DS2
		with open(FASTQ_KIR, "a") as f:
			for line in p.stdout.readlines():
				f.write(line)
		p = subprocess.Popen([PROG_BAMTOFASTQ,'-a',BAM_FILE,'-c','NT_187636.1','-s','149364','-e','165521'], stdout=subprocess.PIPE)#KIR2DS3
		with open(FASTQ_KIR, "a") as f:
			for line in p.stdout.readlines():
				f.write(line)
		p = subprocess.Popen([PROG_BAMTOFASTQ,'-a',BAM_FILE,'-c','NT_113949.1','-s','97146','-e','113480'], stdout=subprocess.PIPE)#KIR2DS5
		with open(FASTQ_KIR, "a") as f:
			for line in p.stdout.readlines():
				f.write(line)
		p = subprocess.Popen([PROG_BAMTOFASTQ,'-a',BAM_FILE,'-c','NT_113949.1','-s','86513','-e','88548'], stdout=subprocess.PIPE)#KIR3DP1
		with open(FASTQ_KIR, "a") as f:
			for line in p.stdout.readlines():
				f.write(line)
		p = subprocess.Popen([PROG_BAMTOFASTQ,'-a',BAM_FILE,'-c','NT_113949.1','-s','69108','-e','84979'], stdout=subprocess.PIPE)#KIR3DS1
		with open(FASTQ_KIR, "a") as f:
			for line in p.stdout.readlines():
				f.write(line)
		"""

		t_end = time.time()
		print "(",t_end-t_start,"sec)", "DONE: Extract Reads in class1, class2 and KIR"

	#for each HLA-gene
	t_start = time.time()
	final_out = []
#	final_out.append("======================= HAPLO_scan v4.0 ========================\n")

	for gene in gene_list:
		BAM_LIST = OUTPUT_PATH + "/" + gene + ".list"
		bound_chr = []
		bound_s_pos = []
		bound_e_pos = []

		##########################################alignment####################################
		if ALIGN == True:
			os.mkdir(OUTPUT_PATH + "/" + gene)

			fastq = ""
			if gene == "A" or gene == "B" or gene == "C" or gene == "E" or gene == "F" or gene == "G"\
				or gene == "MICA" or gene == "MICB" or gene == "PRDM9":
				fastq = FASTQ_CLASS1
			elif gene == "DMA" or gene == "DMB" or gene == "DOA" or gene == "DOB" or gene == "DPA1"\
				or gene == "DPB1" or gene == "DQA1" or gene == "DQB1" or gene == "DRA" or gene == "DRB1"\
				or gene == "DRB5" or gene == "TAP1" or gene == "TAP2":
				fastq = FASTQ_CLASS2
			elif gene == "KIR2DL1" or gene == "KIR2DL2" or gene == "KIR2DL3" or gene == "KIR2DL4"\
				or gene == "KIR2DL5A" or gene == "KIR2DL5B" or gene == "KIR2DP1" or gene == "KIR2DS1"\
				or gene == "KIR2DS2" or gene == "KIR2DS3" or gene == "KIR2DS4" or gene == "KIR2DS5"\
				or gene == "KIR3DL1" or gene == "KIR3DL2" or gene == "KIR3DL3" or gene == "KIR3DP1"\
				or gene == "KIR3DS1":
				fastq = FASTQ_KIR

			else:
				#search gene list
				if GENE_634:
					for line in gene_634:
						if gene == line[:-1]:
							IsGeneExist = True
							break
				else:
					IsGeneExist = False

				if EXON_7255:
					for line in exon_7255:
						item = line.split()
						if gene == item[0] + "_" + item[1]:
							IsExonExist = True
							break
				else:
					IsExonExist = False



				if IsGeneExist == True:
					#search sgene boundary
					sgene_chr = ""
					sgene_s_pos = ""
					sgene_e_pos = ""
					for line in sgene:
						item = line.split()
						if item[4] == gene:
							sgene_chr = item[0]
							sgene_s_pos = item[1]
							sgene_e_pos = item[2]
							break

					#create fastq file
					p = subprocess.Popen([PROG_BAMTOFASTQ,'-a',BAM_FILE,'-c',sgene_chr,'-s',sgene_s_pos,\
					'-e',sgene_e_pos], stdout=subprocess.PIPE)

					with open(FASTQ_OTHER + gene + ".fastq", "w") as f:
						for line in p.stdout.readlines():
							f.write(line)
					fastq = FASTQ_OTHER + gene + ".fastq"

				elif IsExonExist == True:
					#search exon boundary
					exon_chr = ""
					exon_s_pos = ""
					exon_e_pos = ""
					for line in exon_7255:
						item = line.split()
						if gene == item[0] + "_" + item[1]:
							exon_chr = item[2]
							exon_s_pos = str(int(item[3]) - 500)
							exon_e_pos = str(int(item[4]) + 500)
							break

					#create fastq file
					p = subprocess.Popen([PROG_BAMTOFASTQ,'-a',BAM_FILE,'-c',exon_chr,'-s',exon_s_pos,\
					'-e',exon_e_pos], stdout=subprocess.PIPE)

					with open(FASTQ_OTHER + gene + ".fastq", "w") as f:
						for line in p.stdout.readlines():
							f.write(line)
					fastq = FASTQ_OTHER + gene + ".fastq"


				else:
					print "Wrong input :", gene
					exit(0)


			#find fa file
			fa_file = FA_FILE + gene + "/"
			p = subprocess.Popen(['find', fa_file, '-name', '*.fa'], stdout = subprocess.PIPE)
			fa_list = []
			for line in p.stdout.readlines():
				fa_list.append(line[:-1])

			#BWA-mem
			bam_cnt = 0
			proc_alignment = []
			idx_start = 0

			for line in fa_list:
				proc = Process(target = Alignment, args=(gene, line, fastq))
				proc_alignment.append(proc)

				bam_cnt = bam_cnt + 1
				if bam_cnt%THREAD == 0 or bam_cnt == len(fa_list):
					for line1 in proc_alignment[idx_start:bam_cnt]:
						line1.start()
					for line1 in proc_alignment[idx_start:bam_cnt]:
						line1.join()
					idx_start = bam_cnt

					print bam_cnt,
			print
			t_end = time.time()
			print "(", t_end-t_start, "sec)", "DONE: Alignment(.bam)."

		########################get bound####################################
		if gene == "A" or gene == "B" or gene == "C" or gene == "E" or gene == "F" or gene == "G"\
			or gene == "MICA" or gene == "MICB" or gene == "PRDM9"\
			or gene == "DMA" or gene == "DMB" or gene == "DOA" or gene == "DOB" or gene == "DPA1"\
			or gene == "DPB1" or gene == "DQA1" or gene == "DQB1" or gene == "DRA" or gene == "DRB1"\
			or gene == "DRB5" or gene == "TAP1" or gene == "TAP2"\
			or gene == "KIR2DL1" or gene == "KIR2DL2" or gene == "KIR2DL3" or gene == "KIR2DL4"\
			or gene == "KIR2DL5A" or gene == "KIR2DL5B" or gene == "KIR2DP1" or gene == "KIR2DS1"\
			or gene == "KIR2DS2" or gene == "KIR2DS3" or gene == "KIR2DS4" or gene == "KIR2DS5"\
			or gene == "KIR3DL1" or gene == "KIR3DL2" or gene == "KIR3DL3" or gene == "KIR3DP1"\
			or gene == "KIR3DS1":

			#get bound
			with open(GENE_BOUND + gene + ".exn", "r") as f:
				for line in f.readlines():
					item = line.split()
					bound_chr.append(item[1])
					bound_s_pos.append(item[2])
					bound_e_pos.append(item[3])
		else:
				#search gene list
				if GENE_634:
					for line in gene_634:
						if gene == line[:-1]:
							IsGeneExist = True
							break
				else:
					IsGeneExist = False

				if EXON_7255:
					for line in exon_7255:
						item = line.split()
						if gene == item[0] + "_" + item[1]:
							IsExonExist = True
							break
				else:
					IsExonExist = False

				if IsGeneExist == True:
					#get bound
					with open(GENE_BOUND + gene + ".exn", "r") as f:
						for line in f.readlines():
							item = line.split()
							bound_chr.append(item[1])
							bound_s_pos.append(item[2])
							bound_e_pos.append(item[3])
				elif IsExonExist == True:
					for line in exon_7255:
						item = line.split()
						if gene == item[0] + "_" + item[1]:
							bound_chr.append(item[2])
							bound_s_pos.append(item[3])
							bound_e_pos.append(item[4])
							break
		#calcuate depth
		depth_ave = 0.0
		pos_len = 0
		for i in range(0, len(bound_chr)):
			p = subprocess.Popen([PROG_SAMTOOLS, 'depth', BAM_FILE, '-r', bound_chr[i] + ':' + bound_s_pos[i] + '-'\
			+ bound_e_pos[i]], stdout = subprocess.PIPE)

			for line in p.stdout.readlines():
				item = line.split()
				if len(item) == 3:
					depth_ave = depth_ave + float(item[2])
			pos_len = pos_len + (int(bound_e_pos[i]) - int(bound_s_pos[i]) + 1)
		depth_ave = depth_ave/float(pos_len)

		print depth_ave

		#Create filtered Bam list file
		p = subprocess.Popen(['find', OUTPUT_PATH + "/"+gene+ "/", '-name', '*.sorted.bam'], stdout = subprocess.PIPE)
		bam_list = []
		for line in p.stdout.readlines():
			bam_list.append(line)
		with open(BAM_LIST, "w") as f:
			for line in bam_list:
				f.write(line)


		#Determine HLA types
		p = subprocess.Popen([PROG_HLASCAN, BAM_LIST, gene, CUTOFF_SCORE, CONSTANT, DEBUG], stdout = subprocess.PIPE)
		temp_out = ""
		for line in p.stdout.readlines():
			item = line.split()
			if len(item) == 0:	continue
			if item[0] == "HAPLO-Region":
				temp_out = item[2]
			if item[0] == "[Allele":
				temp_out = temp_out + "\t" + item[2]
				depth_ratio = 0.0
				for i in range(3, len(item)):
					if depth_ave != 0:
						depth_ratio = depth_ratio + (float(item[3].split('_')[1]) / depth_ave)
					else:
						depth_ratio = 0
				if depth_ratio != 0:
					depth_ratio = depth_ratio / float(len(item) - 2) * 2.5
				if depth_ratio > 1:
					depth_ratio = 1
				temp_out = temp_out + "\t" + str(depth_ratio)

			if item[0] == "[Allele(Low)":
				temp_out = temp_out + "\t(" + item[2]
				depth_ratio = 0.0
				for i in range(3, len(item)):
					if depth_ave != 0:
						depth_ratio = depth_ratio + (float(item[3].split('_')[1]) / depth_ave)
					else:
						depth_ratio = 0
				if depth_ratio != 0:
					depth_ratio = depth_ratio / float(len(item) - 2) * 2.5
				if depth_ratio > 1:
					depth_ratio = 1
				temp_out = temp_out + "\t" + str(depth_ratio) + ")"

		temp_out = temp_out + "\n"
		final_out.append(temp_out)

	p = subprocess.call(['rm', '-f', OUTPUT_PATH + "/Report"])

	with open(OUTPUT_PATH + "/Report", "w") as f:
		for line in final_out:
			f.write(name + '\t'+ couverture + '\t' + pop + '\t' + line)
