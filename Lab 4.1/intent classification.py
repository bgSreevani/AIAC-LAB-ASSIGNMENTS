#Intent Classification for Chatbot Queries
#A company wants to deploy a chatbot to handle customer queries. Each query must be classified into one of the following intents: Account Issue, Order Status, Product Inquiry, or General Question using prompt engineering techniques.

#Task 1
#Prepare Sample Data Create 6 short chatbot user queries, each mapped to one of the four intents
"""Query ID | Query Content                                                                                     | Intent            |
|----------|--------------------------------------------------------------------------------------------------|-------------------|
| 1        | I need help with my account login.                                                                | Account Issue     |
| 2        | When will my order arrive?                                                                        | Order Status      |
| 3        | What are the features of your latest product?                                                     | Product Inquiry   |
| 4        | How do I reset my password?                                                                       | Account Issue     |
| 5        | Can you tell me about your return policy?                                                         | General Question  |
| 6        | Is there a discount available for bulk orders?                                                    | Product Inquiry   |
"""



#Task 2
#Classify a user query into the given intent categories 
"""Headline: Query Classification Result
Output: Order Status
Observation: The query is asking about the arrival time of an order, which falls under the Order Status intent category."""


#Task 3
#classify a new query by following the given example Headline: "How can I change my shipping address?" Category: Account Issue
"""Headline: "What is the warranty period for your products?"  
Output: Product Inquiry
Observation: The query is inquiring about the warranty period of products, which is related to product information and thus falls under the Product Inquiry intent category."""


#Task 4
#clasify a new query using the examples given below Query 1:     Headline: "I forgot my username, how can I retrieve it?"     Output: Account Issue
#Observation: The query is about retrieving a forgotten username, which is an account-related issue and thus falls under the Account Issue intent category.
#Query 2:
#Headline: "Can you provide details about your latest promotions?" Output: General Question
#Observation: The query is asking for information about promotions, which is a general inquiry and therefore belongs to the General Question intent category.

"""Query 1:
Headline: "What is the process to track my shipment?"
Output: Order Status
Observation: The query is about tracking a shipment, which relates to the status of an order and thus falls under the Order Status intent 
category.
Query 2:
Headline: "Do you have any new arrivals in your product line?"
Output: Product Inquiry
Observation: The query is asking about new products, which is related to product information and therefore belongs to the Product Inquiry 
intent category."""



#Task 5
#Apply all three techniques to the same set of test queries and document differences in performance from the above tasks 
"""In Task 2, zero-shot prompting was used to classify the query without any prior examples. The output was accurate, demonstrating that
the model can effectively understand and classify queries based on their content alone.
In Task 3, one-shot prompting was employed by providing a single example before classifying the new query. This approach also yielded a
correct classification, indicating that even a single example can help guide the model's understanding of the task.
In Task 4, few-shot prompting was utilized by providing multiple examples before classifying the new queries. This method proved to be the 
most effective, as the model had more context and examples to learn from, resulting in accurate classifications for both queries.
Overall, while all three prompting techniques were effective in this scenario, few-shot prompting provided the most context and examples, 
leading to the highest accuracy in classification. Zero-shot and one-shot prompting were also successful, but they may not always perform as 
well in more complex classification tasks."""