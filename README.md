# Motivation

This dissertation aims to enhance investment strategies by leveraging public opinions and news articles. Using VADER lexicon and Latent Dirichlet Allocation (LDA), it extracts insights from Tweets about Nasdaq100 companies and visualizes them in a dashboard gain ideas about both perspectives. Additionally, it fine-tunes the RoBERTa model on a subjective question-answering dataset to improve its reasoning capabilities and creates a retriever-generator system for rapid engagement with news articles. While focused on a specific time frame and company due to research constraints, this framework can be applied to other types of textual datasets. If you're interested, check out the [Research Paper](https://arc.cct.ie/ict/48/) for more details, and explore the model on [HuggingFace](https://huggingface.co/kgntmr/RoBERTa-SQuAD2.0-SubjQA) to try its capabilities directly.

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

## How To Use
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

This code is adaptable for fine-tuning any large language model for question-answering tasks, not limited to RoBERTa. Ensure your data types and names match those specified for seamless integration:

```
Column                Dtype 
------                ----- 
question              object
human_ans_indices     object
review                object
human_ans_spans       object
id                    object
```
- RAG System:

This code is also adaptable for any large language model for RAG system, you can change the choice of your model by simply putting the details of your own model in to this line:

```
qa_pipeline = pipeline("question-answering", model="kgntmr/RoBERTa-SQuAD2.0-SubjQA")
```

The web scraping section may require adjustments, such as modifying the attributes to suit your chosen website, along with other potential tweaks. However, the overall pipeline remains unchanged. If you prefer not to use web scraping, you can simply upload your own files directly into the Jupyter notebook after a small adjustment in the code.
