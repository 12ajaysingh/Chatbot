import json

CATALOG = None


def load_catalog():
    global CATALOG

    if CATALOG is None:
        with open("data/shl_catalog.json", "r", encoding="utf-8") as f:
            CATALOG = json.load(f)

    return CATALOG


def search_catalog(keywords):

    catalog = load_catalog()

    expanded_keywords = []

    for keyword in keywords:
        expanded_keywords.extend(
            keyword.lower().split()
        )

    results = []

    for assessment in catalog:

        text = (
            assessment["name"] + " " +
            assessment["description"] + " " +
            " ".join(assessment["keys"])
        ).lower()

        score = 0

        for keyword in expanded_keywords:

            if keyword in text:
                score += 1

        if score > 0:
            results.append((score, assessment))

    results.sort(key=lambda x: x[0], reverse=True)

    return [item[1] for item in results]

    
    