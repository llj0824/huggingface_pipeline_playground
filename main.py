from transformers import pipeline; 
import argparse

# Get User Argument
parser = argparse.ArgumentParser() 
parser.add_argument('arg1', type=str, help='Input text') 
args = parser.parse_args() 

# Accessing the argument
print(pipeline('sentiment-analysis')(args.arg1))

