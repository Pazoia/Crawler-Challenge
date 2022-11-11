def sanitise_str(string):
  if u"\u2019" in string:
    new_string = string.replace(u"\u2019", "'")
    return new_string
  
  return string