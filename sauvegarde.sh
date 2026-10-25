#!/bin/bash
date_du_jour=$(date +%Y-%m-%d)
echo "sauvegarde du $date_du_jour"

mkdir donnees_du_$date_du_jour
touch file1 file2
mv file* ./donnees_du_$date_du_jour

echo "sauvegarde terminer"

echo "donnees_du_$date_du_jour/" >> .gitignore
