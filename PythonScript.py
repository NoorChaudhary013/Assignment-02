import pandas as pd

# Load CSV
df = pd.read_csv(r"C:\Users\G1F22UBSCS005\Downloads\study_performance.csv")

# Basic Exploration
print("\nFirst 10 rows:\n", df.head(10))
print("\nColumn Types:\n", df.dtypes)
cat_cols = df.select_dtypes(include=["object"]).columns
for col in cat_cols:
    print(f"Unique values in '{col}':", df[col].nunique())

# Data Cleaning
df = df.dropna()
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

# Statistics
scores = ["reading_score", "writing_score", "cgpa"]
for col in scores:
    avg = df[col].mean()
    min_v = df[col].min()
    max_v = df[col].max()
    std = df[col].std()
    print(f"\nStats for {col}: Avg={avg:.2f}, Min={min_v}, Max={max_v}, Std={std:.2f}")

# Filtering & Sorting
top_students = df[(df["reading_score"] > 90) & (df["writing_score"] > 90) & (df["cgpa"] > 90)]
print("\nStudents with scores > 90:\n", top_students)
sorted_df = df.sort_values(by="writing_score", ascending=False)
print("\nSorted by writing score:\n", sorted_df.head())

# Since 'gender' and 'test_preparation_course' columns are not available,
# let's skip Grouping & Aggregation tasks for now

# Transformation
df["average_score"] = df[scores].mean(axis=1)
def level(avg):
    if avg >= 90:
        return "Excellent"
    elif avg >= 70:
        return "Good"
    elif avg >= 50:
        return "Average"
    else:
        return "Poor"
df["performance_level"] = df["average_score"].apply(level)
print("\nFinal DataFrame with performance levels:\n", df.head())