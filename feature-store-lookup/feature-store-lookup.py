def feature_store_lookup(feature_store, requests, defaults):
    results = []

    for req in requests:
        user_id = req["user_id"]
        online = req["online_features"]

        # Get offline features or defaults
        offline = feature_store.get(user_id, defaults)

        # Merge (offline first, then online)
        combined = {**offline, **online}

        results.append(combined)

    return results
