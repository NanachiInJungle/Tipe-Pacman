# Tipe-Pacman

**_Comment les mathématiques, et plus précisément les graphes (la théorie des graphes) peuvent-ils nous permettre d’améliorer nos performances (et prises de 
décisions) sur des jeux d’eSport ou plus largement en sport ?_**

  Avec l’arrivée de nouvelles technologies dans nos vies, de nouveaux loisirs sont aussi apparus. C’est pourquoi les jeux vidéos se démocratisent de plus  en plus, et avec eux la compétition eSportive. Il a fallu longtemps avant que l’eSport soit considéré comme un sport à part entière, et il reste des progrès à faire. Ainsi, le Comité International Olympique (CIO) organise (a organisé) du 22 au 25 juin 2023 les « Olympic Esport Series » à Singapour.

  Les jeux vidéos et l’eSport devenant de plus en plus compétitifs, il est alors intéressant d’élaborer des stratégies, de la même manière que les autres sports, afin d’optimiser les performances du sportif ou du joueur.

  De façon plus précise, il est souvent utile de chercher à optimiser un parcours dans un sport, que cela soit de la course d’orientation, du BMX freestyle, de l’escalade, une compétition de Pacman etc …

  Les jeux vidéos étant informatisés, il est alors plus simple de récolter des données et de se servir de ces jeux comme cobaye afin d’élaborer des stratégies de parcours dans l’environnement du jeu considéré.

  C’est pourquoi nous allons commencer par nous demander quel type d’algorithme et plus précisément quel algorithme permet de trouver le plus court chemin dans un environnement que l’on pourrait représenter par une grille avec plus ou moins d’obstacles.

  Ainsi, nous commencerons par comparer l’efficacité des différents algorithmes de recherche du plus court chemin, dans un labyrinthe semblable à celui de Pacman. C’est à dire dans une grille à coût uniforme dans laquelle on retrouve des obstacles mobiles ou non.

  Ces algorithmes recherches peuvent basés sur des parcours en largeur ou des parcours en profondeur, que l’on définira plus tard. Cela peut par exemple être un algorithme Dijkstra (https://fr.wikipedia.org/wiki/Algorithme_de_Dijkstra ), ou autre algorithme de recherche best-first, tels que l’algorithme de recherche en faisceau (https://fr.wikipedia.org/wiki/Algorithme_de_recherche_en_faisceau) , l’algorithme A* (https://fr.wikipedia.org/wiki/Algorithme_A*) ou encore l’algorithme Jump Point Search, une variante de A* adaptée pour les grilles à coût uniforme.

***Donner les defs de parcours largeur et Longueur***

  Nous utiliserons ainsi uniquement des algorithmes basés sur le parcours en largeur, car le parcours en profondeur est bien moins efficace.

***Demo de l'éfficacité deu parcours a faire: https://www.youtube.com/watch?v=aW9kZcJx64o***
