from django.db import models
import json

class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

def import_data_from_json(json_data):
    # Check if the database already has categories
    if Category.objects.exists():
        print("Data already imported. Skipping import.")
        return

    nodes = json_data["graph"]["nodes"]
    relationships = json_data["graph"]["relationships"]

    node_mapping = {}

    # First, create all nodes without parent relationships
    for node in nodes:
        category = Category(name=node["caption"])
        category.save()
        node_mapping[node["id"]] = category

    # Then, establish parent relationships based on the relationships in the JSON
    for relationship in relationships:
        child = node_mapping[relationship["toId"]]
        parent = node_mapping[relationship["fromId"]]
        child.parent = parent
        child.save()

    # for k, v in node_mapping.items():
    #     if v.parent:
    #         parent_name = v.parent.name
    #     else:
    #         print(k, v.name, "TOP")

def initialize_data():
    with open("neo4j_importer_model.json", "r", encoding="utf-8") as file:
        json_data = json.load(file)
    import_data_from_json(json_data)

# Call the function to load the data
# initialize_data()
