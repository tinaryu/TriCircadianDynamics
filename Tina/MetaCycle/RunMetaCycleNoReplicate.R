library(MetaCycle)

group = "nfil3_WT"

infile = paste("ZK4grp_fpkm_extracted/",group,".txt", sep="")
outdir = paste(group,"_MetaCycleOutput",sep="")

#timepoints = seq(2,20,by=6) #2 8 14 20
timepoints = seq(0,20,by=4) # 0 4 8 12 16 20

meta2d(infile = infile, filestyle = "txt", outdir=outdir,timepoints = timepoints)

#Warning: the input 'minper' is not suitable for JTK, it was reset as  18 
#Warning: the input 'maxper' is not suitable for JTK, it was reset as  24 