import glob

fout=open("C:\\Projects\\MetOffice.csv","a")
# first file:
for line in open(glob.glob("C:\\Projects\\WeatherData\\output_20160913_????.csv")[0]):
    fout.write(line)
# now the rest:
for num in range(14,20):
    f = open(glob.glob("C:\\Projects\\WeatherData\\output_201609"+str(num)+"_????.csv")[0])
    f.next() # skip the header
    for line in f:
         fout.write(line)
    f.close()
fout.close()