import random
possible_numbers=[x for x in range(10)]

def generate_account_number():
  list_account=[str(random.choice(possible_numbers)) for _ in range(15)]
  account_str=''.join(list_account)
  return account_str

