package org.cloudbus.cloudsim.examples.carbonaware;

import java.io.IOException;

import org.cloudbus.cloudsim.examples.power.random.RandomRunner;

public class CarbonAwareSim {

    public static void main(String[] args) throws IOException {
        boolean enableOutput = true;
        boolean outputToFile = true;
        String inputFolder = "";
        String outputFolder = "carbonaware";
        String workload = "random";
        String vmAllocationPolicy = "dvfs";
        String vmSelectionPolicy = "";
        String parameter = "";

        System.out.println("Starting CarbonAwareSim");
        new RandomRunner(
                enableOutput,
                outputToFile,
                inputFolder,
                outputFolder,
                workload,
                vmAllocationPolicy,
                vmSelectionPolicy,
                parameter
        );
        System.out.println("Finished CarbonAwareSim");
    }
}

