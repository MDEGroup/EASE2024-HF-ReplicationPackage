# EASE2024-HF-ReplicationPackage


This repository contains the source code and the supporting data of the paper entitled *Towards automatically categorizing pre-trained models in software engineering: the Hugging Face experience*

## Project structure

- `/results`: This folder contains the results of the evaluation shown in RQ1.
- `/se_kb`: This folder stores the papers, the identified macro and sub-tasks used in the mapping algorithm.
- `/stats`: This folder stores the distribution of the HF tags and the macro-tasks.

## Utils

- `classifier.py`: It contains all the functions to run the two classifiers employed in RQ1.
- `config.py`: It contains local paths that are needed to produce the results.
- `data_utils.py`: A utility script that provides functions for data handling and manipulation.
- `dump_utils.py`: It contains the helper functions to interact with the HF dump.
- `main.py`: The main script that runs the core logic of the project.
- `mapping_utils.py`: It contains the implementation of the mapping algorithm presented in the paper.

- `visualization.py`: It contains functions or classes to visualize the data and results.

## Example mapping

To get the mapping, you need to run the function 

`mapping_pipeline(ptm,dataset)` where ptm is the name of the model and dataset is the filtered dump stored in the dataset folder. An explanatory output of the query ptm='bert' is shown below:




#### Most Frequent Tag
``` text-classification, 8 occurrences ```

#### Similar Pre-trained Models (PTMs)

```
- ber2, text-classification
- ber3, text-classification
- bort, text2text-generation
- ber4, text-classification
- bert, sentence-similarity
- bert1, text-classification
- best, token-classification
- sbert, sentence-similarity
- bert, question-answering
- bert, text-classification
```


#### Identified Macro tasks
```
Classification of SE artifacts
Miscellaneous
Testing/Program repair
Code-related task
Documentation/Requirements
Text engineering related to SE artifacts 
```

#### Identified Sub-tasks

```
Generating code patches
Bug fix/Program repair
Code generation/completion
Algorithm classification
Code clone detection
Code search 
Bug report
Requirement classification
API reviews classification
StackOverflow title generation
Sentiment analysis 
Issue report classification
String generation secondary studies
Commit classification
Program merge
Stack overflow post summarization
Traceability
```




