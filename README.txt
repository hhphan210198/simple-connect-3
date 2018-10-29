- Name: Hieu Phan
- Favorite ice-cream flavor: Pineapple Coconut
- Collaborator: None
- The algorithm works well and is able to output correct answer on tested cases. However, the more blank spaces there
is, the longer it takes the algorithm to runs. This is reasonable because as there are more blank spaces to fill, there
are more possible states (branch factor of 5), thus it takes the algorithm longer to reach the leaves of the tree to
compute the mini-max. This can be improved such as by implementing alpha-beta pruning.
- The command to run is: python connect3.py input_file