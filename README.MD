# start virtual environment
python -m venv .env
source .env/bin/activate


refer to: https://huggingface.co/docs/transformers/installation

Input:
`python main.py "You tell me if this text is positive or negative."`

Output:
```
No model was supplied, defaulted to distilbert-base-uncased-finetuned-sst-2-english and revision af0f99b (https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english).
Using a pipeline without specifying a model name and revision in production is not recommended.
[{'label': 'NEGATIVE', 'score': 0.9963591694831848}]
```
