Author: García Aguilar Luis Alberto
Proyect: House prices prediction model
Description: The proyect contains the next stages:
                * Load data
                    inputs: 
                        * training set file (csv)
                        * testing set file (csv)
                    outputs:
                        * training data set shape
                        * training daya set duplicated registers

                * EDA
                    inputs:
                        * training data set
                    outputs:
                        * heatmap of missing values by column
                        * violin plot: Hause style vs salesprice
                
                * Filling missing data
                    input:
                        * training data set
                    output:
                        * training data set without missings

                * Filling missing data
                    input:
                        * training data set
                        * columns to be dropped
                    output:
                        * training data set without unwanted columns
                
                * Preprocessing
                    inputs:
                        * trainig data set
                    outputs:
                        *training data set with columns transformed
                
                * Model:
                    inputs: 
                        trainig data set
                    outputs:
                        * RandomForestRegressor model

                * FInal output:
                    inputs: t
                        * esting data set
                    outputs:
                        * prediction
                        * metrics of the model