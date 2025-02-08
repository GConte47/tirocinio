import pandas as pd

def parse_entities_to_dataframe(data):
    """
    Parses the entities section of a dictionary into a Pandas DataFrame.
    
    Args:
        data (dict): Dictionary containing 'entities' as a key with nested entity information.
        
    Returns:
        pd.DataFrame: A DataFrame containing the relevant fields from the entities.
    """
    # Extract the 'entities' dictionary
    entities = data.get('entities', {})
    
    # List to hold rows of the DataFrame
    rows = []
    
    # Loop through each entity
    for entity_id, entity_data in entities.items():
        # Extract relevant fields
        row = {
            "entity_id": entity_id,
            "pretty_name": entity_data.get("pretty_name", ""),
            "cui": entity_data.get("cui", ""),
            "type_ids": entity_data.get("type_ids", []),
            "types": entity_data.get("types", []),
            "source_value": entity_data.get("source_value", ""),
            "detected_name": entity_data.get("detected_name", ""),
            "acc": entity_data.get("acc", 0.0),
            "context_similarity": entity_data.get("context_similarity", 0.0),
        }
        # Append the row to the list
        rows.append(row)
    
    # Create a DataFrame
    df = pd.DataFrame(rows)
    
    return df

# Example usage:
data = {
    # Paste your JSON structure here
    'entities': {
  0: {'pretty_name': 'Patients', 

   'cui': 'C0030705', 

   'type_ids': ['T101'], 

   'types': ['Patient or Disabled Group'], 

   'source_value': 'patient', 

   'detected_name': 'patient', 

   'acc': 0.8600446532108288, 

   'context_similarity': 0.8600446532108288, 

   'start': 4, 

   'end': 11, 

   'icd10': [], 

   'ontologies': [], 

   'snomed': [], 

   'id': 0, 

   'meta_anns': {'Status': {'value': 'Affirmed', 

     'confidence': 0.9998550415039062, 

     'name': 'Status'}}}, 

  2: {'pretty_name': 'Adult', 

   'cui': 'C0001675', 

   'type_ids': ['T100'], 

   'types': ['Age Group'], 

   'source_value': 'year-old', 

   'detected_name': 'year~old', 

   'acc': 0.5926714412420233, 

   'context_similarity': 0.5926714412420233, 

   'start': 20, 

   'end': 28, 

   'icd10': [], 

   'ontologies': [], 

   'snomed': [], 

   'id': 2, 

   'meta_anns': {'Status': {'value': 'Affirmed', 

     'confidence': 0.9999629259109497, 

     'name': 'Status'}}}, 

  4: {'pretty_name': 'Caucasians', 

   'cui': 'C0043157', 

   'type_ids': ['T098'], 

   'types': ['Population Group'], 

   'source_value': 'Caucasian', 

   'detected_name': 'caucasian', 

   'acc': 1.0, 

   'context_similarity': 1.0, 

   'start': 29, 

   'end': 38, 

   'icd10': [], 

   'ontologies': [], 

   'snomed': [], 

   'id': 4, 

   'meta_anns': {'Status': {'value': 'Affirmed', 

     'confidence': 0.9998550415039062, 

     'name': 'Status'}}}, 

  5: {'pretty_name': 'Woman', 

   'cui': 'C0043210', 

   'type_ids': ['T098'], 

   'types': ['Population Group'], 

   'source_value': 'female', 

   'detected_name': 'female', 

   'acc': 0.8221183791276476, 

   'context_similarity': 0.8221183791276476, 

   'start': 39, 

   'end': 45, 

   'icd10': [], 

   'ontologies': [], 

   'snomed': [], 

   'id': 5, 

   'meta_anns': {'Status': {'value': 'Affirmed', 

     'confidence': 0.9998550415039062, 

     'name': 'Status'}}}, 

  8: {'pretty_name': 'History of - diabetes mellitus', 

   'cui': 'C0455488', 

   'type_ids': ['T033'], 

   'types': ['Finding'], 

   'source_value': 'history of diabetes', 

   'detected_name': 'history~of~diabetes', 

   'acc': 1.0, 

   'context_similarity': 1.0, 

   'start': 53, 

   'end': 72, 

   'icd10': [], 

   'ontologies': [], 

   'snomed': [], 

   'id': 8, 

   'meta_anns': {'Status': {'value': 'Affirmed', 

     'confidence': 0.9999799728393555, 

     'name': 'Status'}}}
             # Additional entities can be added here
    }
}


df = parse_entities_to_dataframe(data)
df

#The patient is a 71-year-old Caucasian female with a history of diabetes. 