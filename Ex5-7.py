def parse_query_string(url: str) -> dict :
    params = {}
    url_list = url[url.index("?") + 1:]
    var_list = url_list.split("&")
    print(var_list)
    for item in var_list :
        k , v = item.split("=")
        params[k]= v
    return params
print(parse_query_string("http://example.com/show_item.php?item=car&color=red"))
