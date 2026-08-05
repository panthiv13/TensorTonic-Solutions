def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    top_k = recommended[:k]
    hits = sum(item in relevant for item in top_k)

    precision = hits / k
    recall = hits / len(relevant)

    return [precision, recall]