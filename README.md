# <span style = "color: purple">Color Project 
---
Hello, my name is *Brian Gardner*, at the time of this project I am currently an incoming freshman at <span style = "color: red">UMD</span>. Today, I will be working on a project called <span style = "color: purple">Colors. </span>


## <span style = "color: red">Description
1.Make a simple server in python, that reads an <span style = "color: red">*environment variable*</span> to display a color on the screen.

2.Put that server into a <span style = "color: red">docker container</span>.

3.Create  <span style = "color: red ">kubernetes manifests</span> to deploy the server with different deployments based on their color.
##  <span style = "color: gold">Goals
My goal in this project is to learn important  <span style = "color: gold">web development</span> and deployment skills. At the end of the project I will be more <span style = "color: gold">prepared</span> too start creating my portfolio website. This project will also give me free reign to understand what <span style = "color: gold">environment variables</span> are, and how I can utilize them in the future. 
## <span style = "color: green">Important Definitions
### This information can be found within this video: [What Are Enviornment Variables](https://youtu.be/bd65z5VZ7L4?si=QFGxlEM5bLHCnANZ)
### <span style = "color: green">Environment Variables: 

- An environment variable is a Linux/Windows variable which can directly affect a <span style = "color: green">proccess</span> within a system.
- This is because certain proccesses are directly linked to <span style = "color: green">environment variables</span>.
- <span style = "color: green">Example:</span>
    - LOG_LOCATION = /path/id/log
        - This changes the location in which a system contains its logs.
### <span style = "color: green">User Environment Variables Vs System Environment Variables:</span>
- <span style = "color: green">**User Environment Variables**</span> are environment variables that only affect a files path within a <span style = "color: green">system</span>. These will <span style = "color: green">not be</span> persistent after the terminal is killed.
- <span style = "color: green">**System Environment Variables**</span> are environment variables that do remain consistent, and are re used every time the code is run.

- <span style = "color: green">Example:</span>
  - Set INTERVAL = 1 (This sets the environment variable INTERVAL to 1)
  - echo %INTERVAL%(This outputs the INTERVAL enviroment variable we just changed.
### <span style = "color: green">Path Environment Variable</span>
- Path environment variable contains a list of directories seperated by a '/' in linux and a ';' in Windows.
- Example: 
   - set PATH = \myshortcuts
   - You can now access any file within that directory
### <span style = "color: green">Why Is This Important?</span>
- using <span style = "color: green">PATH</span> you can edit different files and proccesses in systems that you are not currently in 
-For Example
 - `echo $PATH nano .usr/local/bin/my_executable`
    - This creates a new text file within the designated path
 - `chmod .usr/local/bin/my_executable`
  - Gives the user proper permissions to run code
## <span style = "color: purple">Questions For Chris
- What is the difference between changing the path of an terminal and changing the directory?
- I need clarification on the difference between User-Controlled Variables and System Variables.
   - <span style = "color: purple">User Controlled Variables:</span> Are only accessible in the current terminal. They are not persistent
   - <span style = "color: purple">System Variables:</span> Are accessible in the whole project's system they are persistent.
- How do we know which ones are user controlled and which are System Variables?

    



