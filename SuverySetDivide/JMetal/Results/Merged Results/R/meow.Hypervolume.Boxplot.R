#postscript("indicators_NSGAII_SPEA2.eps", horizontal=FALSE, onefile=FALSE, height=8, width=12, pointsize=10)
pdf("Allocation_DKM_V2.pdf", onefile=FALSE, width=10)

NSGAIIresultDirectory<-"/Users/aniquatabassum/Downloads/studies/Undergrad Thesis/SuverySetDivide/JMetal/Results/Merged Results"

NSGAIIqIndicator <- function(indicator)
{
  fileNSGAII<-paste(NSGAIIresultDirectory, "Setting 1/Hypervolume/hv_setting1", sep="/")
  NSGAII_results<-scan(fileNSGAII)

  
  fileNSGAIIsi<-paste(NSGAIIresultDirectory, "Setting 2/Hypervolume/hv_setting2", sep="/")
  NSGAIIsi_results<-scan(fileNSGAIIsi)
  
  fileNSGAIIsetting3<-paste(NSGAIIresultDirectory, "Setting 3/Hypervolume/hv_setting3", sep="/")
  NSGAIIsetting3_results<-scan(fileNSGAIIsetting3)
  
  fileNSGAIIsetting4<-paste(NSGAIIresultDirectory, "Setting 4/Hypervolume/hv_setting4", sep="/")
  NSGAIIsetting4_results<-scan(fileNSGAIIsetting4)
  
  fileNSGAIIsetting5<-paste(NSGAIIresultDirectory, "Setting 5/Hypervolume/hv_setting5", sep="/")
  NSGAIIsetting5_results<-scan(fileNSGAIIsetting5)
  
  fileNSGAIIsetting6<-paste(NSGAIIresultDirectory, "Setting 6/Hypervolume/hv_setting6", sep="/")
  NSGAIIsetting6_results<-scan(fileNSGAIIsetting6)
  
  algs<-c("SPC-RM","MPC-RM", "SPC-DKM", "MPC-DKM", "SBX-Poly", "SPC-DKM_V2")
  #algs<-c("SPC-RM","MPC-RM")
  boxplot(NSGAII_results,NSGAIIsi_results, NSGAIIsetting3_results, NSGAIIsetting4_results, NSGAIIsetting5_results, NSGAIIsetting6_results, names=algs, notch = TRUE)
  titulo <-paste(indicator)
  title(main=titulo)
  dev.off()
}


par(mfrow=c(3,2))
indicator<-"HV"
NSGAIIqIndicator(indicator)

