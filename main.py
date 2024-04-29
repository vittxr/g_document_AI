import os
from google.api_core.client_options import ClientOptions
from google.cloud import documentai
from dotenv import load_dotenv

load_dotenv()

project_id = os.getenv("PROJECT_ID")
location = os.getenv("LOCATION")
file_path = "test_files/file_2.pdf"
processor_name = os.getenv("PROCESSOR_NAME")


def analyze(project_id: str, location: str, file_path: str, processor_name: str):
    opts = ClientOptions(api_endpoint=f"{location}-documentai.googleapis.com")
    client = documentai.DocumentProcessorServiceClient(client_options=opts)

    parent = client.common_location_path(project_id, location)
    processor_list = client.list_processors(parent=parent)
    processor = next(
        filter(lambda v: v.display_name == processor_name, processor_list), None
    )

    with open(file_path, "rb") as file:
        file_content = file.read()

    raw_document = documentai.RawDocument(
        content=file_content,
        mime_type="application/pdf",
    )

    request = documentai.ProcessRequest(name=processor.name, raw_document=raw_document)
    result = client.process_document(request=request)
    document = result.document

    print("The document contains the following text:")
    print(document.text)
    with open(f"results/{file_path.split('/')[-1].split('.')[0]}.txt", "w") as f:
        f.write(document.text)


analyze(
    project_id=project_id,
    location=location,
    file_path=file_path,
    processor_name=processor_name,
)
