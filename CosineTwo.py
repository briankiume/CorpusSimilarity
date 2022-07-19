from scipy.spatial.distance import cosine


# Returns 2 separate list of indexes based on closest cosine distance between two zipped lists

def cosine_two(zipped_1, zipped_2):
    final = []
    for x in zipped_2:
        distances = {}
        dists = []
        for y in zipped_1:
            dist = cosine(x[0], y[0])
            new = [x[1], y[1]]
            distances[dist] = new
            dists.append(dist)
        # print(distances)
        least = min(dists)
        for key in distances:
            if key == least:
                final.append(distances[key])
    id_pair_1 = []
    id_pair_2 = []
    for pair in final:
        id_pair_1.append(pair[1])
        id_pair_2.append(pair[0])
    return id_pair_1, id_pair_2
