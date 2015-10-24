#  W    zorowane na przykładzie Rona Zacharskiego


# -*- coding: utf-8 -*-
from math import sqrt

users = {
    "Ania": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5,
             "The Strokes": 2.5, "Vampire Weekend": 2.0},
    "Bonia": {"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5,
              "Vampire Weekend": 3.0},
    "Celina": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5,
               "Slightly Stoopid": 1.0},
    "Dominika": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5,
                 "The Strokes": 4.0, "Vampire Weekend": 2.0},
    "Ela": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},
    "Fruzia": {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5,
               "The Strokes": 4.0, "Vampire Weekend": 4.0},
    "Gosia": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0,
              "The Strokes": 5.0},
    "Hela": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0}
}


def manhattan(rating1, rating2):
    """Oblicz odległość w metryce taksówkowej między dwoma  zbiorami ocen
       danymi w postaci: {'The Strokes': 3.0, 'Slightly Stoopid': 2.5}
       Zwróć -1, gdy zbiory nie mają wspólnych elementów"""
    a = users[rating1]
    b = users[rating2]
    suma = 0
    for i, j in a.items():
        for k, m in b.items():
            if i == k:
                war = abs(j - m)
                suma = suma + war
            else:
                suma = suma + 0

    if suma == 0:
        return -1
    else:
        return suma

    # TODO: wpisz kod


def computeNearestNeighbor(username, users):
    """dla danego użytkownika username, zwróć ze słownika users nazwę użytkownika o najbliższych preferencjach"""
    distance = []

    for i, j in users.items():
        if i != username:
            odl = manhattan(username, i);
            # dodanie do listy na ostatniej pozycji kolejnej odległości
            distance.insert(len(distance) + 1, (i, odl))
    nameOfNearestNeighbor = []

    if (sorted(distance, key=lambda distance: distance[1])[0])[1] != \
            (sorted(distance, key=lambda distance: distance[1])[1])[1]:
        nameOfNearestNeighbor = [(sorted(distance, key=lambda distance: distance[1])[0])[0]]
    else:
        for i in range(len(distance) - 1):
            if (sorted(distance, key=lambda distance: distance[1])[i + 1])[1] == \
                    (sorted(distance, key=lambda distance: distance[1])[i])[1]:
                nameOfNearestNeighbor.insert(i, (sorted(distance, key=lambda distance: distance[1])[i])[0])
                nameOfNearestNeighbor.insert(i + 1, (sorted(distance, key=lambda distance: distance[1])[i + 1])[0])
            else:
                break
    return nameOfNearestNeighbor


def recommend(username, users):
    """Zwróć listę rekomendacji dla użytkownika"""
    # znajdź preferencje najbliższego sąsiada
    nearest = computeNearestNeighbor(username, users)
    recommendations = []

    if len(nearest) == 1:
        pom=nearest[0]
        b = users[pom]
        num = 0
        for i in users[pom].keys():
            if i in users[username].keys():
                recommendations = recommendations
            else:
                recommendations.insert(num, i)
                num += 1
    else:
        for i in range(len(nearest)):
            pom=nearest[i]
            b = users[pom]
            num=0
            for j in users[pom].keys():
                if j in users[username].keys():
                    recommendations=recommendations
                else:
                    recommendations.extend([j])

        for a in range(len(recommendations)):
            if recommendations.count(recommendations[a])>1:
                recommendations[a]=None

        for a in range(recommendations.count(None)):
            recommendations.remove(None)



    # zarekomenduj użytkownikowi wykonawcę, którego jeszcze nie ocenił, a zrobił to jego najbliższy sąsiad
    return sorted(recommendations, key=lambda artistTuple: artistTuple[1], reverse=True)

# przykłady

print(recommend('Hela', users))
print( recommend('Celina', users))
