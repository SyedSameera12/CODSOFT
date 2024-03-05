import pandas as pd

# Sample user-item ratings data (replace with your own dataset)
ratings_data = {
    'userId': [1, 1, 1, 2, 2],
    'itemId': ['a', 'b', 'c', 'b', 'c'],
    'rating': [5, 4, 3, 2, 1]
}

ratings_df = pd.DataFrame(ratings_data)

# Function to create user-item matrix
def create_user_item_matrix(df):
    user_item_matrix = df.pivot_table(index='userId', columns='itemId', values='rating', fill_value=0)
    return user_item_matrix

user_item_matrix = create_user_item_matrix(ratings_df)

# Function to calculate similarity between users
def calculate_user_similarity(user_item_matrix):
    similarity_matrix = {}
    for user1 in user_item_matrix.index:
        similarity_matrix[user1] = {}
        for user2 in user_item_matrix.index:
            if user1 != user2:
                similarity = sum(user_item_matrix.loc[user1] * user_item_matrix.loc[user2]) / (
                        (sum(user_item_matrix.loc[user1] * 2) * 0.5) * (sum(user_item_matrix.loc[user2] * 2) * 0.5))
                similarity_matrix[user1][user2] = similarity
    return similarity_matrix

user_similarity = calculate_user_similarity(user_item_matrix)

# Function to predict ratings
def predict_ratings(user_id, item_id, user_item_matrix, user_similarity):
    numerator = 0
    denominator = 0
    for user in user_item_matrix.index:
        if user != user_id and user_item_matrix.loc[user, item_id] != 0:
            numerator += user_similarity[user_id][user] * user_item_matrix.loc[user, item_id]
            denominator += abs(user_similarity[user_id][user])
    if denominator == 0:
        return 0
    else:
        return numerator / denominator

# Example: Predict rating for user 1 on item 'c'
predicted_rating = predict_ratings(1, 'c', user_item_matrix, user_similarity)
print("Predicted rating for user 1 on item 'c':", predicted_rating)