# Operationalizing Machine Learning

## Overview
This project is part of the Udacity Azure ML Nanodegree. In this project, I  created an AutoML on a dataset, deployed the best model, enabled logging, created and published pipeline and then consumed the model endpoint. The detailed explanation of the process can be found at https://www.youtube.com/watch?v=p5BYb3G2Ssw&feature=youtu.be.

## Summary
For this project, a file was provided that contains bank marketing information. It cotains data about prospective customers. The target column (y) indicates if a customer subscribed to a fixed term deposit. This project will be a classication model that predicts if a customer will subscribe to a fixed term deposit with a financial institution.

## Architecture and Description
**Introduction**
I was provided the url for the data. I imported the data by into Azure ML portal and I registed it. The image below shows the registered dataset.

![alt text](https://github.com/TemitayoIlori/Machine-Learning/blob/main/NewProject/1.%20Registered%20Dataset.PNG)

Then, I proceeded the create AutoML on the dataset.

**Architecture**

![alt text](https://github.com/TemitayoIlori/Machine-Learning/blob/main/NewProject/Architectural%20Diagram.PNG)

The image above shows the architecture of the AutoML. It can be seen that the task is classification and  accuracy is the primary metric.

![alt text](https://github.com/TemitayoIlori/Machine-Learning/blob/main/NewProject/24.%20Bankmarketing%20dataset%20with%20AutoML%20module.PNG)

The image above shows that AutoML was carried out on the Bank Marketing dataset. The experiment completed successfully as shown in the preceeding two images.

![alt text](https://github.com/TemitayoIlori/Machine-Learning/blob/main/NewProject/2.%20AML%20Complete.PNG)

![alt text](https://github.com/TemitayoIlori/Machine-Learning/blob/main/NewProject/3.%20AML%20Complete.PNG)

As shown below VotingEnsemble is the algorithm with the best performance, with an accuracy of 0.91730. 

![alt text](https://github.com/TemitayoIlori/Machine-Learning/blob/main/NewProject/4.%20Best%20Model.PNG)

![alt text](https://github.com/TemitayoIlori/Machine-Learning/blob/main/NewProject/5.%20Best%20Model.PNG)

Other metrics include AUC_macro=0.948, AUC_micro=0.981 and AUC_weighted=0.948.

![alt text](https://github.com/TemitayoIlori/Machine-Learning/blob/main/NewProject/6.%20Deployment.PNG)

![alt text](https://github.com/TemitayoIlori/Machine-Learning/blob/main/NewProject/7.%20Deployment.PNG)

![alt text](https://github.com/TemitayoIlori/Machine-Learning/blob/main/NewProject/8.%20Deployment.PNG)

As shown above, I deployed the model to Acure Container Instance and I enabled authentication. 

![alt text](https://github.com/TemitayoIlori/Machine-Learning/blob/main/NewProject/9.%20Deployed%20Model.PNG)

![alt text](https://github.com/TemitayoIlori/Machine-Learning/blob/main/NewProject/10.%20Application%20Insights%20enabled.PNG)

From the deployed model, I obtained the REST endpoint and Swagger URI from which I downloaded the swagger.json file.

![alt text](https://github.com/TemitayoIlori/Machine-Learning/blob/main/NewProject/11.%20Enable%20logging%20-%20Logs.py.PNG)

As part of the process for enabling the consumption of the deployed mode, I enabled logging with the attached log.py script. 

![alt text](https://github.com/TemitayoIlori/Machine-Learning/blob/main/NewProject/12.%20Application%20Insights.PNG)

![alt text](https://github.com/TemitayoIlori/Machine-Learning/blob/main/NewProject/13.%20Swagger.PNG)

![alt text](https://github.com/TemitayoIlori/Machine-Learning/blob/main/NewProject/14.%20Swagger.PNG)

I ran the swagger.sh file as well as the endpoint.py file. 

![alt text](https://github.com/TemitayoIlori/Machine-Learning/blob/main/NewProject/15.%20Swagger%20locahost.PNG)

Then, I was able to run Swagger on localhost on port 8000. 

![alt text](https://github.com/TemitayoIlori/Machine-Learning/blob/main/NewProject/16.%20Endpoint.py%20run%20result.PNG)

I passed in some test data in json format and I obtained a response.

![alt text](https://github.com/TemitayoIlori/Machine-Learning/blob/main/NewProject/17.%20Benchmark.PNG)
![alt text](https://github.com/TemitayoIlori/Machine-Learning/blob/main/NewProject/18.%20Benchmark.PNG)

I also ran the benchmark script which tries to consume the endpoint about ten times.

The result shows all ten requests were completed successfully at an average of 112.956 per requests. It could process 8.85 requests per second.

![alt text](https://github.com/TemitayoIlori/Machine-Learning/blob/main/NewProject/19.%20Pipeline%20Created.PNG)

![alt text](https://github.com/TemitayoIlori/Machine-Learning/blob/main/NewProject/20.%20Pipeline%20Created.PNG)


Then I created an endpoint pipeline. I used RunDetails to see the progress of the training. 

![alt text](https://github.com/TemitayoIlori/Machine-Learning/blob/main/NewProject/21.%20Published%20Pipeline%20Active%20Status.PNG)


![alt text](https://github.com/TemitayoIlori/Machine-Learning/blob/main/NewProject/22.%20ML%20Showing%20Run.PNG)

![alt text](https://github.com/TemitayoIlori/Machine-Learning/blob/main/NewProject/23.%20RunDetails.PNG)



## Future work
**Improvement for future experiments**

AutoML shows data imbalance. The first thing would be to find out the cause of the imbalance - whether due to limited availability of data or the nature of the dataset. I could deal with the data imbalance by using a metric that is better suited to imbalanced data. An example is AUC_weighted, which considers the relative number of samples in a class in determining the contribution of the class.

Instead of changing the primary metric, a weighted column could be used to make a class have more or less contributions to the model. I may also take a new sample that is more balanced.

A second thing I can do is to carry out another type of experiment, like Regression or forecasting.

In addition, I could also make use of accelerated models/training like ResNet 50, VGG-16 etc. These make it easy to train and deploy model to Azure.

