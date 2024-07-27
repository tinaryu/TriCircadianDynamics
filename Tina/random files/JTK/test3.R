library(circlize)
phasedraw=function(phase,scalenum,colphase){
  library(circlize)
  plot(c(-1, 1), c(-1, 1), type = "n", axes = FALSE, ann = FALSE, asp = 1)
  for(i in 1:6)(
    for(j in 1:4){
      draw.sector((i-1)*45,i*45,j*0.25,col=NA,border="lightgrey")
    }
  )

  lagnum=c("0","4","8","12","16","20")
  degree=cbind(c(105,75),c(60,30),c(15,360-15),c(330,300),c(285,255),c(240,210),c(195,165),c(150,120))
  for(i in 1:6){
    if(is.na(phase[lagnum[i]])){
    }else{
      draw.sector(degree[1,i],degree[2,i],phase[lagnum[i]]/scalenum,col=colphase)
    }
  }
  text(-0.1,0.25,scalenum*0.25)
  text(-0.1,0.5,scalenum*0.5)
  text(-0.1,0.75,scalenum*0.75)
  text(-0.1,1,scalenum*1)
}
data <- read.table("JTK_nfil3_KO_modifyAMP_cleaned.txt", header = TRUE)

# 基于LAG列创建一个表格
test <- table(data$JTK_adjphase)

# 运行函数
pdf("JTKPhase_nfil3_KO.pdf", width = 5, height = 5)
phasedraw(test, 200, "hotpink1")
dev.off()
