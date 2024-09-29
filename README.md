# Evaluating the Affordances of Large Language Models for Enhancing Rule-Based Chatbots for Task-Based Language Teaching

With the goal of improving outcomes in a rule-based chatbot to interpret learner language within a dialogue system, we evaluated the performance of a Large Language Model (LLM), Mixtral-8x7B-Instruct-v0.1, in assessing inputs received from English Language Learners in the AISLA system (an English learning application). Using two prompting strategies, K-shot and Chain of thought (CoT), each student input was evaluated for relevance, presence of a grammatical construct, and factuality by the LLM on two tasks from the app. 

Our findings indicate that the LLM performed better in classifying relevant student inputs, despite the rule-based chatbot achieving higher precision scores. When classifying relevance, neither of the two prompting strategies seemed to have an influence over the LLM's performance. For detecting grammar constructs, CoT showed better results, with the model's performance peaking at 3-shots for both tasks. The model had little difficulty determining when a student's utterance contained truthful information. However, low precision and recall scores for classifying 'false' and 'none' indicate that the model had trouble classifying these categories. Merging the false and none classes did show more consistent and promising results. 

Additional qualitative analysis and detailed discussion of our findings can be found in the paper we have included in the main directory of this repository. 

The data for this study was used with permission from [Bear et al. (2024)](#Bear-2024) and is not publicly available. 


## Repository Structure

The main directory of this repository contains Google Colab notebooks used to run inference for the LLM via Groq playground, as well as for cleaning and analyzing the data. A description of each is below:

+ **ULLMs_Groq.ipynb** - This notebook contains the main code loop for making the API calls to the LLM for inference. A CSV file of responses is output to save the LLM's responses. 
+ **Extract_values.ipynb** - This notebook contains the code used to extract the generations from the model in the saved JSON format.
+ **Data_Analysis.ipynb*** - This notebook contains the code used for the final data analysis of the extracted data from the model

### Data

The Data directory within this repository contains a Microsoft Excel file 'Results_DF.xlsx' containing the accuracy, precision, recall, and F1 scores for each of the prompting styles used in our evaluation. 

As mentioned above, the data used for this project is not publicly available, but accessible in a seperate private data folder. Each of the above notebooks will need to have the appropriate csv file loaded into the notebook to run properly. Below is a list of the files located in the private data folder and their description. 

| File Names          | Description     |
| ------------------- | ---| 
| AnnotatedData.csv   | the self-annotated AISLA pilot data                              |
| prompt_examples.csv | a csv file containing examples passed to the model for inference |
| bday_df_COT_completions.csv | contains the generated JSONs the LLM produced during inference for the bday task and COT prompting |
| bday_df_FS_completions.csv| contains the generated JSONs the LLM produced during inference for the bday task and FS prompting |
| athletes_df_FS_completions.csv| contains the generated JSONs the LLM produced during inference for the bday task and FS prompting |
| athletes_df_COT_completions.csv| contains the generated JSONs the LLM produced during inference for the bday task and FS prompting |
| athletes_df_FS_parsed.csv| contains the parsed JSON generated by the LLM for athletes task and FS prompting|
| athletes_df_FS_parsed.csv| contains the parsed JSON generated by the LLM for athletes task and COT prompting|
| bday_df_FS_parsed.csv| contains the parsed JSON generated by the LLM for Birthday task and FS prompting|
| bday_df_COT_parsed.csv| contains the parsed JSON generated by the LLM for Birthday task and COT prompting|
|athletes_df_combined.csv| combined FS and COT dataframes for the Comparing athletes task.|
|bday_df_combined.csv| combined FS and COT dataframes for the Birthday task.|
| final_athlete_df.csv | The final cleaned csv file for the comparing athletes task of the generated data and gold standards.  |
| final_bday_df.csv | The final cleaned csv file for the Birthday task of the generated data and gold standards.  |



## Citations

<a name="Bear-2024"></a>
Elizabeth Bear, Xiaobin Chen, Daniela Verratti Souto,
Luisa Ribeiro-Flucht, Björn Rudzewitz, and Detmar
Meurers. 2024. Designing a task-based conversational agent for EFL in German schools: Student needs, actions, and perceptions. System, [126:103460](https://doi.org/10.1016/j.system.2024.103460).