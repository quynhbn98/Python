- This is how my IT colleague gave me a little bit taste of what he does everyday (and much less hard core :v)
- I learned how to handle `list, dictionary, tuple` ... thought these are some of my first lines of python code, and I really struggled with data processing and formatting
- Forgive me if my code is so hard to read... (my colleague didn't wanna read :v)  
  
    ###but it works :))

  I will refactor it someday...


- Data input:
    - A list of bag, with each bag's weight and destination
    - A list of trucks, with each truck's remaining weight and destination
    
- Requirement:
    - Assign which bag to put on which truck
    - Maximize truck capacity (least weight remaining) or number of bags on each truck or both
    - Format result data as required

- My solution:
    - For each destination, check its trucks and bags
      - I start from truck that has the least remaining weight
      - Then put in the heaviest bag it can contain
      - Then update all truck and bag data
      - Start over until no bag can fit in any trucks or list of unassigned bags is empty
    - Repeat for other destination
  