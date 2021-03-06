# Optimizing an ML Pipeline in Azure

## Overview
This project is part of the Udacity Azure ML Nanodegree. In this project, I built and optimized an Azure ML pipeline using the Python SDK and a provided Scikit-learn model. This model is then compared to an Azure AutoML run.

## Summary
**Problem statement:**
For this project, a file was provided that contains bank marketing iformation. It cotains data about prospective customers. The target column (y) indicates if a customer subscribed to a fixed term deposit. This project will be a classication model that predicts if a customer will subscribe to a fixed term deposit with a financial institution.
**Solution:**
The best performing model was VotingEnsemble with an accuracy of 0.9168.
## Scikit-learn Pipeline
**Pipeline architecture, including data, hyperparameter tuning, and classification algorithm.**
I was provided the url for the data. I imported the data by creating TabularDataset using TabularDatasetFactory. I cleaned the data by using a clean_data function created in a python script. The data was one not encoded.
I split the data into train and validation datasets using scikit-learn's train_test_split()
The parameters I tuned are C and max_iter

I used RandomParameterSampling with choice.This is a method of hyperparameter tuning that randomly selects hyperparameters in a search space. I chose RandomParameterSampling as against other methods like Grid Search because it allows selection of hyperparameters when thare are no know combinations that perform well and without guessing.
I used SKLearn estimator for my python script. Primary metrics was Accuracy and the primary metric goal is to maximize accuracy. Accuracy of the best child run is 0.90794.
I got the best run by using get_best_run_by_primary_metric() and I registered the model using best_run.register_model.

For AutoML, I used RunDetails to see the progress of the training. I retrieved the best model using get_output().

**Benefits of the parameter sampler chosen?**
I chose RandomParameterSampling parameter sampler and provided values for C (which are not big enough to cause over-fitting) and max_iter. C is the inverse of regulization strength, smaller values of which are associated with stronger regulization. Max_iter is the number of iterations over the data. The experiment will not run more than the specified number of iterations. 
**Benefits of the early stopping policy chosen?**
I chose BanditPolicy as the early stopping policy chosen, with evaluation_interval=1, slack_factor=0.1, delay_evaluation=5. This terminates runs that are not performing well. Precisely, it evaluates every step and terminates a run that is not within 10% of te best performing run. This saves time.

## AutoML
**The model and hyperparameters generated by AutoML.**

There were 23 iterations. VotingEnsemble is the algorithm with the best performance. The best run took 01:40 minutes and had an accuracy of 0.91706. The most important features are: duration, emp.var.rate, nr.employed and euribor3m. AUC_macro=0.94723, AUC_micro=0.98061 and AUC_weighted=0.94723.

VotingEnsemble in this run has ensemble_weights:[0.2,0.1,0.1,0.1,0.2,0.1,0.1,0.1]. ensemble_algorithms are [ XGBoostClassifier, LightGBM, LightGBM, XGBoostClassifier, XGBoostClassifier,LogisticRegression, RandomForest, RandomForest]. Ensembled_iterations:[1,0,19,14,11,9,4,5]

![alt text](https://github.com/TemitayoIlori/Machine-Learning/blob/main/AZMLND_Optimizing_a_Pipeline_in_Azure-Starter_Files/VotingEnsemble.png)

## Pipeline comparison
**Compare the two models and their performance. What are the differences in accuracy? In architecture? If there was a difference, why do you think there was one?**
The AutoML model performed better and is faster than the Scikit-learn pipeline. It had an accuracy of 0.91706 versus 0.90794 for Scikit-learn. AutoML performs better because hyperparameter optimization is automated.

## Future work
**Improvement for future experiments? Why might these improvements help the model?**
I will try Bayesian sampling as a parameter sampler. Since it picks samples based on the performance of previous samples, it can help improve primary metric. Basically, they choose the next hyperparameter based on the hyperparameters used in previous runs that performed well. Therefore, they are able to detect hyperparameters that are more promising than just randomly selecting an hyperparameter.

A second improvement will be to fix the data imbalance that was detected. The first thing would be to find out the cause of the imbalance - whether due to limited availability of data or the nature of the dataset. 

I could deal with the data imbalance by using a metric that is better suited to imbalanced data. An example is AUC_weighted, which considers the relative number of samples in a class in determining the contribution of the class.

Instead of changing the primary metric, a weighted column could be used to make a class have more or less contributions to the model. I may also take a new sample that is more balanced.
## Proof of cluster clean up
**If you did not delete your compute cluster in the code, please complete this section. Otherwise, delete this section.**
**Image of cluster marked for deletion**

See the images below.

![alt text](https://github.com/TemitayoIlori/Machine-Learning/blob/main/AZMLND_Optimizing_a_Pipeline_in_Azure-Starter_Files/AML4.PNG)
![alt text](https://github.com/TemitayoIlori/Machine-Learning/blob/main/AZMLND_Optimizing_a_Pipeline_in_Azure-Starter_Files/AML5.jpg)
![alt text](https://github.com/TemitayoIlori/Machine-Learning/blob/main/AZMLND_Optimizing_a_Pipeline_in_Azure-Starter_Files/AML6.PNG)
