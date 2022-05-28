OBJ = [
    'Fibula',
    'Scapula',
    'Hip',
    'Mandible',
    'Genio',
    'Ribs',
    'Skull',
]
KEYS = []
VALUES = []
VAL = []


def split_dict(xOBJ):
    "for easier iteration / INPUT-names / OUTPUT-names with lower letters"
    for xobj in xOBJ:
        yield str.lower(xobj)


def append_value(dict_obj, key, value):
    "append dictionary by keys and values / INPUT - empty dictionary; keys and values - one by one / OUTPUT - full dictionary"
    # Check if key exist in dict or not
    if key in dict_obj:
        # Key exist in dict.
        # Check if type of value of key is list or not
        if not isinstance(dict_obj[key], list):
            # If type is not list then make it list
            dict_obj[key] = [dict_obj[key]]
        # Append the value in list
        dict_obj[key].append(value)
    else:
        # As key is not in dict,
        # so, add key-value pair
        dict_obj[key] = value


def iter_dict(iterDict):
    "main part / INPUT - range of iteration for letter combination / OUTPUT-dictionary with values of possible combination for each keys "
    dict3 = {}
    count = {}
    combi3 = []
    one = []
    for iter in iterDict:
        for obj in split_dict(OBJ):
            for o in range(len(obj)):
                start = o
                end = start+iter
                if end <= len(obj):
                    comb = obj[start:end]
                    append_value(dict3, obj, comb)

        for val in dict3.values():
            for v in val:
                combi3.append(v)

        for i in combi3:
            if not i in count:
                count[i] = 1
            else:
                count[i] += 1

        for key, val in count.items():
            if val == 1:
                one.append(key)

        combi3 = list(set(combi3))

        for o in one:
            if o in combi3:
                combi3.remove(o)

        for key, val in dict3.items():
            if type(val) == list:
                for c in combi3:
                    if c in val:
                        val.remove(c)

    return dict3


# Create only original combinations of letters / 2-combination of 2 letter / max-len of biggest name
max = len(OBJ[0])
for i in range(len(OBJ)):
    if len(OBJ[i]) > max:
        max = len(OBJ[i])

NameDict = iter_dict(range(2, max))
print("Dictionary with possible original combinations:\n", NameDict, "\n\n")

for key, val in NameDict.items():
    VALUES.append(val)

for v in VALUES:
    if len(v) > 1:
        for i in range(len(v)-1):
            for j in range(1, len(v)):
                if v[i] in v[j]:
                    VAL.append(v[j])

for key, val in NameDict.items():
    for c in VAL:
        if c in val:
            val.remove(c)

print("Dictionary with smaller uniq combinations:\n", NameDict)
