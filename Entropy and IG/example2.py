import pandas as pd
import math

# Sample bank customer dataset
data = {
    'Age': [35, 45, 30, 25, 40, 60, 55, 28, 32, 48],
    'Income': ['Low', 'Low', 'Low', 'Medium', 'Medium', 'High', 'High', 'Low', 'Medium', 'High'],
    'Marital_Status': ['Single', 'Married', 'Single', 'Single', 'Married', 'Married', 'Single', 'Single', 'Married', 'Married'],
    'Education': ['Primary', 'Secondary', 'Primary', 'Primary', 'Secondary', 'Tertiary', 'Secondary', 'Primary', 'Secondary', 'Tertiary'],
    'Term_Deposit': ['No', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No', 'No', 'Yes', 'Yes']
}

# Create DataFrame
df = pd.DataFrame(data)

# Print the dataset table
print("Bank Customer Dataset:")
print(df)
print()


def entropy(target_col):
    """
    Calculate the entropy of a target column.
    """
    entropy = 0
    values = target_col.unique()
    for val in values:
        p = target_col.value_counts()[val] / len(target_col)
        entropy += -p * math.log2(p)
    return entropy


def information_gain(data, split_attribute_name, target_name):
    """
    Calculate the information gain of a dataset for a given attribute.
    """
    # Calculate the total entropy before splitting
    total_entropy = entropy(data[target_name])

    # Calculate the values and counts for the split attribute
    values = data[split_attribute_name].unique()
    weighted_entropy = 0
    for val in values:
        subset = data[data[split_attribute_name] == val]
        subset_entropy = entropy(subset[target_name])
        weighted_entropy += (len(subset) / len(data)) * subset_entropy

    # Calculate information gain
    information_gain = total_entropy - weighted_entropy
    return information_gain


# Calculate entropy of the 'Term_Deposit' attribute
deposit_entropy = entropy(df['Term_Deposit'])
print("Entropy of 'Term_Deposit' attribute:", deposit_entropy)

# Calculate information gain for each attribute
max_gain = float("-inf")
best_attribute = None
for col in df.columns[:-1]:  # Exclude the target column 'Term_Deposit'
    gain = information_gain(df, col, 'Term_Deposit')
    print(f"Information Gain for {col}:", gain)
    if gain > max_gain:
        max_gain = gain
        best_attribute = col

print(
    f"\nBest attribute for splitting: {best_attribute} with Information Gain of {max_gain}")
