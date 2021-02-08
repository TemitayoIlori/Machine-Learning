# Capstone Project - Azure Machine Learning Engineer

## Overview of Project
This project is part of the Udacity Azure ML Nanodegree. This project is in three parts. In the first part, I optimized hyperparameters for Machine Learning using Python SDK. In the second part, built and optimized an Azure ML pipeline using the Python SDK and Scikit-learn model. This model is then compared to the hyerparameter model. Here is a screen capture for the project https://youtu.be/GCAblR2ltv8.

![alt text](https://github.com/TemitayoIlori/Machine-Learning/blob/main/Capstone%20Project%20-%20Azure%20Machine%20Learning%20Engineer/Capstone%20Architecture.png)

The architecture for the project is shown above.

## Summary
**Problem statement:**

I will like to contribute to the health of people in my community. Therefore, for this project, I chose to work on data on Parkinson disease. I obtained the data from https://archive.ics.uci.edu/ml/machine-learning-databases/parkinsons/parkinsons.data.
**Solution:**
AutoML did better than hyperparameter optimization.

## Overview of Data

The data used for this project was obtained from https://archive.ics.uci.edu/ml/machine-learning-databases/parkinsons/parkinsons.data. As shown in the images below, I obtained the data using TabularDatasetFactory. I cleaned the dataset by removing a column called 'name' which is not useful for this project. Then, I registered the dataset.

![alt text](https://github.com/TemitayoIlori/Machine-Learning/blob/main/Capstone%20Project%20-%20Azure%20Machine%20Learning%20Engineer/AutoML-Images/1.%20Obtained%20and%20Registered%20Dataset.PNG)

![alt text](https://github.com/TemitayoIlori/Machine-Learning/blob/main/Capstone%20Project%20-%20Azure%20Machine%20Learning%20Engineer/AutoML-Images/2.%20Registered%20Dataset.PNG)


## Scikit-learn Pipeline


**Pipeline architecture, including data, hyperparameter tuning, and classification algorithm.**
I imported the data by creating TabularDataset using TabularDatasetFactory. I cleaned the data by removing the 'name' field. 
I split the data into train and validation datasets using scikit-learn's train_test_split()
The parameters I tuned are C and max_iter

I used RandomParameterSampling with choice.This is a method of hyperparameter tuning that randomly selects hyperparameters in a search space. I chose RandomParameterSampling as against other methods like Grid Search because it allows selection of hyperparameters when thare are no know combinations that perform well and without guessing.
I used SKLearn estimator for my python script. Primary metrics was Accuracy and the primary metric goal is to maximize accuracy. Accuracy of the best child run is 0.8814.
I got the best run by using get_best_run_by_primary_metric() and I registered the model using best_run.register_model.

**Benefits of the parameter sampler chosen?**
I chose RandomParameterSampling parameter sampler and provided values for C (which are not big enough to cause over-fitting) and max_iter. C is the inverse of regulization strength, smaller values of which are associated with stronger regulization. Max_iter is the number of iterations over the data. The experiment will not run more than the specified number of iterations. 

**Benefits of the early stopping policy chosen?**
I chose BanditPolicy as the early stopping policy chosen, with evaluation_interval=1, slack_factor=0.1, delay_evaluation=5. This terminates runs that are not performing well. Precisely, it evaluates every step and terminates a run that is not within 10% of te best performing run. This saves time.

## AutoML


I used RunDetails to see the progress of the training. I retrieved the best model using get_output(). VotingEnsemble is the algorithm with the best performance. The best run took 01:40 minutes and had an accuracy of 0.93846,  AUC_macro=0.952, AUC_micro=0.971 and AUC_weighted=0.952.

![alt text](https://github.com/TemitayoIlori/Machine-Learning/blob/main/AZMLND_Optimizing_a_Pipeline_in_Azure-Starter_Files/VotingEnsemble.png)


## Pipeline comparison (Hyperparameter Tuning Vs AutoML)

The AutoML model performed better and is faster than the Scikit-learn pipeline. It had an accuracy of 0.93846 versus 0.8814 for Scikit-learn. AutoML performs better because hyperparameter optimization is automated.


## Deployment and Consumption of AutoML Model

![alt text](https://github.com/TemitayoIlori/Machine-Learning/blob/main/Capstone%20Project%20-%20Azure%20Machine%20Learning%20Engineer/AutoML-Images/4.%20AML%20Running.png)

The image above shows that AutoML was carried out on the Bank Marketing dataset. The experiment completed successfully as shown in the preceeding two images.

![alt text](https://github.com/TemitayoIlori/Machine-Learning/blob/main/Capstone%20Project%20-%20Azure%20Machine%20Learning%20Engineer/AutoML-Images/5.%20Experiment%20Completed.png)

As shown below VotingEnsemble is the algorithm with the best performance, with an accuracy of 0.93846. 

![alt text](https://github.com/TemitayoIlori/Machine-Learning/blob/main/Capstone%20Project%20-%20Azure%20Machine%20Learning%20Engineer/AutoML-Images/6.%20Best%20Model.png)

![alt text](https://github.com/TemitayoIlori/Machine-Learning/blob/main/Capstone%20Project%20-%20Azure%20Machine%20Learning%20Engineer/AutoML-Images/7.%20Best%20Model%20-%20Other%20Metrics.png)

Other metrics include AUC_macro=0.948, AUC_micro=0.981 and AUC_weighted=0.948.

![alt text](https://github.com/TemitayoIlori/Machine-Learning/blob/main/Capstone%20Project%20-%20Azure%20Machine%20Learning%20Engineer/AutoML-Images/8.%20Deployment.png)

![alt text](https://github.com/TemitayoIlori/Machine-Learning/blob/main/Capstone%20Project%20-%20Azure%20Machine%20Learning%20Engineer/AutoML-Images/9.%20Deployed%20Model.png)

![alt text](https://github.com/TemitayoIlori/Machine-Learning/blob/main/Capstone%20Project%20-%20Azure%20Machine%20Learning%20Engineer/AutoML-Images/10.%20Endpoint%20showing%20ACI%20Compute%20Type.png)

As shown above, I deployed the model to Acure Container Instance and I enabled authentication. 


![alt text](https://github.com/TemitayoIlori/Machine-Learning/blob/main/Capstone%20Project%20-%20Azure%20Machine%20Learning%20Engineer/AutoML-Images/12.%20Application%20Insights%20Enabled.png)


From the deployed model, I obtained the REST endpoint and Swagger URI from which I downloaded the swagger.json file.

![alt text](https://github.com/TemitayoIlori/Machine-Learning/blob/main/Capstone%20Project%20-%20Azure%20Machine%20Learning%20Engineer/AutoML-Images/11.%20Enable%20Logging%20-%20Logs.py.png)

As part of the process for enabling the consumption of the deployed mode, I enabled logging with the attached log.py script. 

![alt text](https://github.com/TemitayoIlori/Machine-Learning/blob/main/Capstone%20Project%20-%20Azure%20Machine%20Learning%20Engineer/AutoML-Images/13.%20Application%20Insights.png)

![alt text](https://github.com/TemitayoIlori/Machine-Learning/blob/main/Capstone%20Project%20-%20Azure%20Machine%20Learning%20Engineer/AutoML-Images/14.%20Swagger.png)

![alt text](https://github.com/TemitayoIlori/Machine-Learning/blob/main/Capstone%20Project%20-%20Azure%20Machine%20Learning%20Engineer/AutoML-Images/15.%20Swagger.png)

I ran the swagger.sh file as well as the endpoint.py file. 

![alt text](https://github.com/TemitayoIlori/Machine-Learning/blob/main/Capstone%20Project%20-%20Azure%20Machine%20Learning%20Engineer/AutoML-Images/16.%20Swagger%20on%20localhost.png)

Then, I was able to run Swagger on localhost on port 8000. 

![alt text](https://github.com/TemitayoIlori/Machine-Learning/blob/main/Capstone%20Project%20-%20Azure%20Machine%20Learning%20Engineer/AutoML-Images/17.%20endpoint.py%20run.png)

I passed in some test data in json format and I obtained a response.

![alt text](https://github.com/TemitayoIlori/Machine-Learning/blob/main/Capstone%20Project%20-%20Azure%20Machine%20Learning%20Engineer/AutoML-Images/18.%20Benchmark.png)

![alt text](https://github.com/TemitayoIlori/Machine-Learning/blob/main/Capstone%20Project%20-%20Azure%20Machine%20Learning%20Engineer/AutoML-Images/19.%20Benchmark%20Summary.png)

I also ran the benchmark script which tries to consume the endpoint about ten times.

The result shows all ten requests were completed successfully at an average of 206.306 per requests. It could process 4.85 requests per second.

![alt text](https://github.com/TemitayoIlori/Machine-Learning/blob/main/Capstone%20Project%20-%20Azure%20Machine%20Learning%20Engineer/AutoML-Images/20.%20Pipeline.png)

![alt text](https://github.com/TemitayoIlori/Machine-Learning/blob/main/Capstone%20Project%20-%20Azure%20Machine%20Learning%20Engineer/AutoML-Images/21.%20Pipeline%20Created.png)


Then I created an endpoint pipeline. 

![alt text](https://github.com/TemitayoIlori/Machine-Learning/blob/main/Capstone%20Project%20-%20Azure%20Machine%20Learning%20Engineer/AutoML-Images/22.%20Published%20Pipeline%20Active%20Status.png)

I used RunDetails to see the progress of the training. 
![alt text](https://github.com/TemitayoIlori/Machine-Learning/blob/main/Capstone%20Project%20-%20Azure%20Machine%20Learning%20Engineer/AutoML-Images/23.%20RunDetails.png)

## Future work

I will try Bayesian sampling as a parameter sampler. Since it picks samples based on the performance of previous samples, it can help improve primary metric. Basically, they choose the next hyperparameter based on the hyperparameters used in previous runs that performed well. Therefore, they are able to detect hyperparameters that are more promising than just randomly selecting an hyperparameter.

A second improvement will be to fix the data imbalance that was detected. The first thing would be to find out the cause of the imbalance - whether due to limited availability of data or the nature of the dataset. 

I could deal with the data imbalance by using a metric that is better suited to imbalanced data. An example is AUC_weighted, which considers the relative number of samples in a class in determining the contribution of the class.

Instead of changing the primary metric, a weighted column could be used to make a class have more or less contributions to the model. I may also take a new sample that is more balanced.



## Proof of cluster clean up

The compute cluster was deleted in the code.
