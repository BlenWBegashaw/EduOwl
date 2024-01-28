from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
from diagrams.aws.integration import SQS
from diagrams.custom import Custom
from diagrams.onprem.client import User
from diagrams.onprem.compute import Server
from diagrams.onprem.iac import Ansible
from diagrams.programming.language import Python

with Diagram("Enhanced Software Architecture", show=False):
    with Cluster("User Interface"):
        user_input = User("User Input")
        input_processing = Python("Input Processing")

    with Cluster("Backend Services"):
        chat_function = Python("Chat Function")
        data_processing = Server("Data Processing")
        pdf_extraction = RDS("PDF Extraction")
        langchain_component = Custom("LangChain", "/Users/blenbegashaw/PycharmProjects/pythonProject1/1*44fD_VXcqw2kDWublQLONw.jpeg")  # Update the path to your LangChain logo

    with Cluster("Integration"):
        openai_api = Custom("OpenAI API", "/Users/blenbegashaw/PycharmProjects/pythonProject1/logo-open-ai.png")  # Update the path to your OpenAI logo
        memory = ELB("Memory Storage")

    with Cluster("Response Generation"):
        response_processing = Python("Response Processing")
        user_output = User("User Output")

    # Connections
    user_input >> input_processing >> chat_function
    chat_function >> data_processing >> pdf_extraction
    pdf_extraction >> langchain_component >> openai_api
    openai_api >> memory >> response_processing
    response_processing >> user_output

    # Additional styling
    pdf_extraction - Edge(color="red", style="dotted") - data_processing
