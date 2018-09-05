totalmonths = 0
total_profloss = 0
months = []
diff = []
data = []



fname = '/Users/anikarahman/Desktop/Bootcamp_HW/HW3/budget_data.csv'
import csv

with open(fname) as f:
    csvreader = csv.reader(f)
    next(csvreader, None)

    for row in csvreader:

	    totalmonths += 1
	    data.append(int(row[1]))
	    months.append(row[0])
	    


diff = [data[i] - data[i-1] for i in range(1,len(data))]

avgchg = (data[-1] - data[0])/(totalmonths-1)
total_profloss = sum(data)



f = open('PyBankResults.txt','w')
print("Financial Analysis", file=f)    	
print("----------------------------", file=f)
print(f"Total Months: {totalmonths}", file=f)
print(f"Total: ${total_profloss}", file=f)
print(f"Average  Change: ${round(avgchg,2)}", file=f)
print(f"Greatest Increase in Profits: {months[diff.index(max(diff))+1]} (${max(diff)})", file=f)
print(f"Greatest Decrease in Profits: {months[diff.index(min(diff))+1]} (${min(diff)})", file=f)

f.close()
f = open('PyBankResults.txt','r')
print(f.read())
f.close()



# print("Financial Analysis")    	
# print("----------------------------")
# print(f"Total Months: {totalmonths}")
# print(f"Total: ${total_profloss}")
# print(f"Average  Change: ${round(avgchg,2)}")
# print(f"Greatest Increase in Profits: {months[diff.index(max(diff))+1]} (${max(diff)})")
# print(f"Greatest Decrease in Profits: {months[diff.index(min(diff))+1]} (${min(diff)})")


