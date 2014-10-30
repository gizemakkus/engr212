from recommendations import *

prefs = loadMovieGenre("u.item")

#print sim_jaccard(prefs, "Action", "Adventure")
print sim_jaccard2(prefs, "Action", "Adventure")


print topMatches(prefs, "Adventure", similarity=sim_jaccard)
print topMatches(prefs, "Drama", similarity=sim_jaccard)
#print topMatches(prefs, "Drama", similarity=sim_jaccard2)
print topMatches(prefs, "Thriller", similarity=sim_jaccard)