import iron

ironapp = iron.Iron("tokker.html", "tonk")
ironapp.vars["key"] = "4322"
ironapp.inject(htmlCode = "<code>print('Hello World!!')</code> # number |%key%|", params = ["key"])

