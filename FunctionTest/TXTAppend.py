
TestFile=open('/SegNet/segnet-fmri/test1.txt','w')
for i in range(1,241):
    TestFile.write("/home/philex/Data/ToPng/%d.png\n"%i)

print("success!")