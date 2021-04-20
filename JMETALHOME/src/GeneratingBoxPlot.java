import jmetal.core.Algorithm;
import jmetal.experiments.Experiment;

import java.io.IOException;

public class GeneratingBoxPlot extends Experiment{
    @Override
    public void algorithmSettings(String problemName, int problemId, Algorithm[] algorithm) throws ClassNotFoundException {

    }

    public static void main(String[] args) throws IOException {
        GeneratingBoxPlot exp = new GeneratingBoxPlot();
        exp.experimentName_ = "Doctor Allocation NSGAii";
        exp.experimentBaseDirectory_ = "/Users/aniquatabassum/Downloads/studies/Undergrad Thesis/SuverySetDivide/JMetal/Results/Merged Results";
        exp.indicatorList_ = new String[]{"Hypervolume"};
        exp.algorithmNameList_ = new String[]{"NSGAii"};
        exp.generateRBoxplotScripts(2, 2, new String[]{"NSGAii"}, "meow", true, exp) ;




    }
}
