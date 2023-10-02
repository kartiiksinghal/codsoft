#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[8]:


print("------------------------Codsoft Task-2------------------------")
print("PASSWORD GENERATOR")

# Importing necessary libraries
import random
import string

def generate_pass(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Asking user for password length
while True:
    pass_len = input("Enter password length: ")

    if pass_len.isdigit() and int(pass_len) > 0:
        pass_len = int(pass_len)
        break
    else:
        print("Invalid input. Please enter a positive integer.")

# Generating and displaying the password
generated_pass = generate_pass(pass_len)
print("Generated Password:", generated_pass)


# In[ ]:




