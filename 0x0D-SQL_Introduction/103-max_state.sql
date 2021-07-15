#LISTER LA TEMPERATURE MAX DE CHAQUE CITE
SELECT state, MAX(value) as max_temp FROM temperatures GROUP BY state ORDER BY state ASC;
