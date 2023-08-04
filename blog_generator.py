#!/usr/bin/env python3

import openai
# First, we've imported a method called dotenv_values from the module.
from dotenv import dotenv_values

#The dotenv_values() will take in the path to the .env file and return us a dictionary with all the variables in the .env file. We then created a config variable to hold that dictionary.

config = dotenv_values(".env")

#Now, all we have to do is replace the exposed API key with the environment variable in the config dictionary like so:
openai.api_key = config['API_KEY']  # Securing Our App

# Note: If you want to push your code to GitHub, you don't want to push the .env file as well. In the root directory of your project, create a file called .gitignore, and in the Git ignore file, type in .env. This will prevent the file from being tracked by Git and ultimately pushed to GitHub.

# the core function
def generate_blog(paragraph_topic):
	response = openai.Completion.create(
		model = 'text-davinci-002',
		prompt = 'Write a paragraph about the following topic.' + paragraph_topic,
		max_tokens = 400,
		temperature = 0.3
	)
	
	retrieve_blog = response.choices[0].text
	
	return retrieve_blog

print(generate_blog('Which programming language should I learn to get a good job in 2023'))

# multiple paragrapgs
keep_writing = True
while keep_writing == True:
	answer = input('Write a paragraph? Y for yes, anything else for no.')
	if (answer == 'Y'):
		paragraph_topic = input('What should this paragraph be about? ')
		print(generate_blog(paragraph_topic))
	else:
		keep_writing = False
		
# rate limit - Rate limit is the number of API calls an app or user can make within a given time period. For GPT-3, the rate limit is 20 requests per minute. 

		

		
		
