import os
import csv

# initializing the variables
total_votes=0
candidatewise_votes=0
curr_candidate=''
candidate=[]
candidate_vote=[]
candidate_vote_pct=[]

candidate_dict={}

# defining the path of the input csv file
pypoll_csv_path=os.path.join('Resources','election_data.csv')


with open(pypoll_csv_path) as pypoll_csv_file:
    csv_reader=csv.reader(pypoll_csv_file)
    # print(csv_reader)
    # removing the header from the dataset
    header=next(csv_reader)
    # print(header)
    # looping through the rows
    for row in csv_reader:
        total_votes+=1
        if row[2]  in candidate:
            # checking the Candidate list for the candidate name if exists then adding vote count +1 for the candidate's index value
            # candidatewise_votes=1
            candidate_index=candidate.index(row[2])
            candidate_vote[candidate_index]+=1
        else:
             # else adding the candidate name into the Candidate list and then initializing vote count to 1 for the candidate's index value
            candidate.append(row[2])
            candidate_vote.append(1)
        
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {total_votes}")
print(f"-------------------------")

# fetching the candidate and the respective vote
for index,value in enumerate(candidate):
    print(f"{value}: {round((candidate_vote[index]/total_votes)*100,3)}% ({candidate_vote[index]})")
    

print(f"-------------------------")
print(f"Winner: {candidate[candidate_vote.index(max(candidate_vote))]}")
print(f"-------------------------")            


# defining the output file path
output_path=os.path.join('analysis','output_election_data.txt')
# writing the files
# opening the file in write mode
with open(output_path,'w') as writefile:
    writefile.write("Election Results\n")
    writefile.write("--------------------------\n")
    writefile.write(f"Total Votes: {total_votes}\n")
    writefile.write(f"--------------------------\n")
    for index,value in enumerate(candidate):
        writefile.write(f"{value}: {round((candidate_vote[index]/total_votes)*100,3)}% ({candidate_vote[index]})\n")

    writefile.write(f"-------------------------\n")
    writefile.write(f"Winner: {candidate[candidate_vote.index(max(candidate_vote))]}\n")
    writefile.write(f"-------------------------\n")