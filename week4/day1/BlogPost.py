#Create a BlogPost class that has
#an authorName
#a title
#a text
#a publicationDate
#Create a few blog post objects:
#"Lorem Ipsum" titled by John Doe posted at "2000.05.04."
#Lorem ipsum dolor sit amet.
#"Wait but why" titled by Tim Urban posted at "2010.10.10."
#A popular long-form, stick-figure-illustrated blog about almost everything.
#"One Engineer Is Trying to Get IBM to Reckon With Trump" titled by William Turton at "2017.03.28."
#Daniel Hanley, a cybersecurity engineer at IBM, doesn’t want to be the center of attention. When I asked to take his picture outside one of IBM’s New York City offices, he told me that he wasn’t really into the whole organizer profile thing.

class BlogPost():
    authorName = ""
    title = ""
    text = ""
    publicationDate = ""

BlogPost1 = BlogPost()
BlogPost2 = BlogPost()

BlogPost1.authorName = "John Doe"
BlogPost1.title = "Lorem Ipsum"
BlogPost1.text = "Lorem ipsum dolor sit amet."
BlogPost1.publicationDate = "2000.05.04."

BlogPost2.authorName = "Tim Urban"
BlogPost2.title = "Wait but why"
BlogPost2.text = "A popular long-form, stick-figure-illustrated blog about almost everything."
BlogPost2.publicationDate = "2010.10.10."


print (BlogPost1.authorName)
print (BlogPost1.title)
print (BlogPost1.text)
print (BlogPost1.publicationDate)
