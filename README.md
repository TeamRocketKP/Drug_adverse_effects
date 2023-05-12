# Classification of Severity of Drug adverse effects

The project idea was absorbed from the people that we see in our daily life. People are using different types of medicines for various diseases. Many of us know that these medicines will have side effects, but there is something that we need to look into, the adverse effects causing in long period of time. In this project, we would like to classify the severity of adverse drug effects. 

The data source: https://download.open.fda.gov/drug/event/2022q1/drug-event-0001-of-0035.json.zip (it is one of the file) 
There are more than 100 files, if we open the this link (https://open.fda.gov/data/downloads/). The data we are concentrating is 2022 data in "Human Drug" section, "Drug Adverse Events" sub-section.

The EDA file covers the Data wrangling, Data Cleaning, Data Visualization.


Target columns : seriousness related columns like serious, seriousnessdeath, seriousnesshospitalization, seriouslifethreatening, seriousdisabling, seriouscongenitalanomoli.

# Dataset:
Data for this project is retrieved from OpenFDA website. OpenFDA is an Elastic search based API that serves public FDA data about drugs, devices, and foods.

Data set is available under Human Drug tab. Data is available from 2003 , but we will be only working with the first three parts of the year 2022 data.

# Data Cleaning:
As mentioned earlier data is collected from multiple locations, it contains numerous gaps and inconsistencies. It requires extensive cleaning in order to properly format it for analysis and generate accurate predictions.


Visual Representation of Null values in dataset
Data Cleaning Steps :

Extracting useful data columns from Patient and Reaction field.
Dropping the columns which have most of the null values.
Checking the distribution of data points in each column.
Converting the data types from object to category.
Changing binary values from (1 and 2) to (1 and 0).
Converting distinct values of age to age bins.
Transforming generic names of drug dosage form to standard names.
Transforming all drug dosage forms into a uniform name was a tedious task . Even a simple name such as “Tablet” had more than 50 variations, such as “pills,” “TAB,” “film-coated tab,” and “Chewable tablet.” Identifying all of these expressions using regular expressions proved to be challenging. As a result, it was necessary to manually inspect all of the variations and replace them with the correct standardized form.

# Exploratory Data Analysis
Through the data analysis we are trying to gain a deeper understanding of the values, identify patterns and trends, and visualize the distribution of the information.


The graph displays the age distribution by gender within the dataset, revealing that the majority of reported cases of adverse reactions occur in individuals between the ages of 40 — 80. All the age groups have higher percentage of female reports, except for the 0–20 age group. This trend can be attributed to the fact that women tend to undergo various health changes after the age of 20, including pregnancy, which often involves taking medication and increases the likelihood of experiencing adverse reactions.
More than 80 % of the cases are reported from the country USA and Canada.
Highest number of adverse reaction causing death are reported where drug dosage form was Tablet.
Highest number of adverse reaction causing hospitalization are reported where drug dosage form was Injection.
In the case of adverse drug reactions (ADRs), it is crucial to identify the reaction as quickly as possible to provide timely treatment and prevent further harm to the patient. However, when a patient experiences an ADR due to a tablet, there is a higher likelihood that they are outside of the hospital at the time, which can delay the identification and treatment of the reaction. Unfortunately, this delay has resulted in a significant number of patient deaths.

On the other hand, patients who receive injections have a higher probability of being in the hospital at the time of the reaction, which allows for immediate treatment and reduces the risk of adverse outcomes.

*Modeling*
In the predictive modeling process, first the “serious” column was selected as the target feature. This column contains a binary value where 1 indicates that the patient experienced adverse effects of the drug resulting in hospitalization, life-threatening situations, disability, or death, while 0 represents no serious adverse effects.

To perform the binary classification, a logistic regression model was employed, and after training and testing the model, it showed 100% accuracy, indicating low bias in the data and a risk of overfitting.

Consequently, a decision was made to increase the complexity of the prediction by using a multi class classification approach. For this purpose, a decision tree model with five classes (no reaction, hospitalization, life-threatening reaction, disability, and death) was chosen. This model offers a more comprehensive understanding of the data by accounting for the different levels of severity of adverse effects.


Decision Tree Model Pipeline
In the decision tree model, grid search cross-validation was utilized to determine the optimal parameters. The overall training accuracy of the model was found to be 80%, while the test accuracy was 74%. These results indicate that the model’s performance is satisfactory with the selected parameters, specifically max_depth=20 and min_samples_split=0.01.

Checkout this confusion matrix for visually representation of classification scores.


Multi-class Confusion Matrix for Decision Tree
However, due to the highly imbalanced classes, the F1-score was a better evaluation metric than accuracy. The F1 score for major classes, such as “no reaction” and “hospitalization,” was found to be better predicted than other classes. However, the classes with lower numbers of records, including “life-threatening,” “disabling,” and “death,” had fewer data points to learn from, resulting in difficulties in keeping the true positive score high for those classes.

To give the model more data points to learn we can combine “life-threatening” and “disabling” class check if there is any improvement.
Multi-class Confusion Matrix and report for Logistic regression model
Logistic Regression model with four classes has increased the hospitalization and death class true positive results. But they are not significant. Over all accuracy is also increased by 2%.

*Web Application using Flask*
For this project, you can also have an interactive web application to predict the seriousness of drug usage for different diseases. The front-end of the application is built using Streamlit, a Python library that allows developers to create attractive user interfaces with ease. The Flask server is used as the back-end to handle HTTP requests and responses and connect with SQL to store and access data from the dataset.


To load the machine learning model and dataset into the Flask server, you can used pickle files. Using pickle files it is easier to access the model and process the data while ensuring that the model’s accuracy is not affected.

The application consists of four tabs — the home page, dataset page, visualization page, and prediction page. Each of these pages is connected to the Flask server and provides a different functionality.

The prediction page is the most important aspect of the application, as it allows users to input values and predict the seriousness of drug usage for different diseases. The seriousness is categorized into four types: no seriousness, death seriousness, hospitalization seriousness, and life-threatening & disabling seriousness.

The purpose of this application is primarily for experimentation, however, it is important to emphasize that it should not replace the advice and consultation of medical professionals. Before using any drug, it is essential to seek the guidance of a qualified healthcare provider. The goal of this application is to raise awareness about drug usage and its potential impact on our health.

Authors: Sai Manoj Kalasani(https://www.linkedin.com/in/kalasani-sai-manoj/) and Shreya Patil (https://www.linkedin.com/in/shreya-patil-data-scientist/)
