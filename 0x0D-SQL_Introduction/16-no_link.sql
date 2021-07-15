#LISTER TOUS LES LIGNES DE LA TABLE seconde_table
SELECT score, name FROM second_table WHERE name IS NOT NULL or name = '' ORDER BY score DESC;
