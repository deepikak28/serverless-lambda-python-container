FROM public.ecr.aws/lambda/python:3.8

# Copy function code

COPY http_response.py ${LAMBDA_TASK_ROOT}

COPY lambda.py ${LAMBDA_TASK_ROOT}

CMD [ "lambda.handler" ]