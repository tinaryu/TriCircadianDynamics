library(MetaCycle)

#nfil3_KO and nfil_WT were also ran
groups <- list("GF","hdac3_KO","hdac3_WT","nr1d1_WT","nr1d1_KO")

for (group in groups) {
infile = paste("ZK4grp_fpkm_extracted/replicated/expressed/",group,"_expressed.txt", sep="")
outdir = paste("MetaCycleOutput_rep/",group,"_MetaCycleOutput",sep="")

timepoints = seq(2,44,by=6) 
#timepoints = seq(0,44,by=4) #this is for nfil3 time points

meta2d(infile = infile, filestyle = "txt", outdir=outdir,timepoints = timepoints)
}

#Warning: the input 'minper' is not suitable for JTK, it was reset as  18 
#Warning: the input 'maxper' is not suitable for JTK, it was reset as  24 