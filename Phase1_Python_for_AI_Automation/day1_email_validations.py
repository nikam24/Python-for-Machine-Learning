emails = ["test@example.com", "invalid-email", "user@domain.com"] 

def is_valid_email(email): 
    if ".com" in email and "@" in email: 
        return True 
    return False 

for (index, email) in enumerate(emails, start=1): 
    if is_valid_email(email): 
        print(f"Email {index}: {email} is valid") 
    else: 
        print(f"Email {index}: {email} is invalid")