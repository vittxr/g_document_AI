# Setup

1. run `python -m venv venv`
2. run `./venv/Scripts/activate` (`source ./venv/bin/activate` if you are using linux)
3. run `pip install -r requirements.txt`
4. config your credentials (service account) and the documentAI API in gcp. 
5. setup .env
6. run `python main.py` (`python3 main.py` if you are using linux)

# References

1. https://cloud.google.com/document-ai/docs/process-documents-client-libraries
2. https://cloud.google.com/document-ai/docs/samples/documentai-list-processors
3. https://cloud.google.com/document-ai/docs/create-processor