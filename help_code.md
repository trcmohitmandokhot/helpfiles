# CODE TIPS

## GIT

[Git CheatSheet](https://education.github.com/git-cheat-sheet-education.pdf)

**Pull a branch forward and up-to-date with main**
``` 
git checkout <branch-name>
git merge main
git push
```

## Project Repository Structure 
### GUI Apps
TodoApp
- .gitignore
- LICENSE
- README.md
- docs
    - how_to_use.md
    - how_to_contribute.md
    - ...
- todo
    - __init__.py
    - app.py
    - ui
        - gui.py
        - gui.ui
    - model
        - __init__.py
        - ModelClass.py
        - helper.py
    - tests
        - __init__.py
        - test_class.py
        - test_gui.py(?)
    - common_libs
        - __init__.py
        - helper_funcs.py
    - data
        - user1.json

This data structure is inspired from the following references:  
1. [Structuring Your Project](https://docs.python-guide.org/writing/structure/)
2. [Dead Simple Python: Jason McDonald](https://dev.to/codemouse92/dead-simple-python-project-structure-and-imports-38c6)
    
Other tips.
1. Use absolute imports only.  
2. Add author and version information in app.py 

## Python Techniques
1. Classes Structure. Corey Schafer videos that outline Object Oriented Programming with Python. 
2. Error Handling.  Corey Schafer Videos [here](https://www.youtube.com/watch?v=NIWwJbo-9_8)
3. Type Hinting. Tech with Tim Videos [here](https://www.youtube.com/watch?v=QORvB-_mbZ0)
4. Logging 
5. Tests / Unit Testing? 
