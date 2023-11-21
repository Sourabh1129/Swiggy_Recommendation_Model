# Swiggy_Restaurant_Recommendation_Model

Welcome to our "Swiggy Restaurant Recommendation Model" project, where we embark on a culinary journey to simplify your dining decisions. In this venture, we harness the potential of data science and machine learning to serve you with personalized restaurant suggestions based on your preferences and location. With a blend of web scraping, data refinement, and an interactive web application, we aim to elevate your dining experience to new heights.

<img src="https://miro.medium.com/v2/resize:fit:1400/1*Qw11nbTP2pBb08x-H2WDSA.png" width="1000" height="250" align="center">

## 📑 Table of Contents

- [🌟 Introduction](#introduction)
- [🧭 Objective to Address](#objective-to-address)
- [📑 Project Synopsis](#project-synopsis)
   - [🌐 Data Extraction](#data-extracrion)
   - [🧼 Data Preprocessing](#data-preprocessing)
   - [📊 Insights and Visualizations](#insights-and-visualizations)
   - [🤖 Machine Learning Algorithm Design](#machine-learning-algorithm-design)
   - [🖥️ Interactive Web Interface](#interactive-web-interface)
   - [🌟 Obstacles and Insights 🌠](#obstacles-and-insights)
   - [🔮 Future Prospects 🌠](#future-prospects)
- [🔚 Conclusion](#conclusion)

## 🌟 Introduction 

The "Swiggy Restaurant Recommendation Model" project is designed to streamline dining decisions using data science and machine learning. It offers individualized restaurant suggestions to users according to their culinary preferences and location. This comprehensive project encompasses web scraping, data refinement, machine learning model creation, and the creation of an interactive web application for an improved dining experience.

## 🧭 Objective to Address

- **Dining Choices Dilemma**: Abundant dining options can be overwhelming.

- **Project Goal**: Create a Restaurant Recommendation Model for personalized suggestions based on cuisine and location.

- **Data-Driven Process**: Involves data collection, refinement, and machine learning for price predictions.

- **User-Friendly App**: Develop an interactive web app for easy dining decisions.


## 📑 Project Synopsis

The project can be divided into several key components:

### 🌐 Data Extraction

- Using Selenium for web scraping, the project gathers extensive restaurant data from Swiggy, encompassing details such as restaurant names, cuisines, locations, user reviews, and menu prices.
![scrapping img 1](https://github.com/Sourabh1129/Swiggy_Recommendation_Model/assets/137646963/f21e1ff6-2c5e-47a1-9ba0-06aa9ef8c9ae)
![scrapping img 2](https://github.com/Sourabh1129/Swiggy_Recommendation_Model/assets/137646963/a5934bb8-7108-40bf-8515-57421789c8f7)

This code snippet illustrates the application of Selenium for web scraping, focusing on the extraction of critical restaurant data from Swiggy's website. It effectively accomplishes the following tasks:
1. Sets up a WebDriver using Selenium to access the Swiggy website.
2. Utilizes the "find_elements" method with the "By.CLASS_NAME" attribute to pinpoint and extract restaurant names and their respective locations.
3. Demonstrates the extracted restaurant names and locations by printing them to the console.

### 🧼 Data Preprocessing

- **Data Quality Enhancement**: Addressing noisy data, null values, and duplicate entries to ensure data integrity and reliability.

- **Outlier Identification**: Conducting outlier analysis to pinpoint and rectify data points that may potentially disrupt accurate predictions.

### 📊 Insights and Visualizations

- Exploring and analyzing the collected data to gain insights into restaurant trends, popular cuisines, and price ranges.
- Creating visualizations to present these insights to users.
![Analysis 1](https://github.com/Sourabh1129/Swiggy_Recommendation_Model/assets/137646963/127e1f5d-a97c-4ee1-8b74-35ea2a1da8c3)
![Analysis 2](https://github.com/Sourabh1129/Swiggy_Recommendation_Model/assets/137646963/6a8931a5-9a4b-4833-9a5b-e70f15580fbd)

### 🤖 Machine Learning Algorithm Design
- Building a Linear Regressor model to predict restaurant prices based on various factors, including cuisine, location, and user reviews.
- Converting categorical columns into numerical values using Label Encoding for model training.
![ml 1](https://github.com/Sourabh1129/Swiggy_Recommendation_Model/assets/137646963/7de75eb3-a28e-4f24-9c0f-bb94512e0284)

### 🖥️ Interactive Web Interface

- Creating a dynamic web interface with Flask, enabling users to input their preferences and receive custom restaurant suggestions.
- Incorporating user-centric features to elevate the dining experience.
![image](https://github.com/Sourabh1129/Swiggy_Recommendation_Model/assets/137646963/d2ee89b1-0a41-454a-ba4f-7651a1097bca)
![image](https://github.com/Sourabh1129/Swiggy_Recommendation_Model/assets/137646963/b8f066df-68cd-4c18-ae0f-1b58bad33775)


### 🌟 Obstacles and Insights 🌠

- Tackling hurdles encountered in web scraping, data refinement, and model building.
- Gaining valuable insights into data management and privacy considerations.


### 🔮 Future Prospects 🌠

- Delving into prospects for real-time menu price updates and dynamic user preferences.
- Elevating the recommendation model through the integration of advanced machine learning 
  algorithms.
- Enhancing the transparency and interpretability of restaurant suggestions.

## 🔚 Conclusion

In summary, the Restaurant Recommendation Model project tackles the dining decision dilemma by offering tailored suggestions. It encompasses data extraction, preprocessing, and machine learning price predictions. The user-friendly web app enhances the dining experience, and visualizations offer valuable restaurant insights. While there are limitations, the project highlights the power of data-driven dining choices.

