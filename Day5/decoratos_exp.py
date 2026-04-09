import requests


def boldtext(original_function):
  def wrapper():
    return "<b> " + original_function() + " </b>"

  return wrapper


@boldtext
def get_a_funny_phrase():
  return requests.get("https://official-joke-api.appspot.com/random_joke").json().get("setup", "Something is better than nothing")


@boldtext
def get_a_serious_phrase():
  return "Serious phrases are not funny, but they can be useful in certain situations."

print(get_a_funny_phrase())
print(get_a_serious_phrase())