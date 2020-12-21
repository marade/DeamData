
    
PATH_TO_FILE = ""  #create string with directory path

with open(PATH_TO_FILE+"", 'r', 0) as referenceCSV: #open reference fasta
    reference =  referenceCSV.readlines()[1]


with open(PATH_TO_FILE+"", 'r', 0) as untreatedContext: #open csv file contaning variants data
    Context =  untreatedContext.readlines()[1:]


#function to extract position

def parse_context(position_df):
    position_str = position_df.split(",")[1]
    position = int(position_str)
    sequence = reference[position - 24: position + 23] #values indicate range of bases to be selected 
    return(position_str,sequence)


for i in Context:
	output = parse_context(i)
	header = ">"+output[0]
	sequence2 = output[1]+"\n"
	print(header, sequence2)
	fasta_file = open(PATH_TO_FILE+"output.fasta", 'a+')
	fasta_file.write(header)
	fasta_file.write(sequence2)

