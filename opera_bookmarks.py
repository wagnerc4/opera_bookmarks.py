from json import load


def json_to_html(level, rq):
  rs = []
  for item in rq:
    if item["type"] == "folder":
      rs.append(('    ' * level) + '<DT><H3>'+item["name"]+'</H3>')
      rs.append(('    ' * level) + '<DL><p>')
      rs.extend(json_to_html(level+1, item["children"]))
      rs.append(('    ' * level) + '</DL><p>')
    else:
      rs.append(('    ' * level) + '<DT><A HREF="'+item["url"]+'">'+item["name"]+'</a>')
  return rs


with open('Bookmarks') as data_file:
  data = load(data_file)


html = json_to_html(0, data["roots"]["bookmark_bar"]["children"])


with open("bookmarks.html", "w") as text_file:
  print('\n'.join(html), file=text_file)
