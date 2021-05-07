#postscript("indicators_NSGAII_SPEA2.eps", horizontal=FALSE, onefile=FALSE, height=8, width=12, pointsize=10)
pdf("Allocation_Algo_Spread.pdf", onefile=FALSE, width=10)

NSGAIIresultDirectory<-"/Users/aniquatabassum/Downloads/studies/Undergrad Thesis/SuverySetDivide/JMetal/Results/Merged Results"

NSGAIIqIndicator <- function(indicator)
{
  fileNSGAII<-paste(NSGAIIresultDirectory, "Setting 21/Spread/spread_nsga", sep="/")
  NSGAII_results<-scan(fileNSGAII)

  
  fileNSGAIIsi<-paste(NSGAIIresultDirectory, "Setting 22/Spread/spread_spea", sep="/")
  NSGAIIsi_results<-scan(fileNSGAIIsi)
  

  
  algs<-c("NSGAii", "SPEA2")
  #algs<-c("SPC-RM","MPC-RM")
  boxplot(NSGAII_results,NSGAIIsi_results, names=algs, notch = TRUE)
  titulo <-paste(indicator)
  title(main=titulo)
  dev.off()
}


par(mfrow=c(1, 2))
indicator<-"Spread"
NSGAIIqIndicator(indicator)

