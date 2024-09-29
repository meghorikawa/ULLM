# Evaluating the Affordances of Large Language Models for Enhancing Rule-Based Chatbots for Task-Based Language Teaching

With the goal of improving outcomes in a rule-based chatbot to interpret learner language within a dialogue system, we evaluated the performance of a Large Language Model (LLM), Mixtral-8x7B-Instruct-v0.1, in assessing inputs received from English Language Learners in the AISLA app. Using two prompting strategies, K-shot and Chain of thought (CoT), each student input was evaluated for relevance, presence of a grammatical construct, and factuality on two tasks from the app. 

Our findings indicate that the LLM performed better in classifying relevant student inputs, despite the rule-based chatbot achieving higher precision scores. When classifying relevance, neither of the two prompting strategies seemed to have an influence over the LLM's performance. For detecting grammar constructs, CoT showed better results, with the model's performance peaking at 3-shots for both tasks. The model had little difficulty determining when a student's utterance contained truthful information. However, low precision and recall scores for classifying 'false' and 'none' indicate that the model had trouble classifying these categories. Merging the false and none classes did show more consistent and promising results. 

Additional qualitative analysis and detailed discussion of our findings can be found in the paper we have included in the main directory of this repository. 

The data for this study was used with permission from [Bear et al. (2024)](#Bear-2024) and is not publicly available. 


## Repository Structure

The main directory of this repository contains Google Colab notebooks used to run inference for the LLM via Groq playground, as well as for cleaning and analyzing the data. A description of each is below:

+ **ULLMs_Groq.ipynb** - This notebook contains the main code loop for making the API calls to the LLM for inference. A CSV file of responses is output to save the LLM's responses. 
+ **Extract_values.ipynb** - This notebook contains the code used to extract the generations from the model in the saved JSON format.
+ **Data_Analysis.ipynb*** - This notebook contains the code used for the final data analysis of the extracted data from the model

The Data directory contains a Microsoft Excel file 'Results_DF.xlsx' containing the accuracy, precision, recall, and F1 scores for each of the prompting styles used in our evaluation. 

## Citations

<a name="Bear-2024"></a>
Elizabeth Bear, Xiaobin Chen, Daniela Verratti Souto,
Luisa Ribeiro-Flucht, Björn Rudzewitz, and Detmar
Meurers. 2024. Designing a task-based conversational agent for EFL in German schools: Student needs, actions, and perceptions. System, [126:103460](https://doi.org/10.1016/j.system.2024.103460).