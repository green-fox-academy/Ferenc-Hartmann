#Create a PostIt class that has
#a backgroundColor
#a text on it
#a textColor
#Create a few example post-it objects:
#an orange with blue text: "Idea 1"
#a pink with black text: "Awesome"
#a yellow with green text: "Superb!"

class PostIt():
    backgroundColor = ""
    text = ""
    textcolor = ""

PostIt1 = PostIt()
PostIt2 = PostIt()

PostIt1.backgroundColor = "orange"
PostIt1.text = "Idea 1"
PostIt1.textcolor = "blue"

PostIt2.backgroundColor = "pink"
PostIt2.text = "Awesome"
PostIt2.textcolor = "black"

PostIt3.backgroundColor = "yellow"
PostIt3.text = "Superb"
PostIt3.textcolor = "green"

print (PostIt2.backgroundColor)
print (PostIt2.text)
print (PostIt2.textcolor)
