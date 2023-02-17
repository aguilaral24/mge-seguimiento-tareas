# House prices prediction model
### Author: García Aguilar Luis Alberto

Description: The proyect contains the next stages:
                1. Load data
                    inputs: 
                        * training set file (csv)
                        * testing set file (csv)
                    outputs:
                        * training data set shape
                        * training daya set duplicated registers

                2. EDA
                    inputs:
                        * training data set
                    outputs:
                        * heatmap of missing values by column
                        * violin plot: Hause style vs salesprice
                
                3. Filling missing data
                    input:
                        * training data set
                    output:
                        * training data set without missings

                4. Filling missing data
                    input:
                        * training data set
                        * columns to be dropped
                    output:
                        * training data set without unwanted columns
                
                5. Preprocessing
                    inputs:
                        * trainig data set
                    outputs:
                        *training data set with columns transformed
                
                6. Model:
                    inputs: 
                        trainig data set
                    outputs:
                        * RandomForestRegressor model

                7. FInal output:
                    inputs: t
                        * esting data set
                    outputs:
                        * prediction
                        * metrics of the model