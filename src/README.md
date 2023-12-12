# Directory Structure
1. ```dataset_generation/``` folder stores all related codes & prompts for generating synthetic emails
2. ```EmailSense.py```: Entry point of the system. It contains the Email Monitor Engine and the Result Generator Engine.
3. ```classifier.py```: The GPT4-Turbo based classifier
4. ```summarizer.py```: The GPT4-Turbo based summarizer

# Validation & Testing
You can evaluate the classifier & summarizer separately using our datasets (or any other dataset following the same format) with: <br/>
```python3 classifier.py <path-to-dataset>.csv``` 
The result will be saved to: ```<path-to-dataset>_result.csv```<br/>
```python3 summarizer.py <path-to-dataset>.csv```
The result will be saved to: ```<path-to-dataset>_summarizer_result.csv```<br/>

