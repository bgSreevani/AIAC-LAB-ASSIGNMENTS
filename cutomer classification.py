
#Lab 4: Advanced Prompt Engineering – Zero-shot, One-shot, and Few-shot Techniques
"""
=======================================================================
Problem Statement 1: Customer Email Classification
=======================================================================

Categories:
Billing, Technical Support, Feedback, Others

1. Sample Emails:
1: "My bill amount is higher than expected. Please verify."
Category: Billing
2: "The website is not loading on my browser."
Category: Technical Support
3: "I really like your fast customer support service."
Category: Feedback
4: "Can you share your company address?"
Category: Others
5: "I need a payment receipt for my last transaction."
Category: Billing
Observation:Sample data preparation helped clearly define each category and made classification easier.
-----------------------------------------------------------------------

2. Zero-shot Prompt:

Classify the following email into Billing, Technical Support, Feedback, or Others.
Email: "My account balance is showing incorrectly after payment."
Expected Output:
Billing
Observation:The model correctly classified the email without examples, showing good understanding, but accuracy may reduce for complex cases.

-----------------------------------------------------------------------

3. One-shot Prompt:
Example:
Email: "My bill is incorrect."
Category: Billing
Now classify:
Email: "The app is freezing while opening."
Expected Output:
Technical Support
Observation:Providing one example improved clarity and accuracy, giving more reliable results than zero-shot prompting.

-----------------------------------------------------------------------

4. Few-shot Prompt:
Example 1:
Email: "Please provide payment receipt."
Category: Billing
Example 2:
Email: "Website not loading properly."
Category: Technical Support
Example 3:
Email: "Great service experience."
Category: Feedback
Now classify:
Email: "What is your office location?"
Expected Output:
Others
Observation:Multiple examples provided better context, resulting in the most accurate and consistent classifications.

-----------------------------------------------------------------------

5. Comparison:
In Task 2, zero-shot prompting was used to classify the customer email without providing any prior examples. 
The output was accurate, indicating that the language model is capable of understanding the context and 
meaning of the email and performing classification based solely on the given instructions.

In Task 3, one-shot prompting was applied by providing a single labeled example before classifying a new email. 
This method resulted in improved accuracy and clarity, as the example helped guide the model in understanding 
the expected classification pattern.

In Task 4, few-shot prompting was implemented by providing multiple labeled examples prior to classification. 
This approach proved to be the most effective, as the additional examples provided richer context and better 
guidance, leading to highly accurate and consistent classification results.

Overall, while zero-shot and one-shot prompting techniques demonstrated satisfactory performance, few-shot 
prompting delivered the best results. The presence of multiple examples enhanced the model’s understanding of 
category distinctions, making few-shot prompting the most reliable method for customer email classification.


"""