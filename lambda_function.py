import json

def lambda_handler(event, context): 
  #TODO implement 
  #Get the email address from the event 
  email = event['email'] 
  #Validate the email address 
  if validate_email(email): 
    return { 
      'statusCode': 200, 
      'body': json.dumps('Email address is valid!') 
    } 
  #Return an error message 
  else: 
    return { 
      'statusCode': 400, 
      'body': json.dumps('Email address is not valid!') 
    }

#Function that validates an email address using regex 
def validate_email(email): 
  import re 
  regex = 
  r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b' 
  if(re.fullmatch(regex, email)): 
    return True 
  else: 
    return False 
