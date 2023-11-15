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

**Submodules**  
References:  
1. [This](https://dev.to/jjokah/submodules-a-git-repo-inside-a-git-repo-36l9) article explains submodules.  
2. [This]() git-scm book chapter provides a great reference manual.  
3. [autoware.repos](https://github.com/autowarefoundation/autoware/blob/main/autoware.repos) Autoware-AI manages submodules using a *.repos YAML configuration file.  
4. [vcstools](https://github.com/dirk-thomas/vcstool) To work with the YAML configuration file you need to install *vcstool* to manage submodules.  

## Clean Code Workflow  
Ref - https://pybit.es/articles/tips-for-clean-code-in-python/  
Flake8 PEP Checker - https://flake8.pycqa.org/en/latest/index.html  
Black Python Code Reformatter - https://black.readthedocs.io/en/stable/  
mypy - https://mypy-lang.org/  
pre-commit - https://pre-commit.com/#intro  
 
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

## Website Hosting on EC2 
How to host a Jekyll Website on AWS EC2 using NGINX?  
https://romainstrock.com/blog/static-website-nginx-ec2.html  
How to add authentication to NGINX webserver.  
https://www.youtube.com/watch?v=_zoDkXyXrx4  
How to buy a domain and configure DNS records using Route53.  
https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-register.html  
How to attach your EC2 instance to the domain.  
https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-ec2-instance.html  
How to convert http website to 

## Website Workflow.  

### Website Development Frameworks.  
1. Use Jekyll for Static Websites.  
    - MkDocs is a variant of this.  
    - Use a lot of advanced templates to make this easy. Nice features exist.  

2. Python Flask for Web Apps. This is still in draft mode.  

### Pipeline to Host.  
1. Hosting on S3 in a public bucket.  
    - Not https. 
    - Bucket content not private.  
2. Hosting on S3 using Cloudfront.  
    - Adds https functionality.  
    - Bucket content can be held private.  
    - Can attach a git based AWS code pipeline to publish to S3. 
    - Distribution takes place through cloudfront, which makes availability high.  
Ref - [https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html#create-oac-overview-s3](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html#create-oac-overview-s3)  
[Getting-Started-Simple-Distribution](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/GettingStarted.SimpleDistribution.html)  
  


3. Hosting on AWS EC2 webserver with NGINX and Basic Authentication.  
    - Can be full fledged private website with domain and authentication.  
    - Server content can be locked inside a SSH limited access.  