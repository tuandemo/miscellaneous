inp = "input.txt"
fi = open(inp, "r")
data = fi.readlines()
data = [d for d in data if d != "\n"]
fi.close()

className = data[0]
data.remove(className)
classModifier = "public" if className[0] == "+" else "private" if className[0] == "-" else "default"
className = className.replace("\n", "")
className = className if classModifier == "default" else className[1:]
attributes = list(d.replace("\n", "") for d in data if "(" not in d)
methods = list(d.replace("\n", "") for d in data if "(" in d)

attributeAccessModifiers = []
attributeNames = []
attributeDataTypes = []
for a in attributes:
	if a[0] == "+":
		attributeAccessModifiers += ["public"]
	elif a[0] == "-":
		attributeAccessModifiers += ["private"]
	else:
		attributeAccessModifiers += ["default"]
	attributeNames += [a[1:a.find(":")]]
	attributeDataTypes += [a[a.find(":") + 1:]]

methodAccessModifiers = []
methodDataTypes = []
methodNames = []
methodParameters = []
for m in methods:
	if m[0] == "+":
		methodAccessModifiers += ["public"]
	elif m[0] == "-":
		methodAccessModifiers += ["private"]
	else:
		methodAccessModifiers += ["default"]
	if ":" in m[m.find(")"):]:
		methodDataTypes += [m[m.find(":") + 1:]]
	else:
		methodDataTypes += ["void"]
	methodNames += [m[1:m.find("(")] if m[0] in "+-" else m[:m.find("(")]]
	if "()" in m:
		methodParameters += [[]]
	else:
		betweenParentheses = m[m.find("(") + 1:m.find(")")].split(",")
		params = list(p[:p.find(":")] for p in betweenParentheses)
		paramsDataTypes = list(p[p.find(":") + 1:] for p in betweenParentheses)
		methodParameters += [[params, paramsDataTypes]]

data = []
data += [(classModifier + " " if classModifier != "default" else "") + "class " + className + " {\n\n"]
for i in range(len(attributes)):
	attribute = attributeAccessModifiers[i] + " " + attributeDataTypes[i] + " " + attributeNames[i] + ";"
	data += ["\t" + attribute + "\n"]
data += ["\n"]
for i in range(len(methods)):
	method = (methodAccessModifiers[i] + " ") if methodAccessModifiers[i] != "default" else ""
	method += (methodDataTypes[i] + " " if methodNames[i] != className else "") + methodNames[i]
	if len(methodParameters[i]) == 0:
		method += "()"
	else:
		method += "("
		for j in range(len(methodParameters[i][0])):
			method += methodParameters[i][1][j] + " " + methodParameters[i][0][j] + ", "
		method = method[:-2]
		method += ")"
	method += " { }"
	data += ["\t" + method + "\n\n"]
data += ["}"]

out = "output.java"
fo = open(out, "w")
fo.write("".join(data))
fo.close()
