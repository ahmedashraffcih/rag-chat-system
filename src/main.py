import openai 
from dotenv import load_dotenv
import os
import argparse
from src.utils.constants import *
from modules.query import query_data
from modules.extraction import generate_data_store

load_dotenv()
openai.api_key = os.environ['OPENAI_API_KEY']

parser = argparse.ArgumentParser()
parser.add_argument("query_text", type=str, help="The query text.")
args = parser.parse_args()
query_text = args.query_text

if __name__ == '__main__':
    # Create database
    # generate_data_store()

    query_data(query_text)