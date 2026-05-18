import pandas as pd
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def main():
    print("--- Project 2: Data Classification Using AI ---")
    
    # 1. Load and understand the dataset
    print("\n[Step 1] Loading the Wine Dataset...")
    # The Wine dataset is a classic classification dataset for predicting wine cultivars based on chemical analysis.
    wine_data = load_wine()
    
    # Create a pandas DataFrame for better visualization
    df = pd.DataFrame(data=wine_data.data, columns=wine_data.feature_names)
    df['target'] = wine_data.target
    
    print("\nDataset Shape:", df.shape)
    print("Target classes:", wine_data.target_names)
    print("\nFirst 5 rows of the dataset:")
    print(df.head())
    
    # 2. Split data into training and testing sets
    print("\n[Step 2] Splitting data into Training and Testing sets...")
    X = wine_data.data
    y = wine_data.target
    
    # 80% for training, 20% for testing
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print(f"Training data features shape: {X_train.shape}")
    print(f"Testing data features shape: {X_test.shape}")
    
    # 3. Apply a classification algorithm
    print("\n[Step 3] Applying Random Forest Classifier...")
    # Initialize the model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    
    # Train the model
    model.fit(X_train, y_train)
    print("Model training complete.")
    
    # Make predictions on the test set
    print("\n[Step 4] Evaluating the model...")
    y_pred = model.predict(X_test)
    
    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f"\n=> Model Accuracy: {accuracy * 100:.2f}%")
    
    print("\n=> Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    
    print("\n=> Classification Report:")
    print(classification_report(y_test, y_pred, target_names=wine_data.target_names))

if __name__ == "__main__":
    main()
