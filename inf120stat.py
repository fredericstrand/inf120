import statistics as st

flyt_verdier = [9.81,3.14,2.71,1.14,1.73]

def mean(values):
    return(st.mean(values))

def std(values):
    return(st.stdev(values))

mean_result = mean(flyt_verdier)
std_result = std(flyt_verdier)

print("Mean:", mean_result)
print("Standard Deviation:", std_result)
