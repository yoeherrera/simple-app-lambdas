# Dockerfile for answer_question Lambda function
FROM public.ecr.aws/lambda/python:3.9

# Copy the function code
COPY . /var/task/

# Copy and install dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Command to run the Lambda function
CMD ["plot_freq.lambda_handler"]
