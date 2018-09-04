
totalvote = 0
cands = []
votebycand = []

fname = '/Users/anikarahman/Desktop/Bootcamp_HW/HW3/election_data.csv'
import csv

with open(fname) as f:
    csvreader = csv.reader(f)

    for row in csvreader:
	    if (row[0] != "Voter ID"):
	    	totalvote += 1

	    	if (row[2]  in cands):
	    		votebycand[cands.index(row[2])] += 1

	    	else:
	    		cands.append(row[2])
	    		votebycand.append(1)



winner = cands[votebycand.index(max(votebycand))]
percents = [i*100/totalvote for i in votebycand]


# print("Election Results")
# print("-------------------------")
# print(f"Total Votes: {totalvote}")
# print("-------------------------")

# for j in range(0,len(cands)) :

# 	print(f"{cands[j]}: {round(percents[j])}.000% ({votebycand[j]})")

# print("-------------------------")
# print(f"Winner: {winner}")
# print("-------------------------")



f = open('PyPollResults.txt','w')

print("Election Results", file=f)
print("-------------------------", file=f)
print(f"Total Votes: {totalvote}", file=f)
print("-------------------------", file=f)

for j in range(0,len(cands)) :

	print(f"{cands[j]}: {round(percents[j])}.000% ({votebycand[j]})", file=f)

print("-------------------------", file=f)
print(f"Winner: {winner}", file=f)
print("-------------------------", file=f)
f.close()


f = open('PyPollResults.txt','r')
print(f.read())
f.close()
