# Add "My todo:" to the beginning of the todoText
# Add " - Download games" to the end of the todoText
# Add " - Diablo" to the end of the todoText but with indention

# Expected outpt:

# My todo:
#  - Buy milk
#  - Download games
#      - Diablo

todotext = " - Buy milk\n"
todotext = "My todo: \n" + todotext
todotext = todotext + " - Download games\n"
todotext = todotext + "     -  Diablo\n"

print(todotext)
