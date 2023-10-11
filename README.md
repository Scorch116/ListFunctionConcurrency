# ListFunctionConcurrency
Created this script to assist users to list lambda function with a region that using both reserved and provisioned concurrency and how much concurrency they are using.

This will save the user time going through the console to find out which functions have reserved/provisioned concurrency and how much.

Note: Lambda Execution role will need the following permissions:

lambda:GetFunctionConcurrency
lambda:ListFunctions
lambda:ListProvisionedConcurrencyConfigs


The following application code can be simply run in a Lambda function.

Application will list lambda function in region. Using a nested for loop, the list will iterated through and will return the lambda functions.

The results from the for loop will then call the get_function_concurrency which will return details about the reserved/provisioned concurrency configuration for each function in the defined region.

Users can simply paste this code into a lambda function, within the code section. Users will just have to update the variable "region" with the desired region they would like to list functions using concurrency.
