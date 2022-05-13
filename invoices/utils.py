import random
possible_numbers=[x for x in range(10)]

def generate_invoice_number():
  list_nmbr=[str(random.choice(possible_numbers)) for _ in range(10)]
  nmbr_str=''.join(list_nmbr)
  return nmbr_str

