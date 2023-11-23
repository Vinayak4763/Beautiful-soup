import requests ,string
from bs4 import BeautifulSoup

with open("sample.html","r") as f:
       html_doc=f.read()

soup=BeautifulSoup(html_doc,'html.parser')
#print(soup.prettify())
#print(soup.find_all("div")[1#])
#for link in soup.find_all("a"):
      #

#s=soup.find(id="link3")
#print(soup.span.get("class")) 
#print(soup.find_all(class_="italic"))
#for parent in soup.find (class_="container").parents:
  #     print(parent)
# cont=soup.find(class_="container")
# cont.name="span"

# cont["class"]="myclass"
# cont.string="i am wonderful"
# print(cont)

# ultag=soup.new_tag("ul")
# litag=soup.new_tag("li")
# litag.string="Home"

# ultag.append(litag)

# litag=soup.new_tag("li")
# litag.string="Home"

# ultag.append(litag)
# soup.html.body.insert(0,ultag)
# ##with open("modified.html","w") as f:
# #          f.write(str(soup))

# cont=soup.find(class_="container")
# print(cont.has_attr("content"))

def class_but_not_id(tag):
       return  tag.has_attr("class") and  tag.has_attr("id")

results=soup.find_all(class_but_not_id)
print(results)