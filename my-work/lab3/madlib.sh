

#!/bin/bash


clear
echo "Let's build a mad-lib!"

read -p "1. Name an unusual sport: " NOUN1
read -p "2. A describer word: " ADJ1
read -p "3. A type of pet: " NOUN2
read -p "4. Name a person: " NOUN3
read -p "5. Name a body part: " NOUN4
read -p "6. Name a verb: " VERB1
read -p "7. Name an adverb: " ADVERB1
read -p "8. Name a place: " NOUN5

echo "Here we go..."
clear

echo "I was playing $NOUN1 yesterday and one of the fans in the crowd had a $ADJ1 $NOUN2."
echo "It got loose and attacked $NOUN3 and bit them on the $NOUN4."
echo "$NOUN3 $VERB1 $ADVERB1 until the ambulance arrived, and brought them to the $NOUN5."
echo "The End."
