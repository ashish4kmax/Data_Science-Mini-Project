import pandas as pd
import math

# Sample weather dataset
data = {
    'Outlook': ['Sunny', 'Sunny', 'Overcast', 'Rainy', 'Rainy', 'Rainy', 'Overcast', 'Sunny', 'Sunny', 'Rainy'],
    'Temperature': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool', 'Mild', 'Cool', 'Mild'],
    'Humidity': ['High', 'High', 'High', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'Normal'],
    'Windy': [False, True, False, False, False, True, True, False, False, False],
    'Play': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes']
}

# Create DataFrame
df = pd.DataFrame(data)

# Print the dataset table
print("Weather Dataset:")
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


# Calculate entropy of the 'Play' attribute
play_entropy = entropy(df['Play'])
print("Entropy of 'Play' attribute:", play_entropy)

# Calculate information gain for each attribute
max_gain = float("-inf")
best_attribute = None
for col in df.columns[:-1]:  # Exclude the target column 'Play'
    gain = information_gain(df, col, 'Play')
    print(f"Information Gain for {col}:", gain)
    if gain > max_gain:
        max_gain = gain
        best_attribute = col

print(
    f"\nBest attribute for splitting: {best_attribute} with Information Gain of {max_gain}")
