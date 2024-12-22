# Machine Learning Engineer Challenge Documentation

## Part 1: Transcribe the .ipynb Code to model.py

### Overview

In this section, we will transcribe the code from a Jupyter Notebook (`.ipynb`) to a Python script (`model.py`). This process involves converting the notebook cells into a cohesive and well-structured Python script, to preprocess data, train a model and predict.

### Steps

1. **Model selection**
    As it is said in the notebook "the model to be productive must be the one that is trained with the top 10 features and class balancing", so let's go deeper into how to select a model and why I selected the **Logistic regression**. Points to have in mind to select a mode:

     - Performance: There is no significant difference in performance between XGBoost and Logistic Regression.
     - Efficiency: With the feature selection (TOP 10) and class balancing, it is being improved in both.
     - Interpretability: Logistic Regression is easier to interpret and explain, especially when using the top 10 most important features.
     - Simplicity: Logistic Regression It is computationally less complex compared to XGBoost, which reduces the computational cost and makes it easier to maintain in production.

    So the decition is Logistic regression as it is less complex and easier to interpret.

2. **Modify the Model module**

   - Add `constants.py` and `preprocess_functions.py` to manage things out of the scope of the class DelayModel.
   - Modify **preprocess** method to return a tuple of features,target or just a dataframe with the features, the features are always returned with the TOP 10 feture selection.
   - Modify **fit** method to train the model using the features and the target but having in mind the class balance and stores it in the instance variable `self._model`
   - Modify **predict** method to use `self._model` and predict using the parameter features, raises an error if the model has not been trained

3. **Tests**

   - Modify **Data Loading** path to be a relative path to the project
   - Modify **test_model_predict** test to train a model first and then use it, as it was before, the test is always failing as the model needs to be trained first. Despite the model was trained in the previous test, remember that each tests is independent and the setup method will always clear and instantiate again all for each test.
   - Add **test_model_predict_error** test to increase the coverage and test the error case when the model is not trained before

### Conclusion

-------
