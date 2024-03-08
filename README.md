# EASE2024-HF-ReplicationPackage


This repository contains the source code and the supporting data of the paper entitled *Automated categorization of pre-trained models in software engineering: A case study with a Hugging Face dataset*





## Project structure and set up

- `/results`: This folder contains the results of the evaluation shown in RQ1.
- `/se_kb`: This folder stores the papers, the identified macro and the corresponding sub-tasks used in the mapping algorithm.
- `/stats`: This folder stores the distribution of the HF tags and the macro-tasks.
- `datasets.zip`: It contains the original HF dump, the d1 dataset (step 1 of the filtering process), and d2 which represents the final dataset used in the RQ1 experiments.
- `requirements.txt`: This file contains the needed libraries to run the project. 




## Utils

- `classifier.py`: It contains all the functions to run the two classifiers employed in RQ1.
- `config.py`: It contains local paths that are needed to produce the results.
- `data_utils.py`: A utility script that provides functions for data handling and manipulation.
- `dump_utils.py`: It contains the helper functions to interact with the HF dump.
- `main.py`: The main script that runs the core logic of the project.
- `mapping_utils.py`: It contains the implementation of the mapping algorithm presented in the paper.


## Classification pipeline

To replicate the experiment conducted in RQ1, you can run the 
run_classifier function with the following parameters:

``` 
run_classifier(dataset='datasets/d2.csv',
desc='card_data',
 cat='tags', 
 model='CNB', results_csv_path='results/cnb_results.csv') 
 ```

where *desc* and *cat* are the model card description and the pipeline tag respectively. You can change the classifier by setting the *model* parameter equal to ['SVC','CNB']. The results of the cross-fold validation are stored in the path specified by the *results_csv_path* parameter.   

## Identified papers and macro tasks

The se_kb folder contains the following files:

- `papers_all.csv`: It contains all the papers retrieved from Scopus
- `papers_selected.csv`: It contains the final number of papers relevant to our study. Each paper has a unique ID used in the mapping phase. 
- `extracted_se_tasks.csv`: It contains all the SE sub-tasks and the corresponding paper IDs
- `macro_sub_tasks.csv`: It stores the list of macro tasks and the corresponding sub-tasks.


All the abovementioned files have been used by the mapping algorithm discussed in the forthcoming section. 





## Example mapping

To get the mapping, you need to run the function 

`mapping_pipeline(ptm,dataset)` where ptm is the name of the model and the dataset is *d2.csv* file stored in the *datasets.zip* folder. An explanatory output of the query ptm='bert' is shown below:




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
- Classification of SE artifacts
- Miscellaneous
- Testing/Program repair
- Code-related task
- Documentation/Requirements
- Text engineering related to SE artifacts 
```

#### Identified Sub-tasks

```
- Generating code patches
- Bug fix/Program repair
- Code generation/completion
- Algorithm classification
- Code clone detection
- Code search 
- Bug report
- Requirement classification
- API reviews classification
- StackOverflow title generation
- Sentiment analysis 
- Issue report classification
- String generation secondary studies
- Commit classification
- Program merge
- Stack overflow post summarization
- Traceability
```




