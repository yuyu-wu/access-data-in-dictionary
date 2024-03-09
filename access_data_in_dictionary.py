'''
Access Data in a Dictionary Exercise
Given the dictionary below:

artist = {
    "first": "Neil",
    "last": "Young",
}
Declare a variable called full_name  that is equal to artist's first  and last  names with a space between. You must reference the values associated with those keys in the artist dictionary.

print(full_name)
# Neil Young
'''


# Solution using string concatenation:

artist = {
    "first": "Neil",
    "last": "Young",
}

full_name = artist["first"] + " " + artist["last"]

# Solution using the format() method:

artist = {
    "first": "Neil",
    "last": "Young",
}
 
full_name = "{} {}".format(artist["first"], artist["last"])


# Only works in Python 3.6 or greater.   
# Pay attention to the quotes

artist = {
    "first": "Neil",
    "last": "Young",
}
 
full_name = f"{artist['first']} {artist['last']}"