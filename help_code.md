# CODE TIPS

## GIT

[Git CheatSheet](https://education.github.com/git-cheat-sheet-education.pdf)

**Pull a branch forward and up-to-date with main**
``` 
git checkout <branch-name>
git merge main
git push
```

**Delete local and remote branch**
```
git branch -d local
git push origin -d local
```

**Checkout Local and Push to Remote**
```
git checkout -b local
git push --set-upstream origin local
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

4. Tests / Unit Testing?  
Pandas has their own testing module. [pandas.testing.assert_frame_equal](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.testing.assert_frame_equal.html) 

### Logging
Two Corey Schafer's Logging Videos are good.  
[Logging_Basics](https://www.youtube.com/watch?v=-ARI4Cz-awo&t=0s)  
[Logging_Advanced](https://www.youtube.com/watch?v=jxmzY9soFXg)  

Key takeaways:  
- Module and submodule may print out different logs.
- This can enable maintenance of different log files.  

Code snippet reference is here:  
- [example_logging.py](snippets/example_logging.py)
- [example_logging_module.py](snippets/example_logging_module.py)

## Software Architecture and UML Diagrams
How much should one learn to communicate in UML? 