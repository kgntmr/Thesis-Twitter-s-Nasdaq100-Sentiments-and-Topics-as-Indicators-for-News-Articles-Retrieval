# Motivation

This dissertation aims to enhance investment strategies by leveraging public opinions and news articles. Using VADER lexicon and Latent Dirichlet Allocation (LDA), it extracts insights from Tweets about Nasdaq100 companies and visualizes them in a dashboard gain ideas about both perspectives. Additionally, it fine-tunes the RoBERTa model on a subjective question-answering dataset to improve its reasoning capabilities and creates a retriever-generator system for rapid engagement with news articles. While focused on a specific time frame and company due to research constraints, this framework can be applied to other types of textual datasets.

## Installation

To set up the environment for this project, follow these steps:

**1. Clone the Repository:**
Clone this repository to your local machine

```
git clone https://github.com/kgntmr/Thesis-Twitter-s-Nasdaq100-Sentiments-and-Topics-as-Indicators-for-News-Articles-Retrieval.git
cd Thesis-Twitter-s-Nasdaq100-Sentiments-and-Topics-as-Indicators-for-News-Articles-Retrieval
```

**2. Install Dependencies:**
All required libraries and dependencies are specified in the `requirements.txt` file. Install them by running:

```
pip install -r requirements.txt
```

### How To Use
Each jupyter files are serving to different purposes and each needs to be used differently:
- Sentiment Analysis:

To perform sentiment analysis, simply replace the file path in `amz = pd.read_excel('Amazon.xlsx')` with your dataset. Adjust the text preprocessing steps as needed—for instance, you may choose to include or convert emojis to text. Please ensure data types are formatted as follows:
```
Date                          datetime64[ns]
Tweet content                 string[python]
```

- Semantic Analysis:

For semantic analysis, also replace the file path with your dataset in the specified step. Ensure the data types align with those used in the sentiment analysis.

- Fine-Tuning an LLM for QA:

This code is adaptable for fine-tuning any large language model for question-answering tasks, not limited to RoBERTa. Ensure your data types match those specified for seamless integration:

```
 #   Column             Non-Null Count  Dtype 
---  ------             --------------  ----- 
 0   question           2501 non-null   object
 1   human_ans_indices  2501 non-null   object
 2   review             2501 non-null   object
 3   human_ans_spans    2501 non-null   object
 4   id                 2501 non-null   object
```
