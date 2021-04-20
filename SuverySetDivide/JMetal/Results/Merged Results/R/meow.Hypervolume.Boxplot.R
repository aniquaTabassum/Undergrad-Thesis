#postscript("indicators_NSGAII_SPEA2.eps", horizontal=FALSE, onefile=FALSE, height=8, width=12, pointsize=10)
pdf("Allocation_RandomMutation.pdf", onefile=FALSE, width=10)

NSGAIIresultDirectory<-"/Users/aniquatabassum/Downloads/studies/Undergrad Thesis/SuverySetDivide/JMetal/Results/Merged Results"

NSGAIIqIndicator <- function(indicator)
{
  fileNSGAII<-paste(NSGAIIresultDirectory, "Setting 1/Hypervolume/hv_setting1", sep="/")
  NSGAII_results<-scan(fileNSGAII)

  
  fileNSGAIIsi<-paste(NSGAIIresultDirectory, "Setting 2/Hypervolume/hv_setting2", sep="/")
  NSGAIIsi_results<-scan(fileNSGAIIsi)
  
  #fileNSGAIIsetting3<-paste(NSGAIIresultDirectory, "Setting 3/Hypervolume/hv_setting3", sep="/")
  #NSGAIIsetting3_results<-scan(fileNSGAIIsetting3)
  
  #fileNSGAIIsetting4<-paste(NSGAIIresultDirectory, "Setting 4/Hypervolume/hv_setting4", sep="/")
  #NSGAIIsetting4_results<-scan(fileNSGAIIsetting4)
  
  #algs<-c("SPC-RM","MPC-RM", "SPC-DKM", "RPC-DKM")
  algs<-c("SPC-RM","MPC-RM")
  boxplot(NSGAII_results,NSGAIIsi_results, names=algs, notch = TRUE)
  titulo <-paste(indicator)
  title(main=titulo)
  dev.off()
}


par(mfrow=c(2,2))
indicator<-"HV"
NSGAIIqIndicator(indicator)

