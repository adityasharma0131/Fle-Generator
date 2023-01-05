import os
import time
import sys
#Built-in Module's


# to make a new directory for the new project with a user defined name
directory_Name = input('Enter The Folder name: ')
os.mkdir(directory_Name)

# to Enter the Directory we created for a new Project
val = os.getcwd()
os.chdir(f'{val}\\{directory_Name}')


print("Loading:")
#animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

for i in range(len(animation)):
    time.sleep(0.3)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()

print("\n")


#in this we will create 3 basic files of web-development{HTML| CSS| Javascript}

#every file contains user defined name 
html_File = input('Enter the Name of the HTML File: ')
css_File = input('Enter the Name of the CSS File: ')
js_File = input('Enter the Name of the JS File: ')


#These will open a file in the write mode to create a new file in the user defined directory with their specific user-defined name with the help of f-STRING
main_HTML = open(f'{html_File}.html', 'w+')
style_CSS = open(f'{css_File}.css', 'w+')
main_JS = open(f'{js_File}.js', 'w+')



#this will be written in the HTML file 
main_HTML.write(f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    
    
    <link rel="stylesheet" href="{css_File}.css"> 
</head>
<body>
    
    
    
    
    <script src="{js_File}.js"></script>
</body>
</html> 
         ''')

# this will be written in the CSS file
style_CSS.write('''           
:root{
    --white: #ffff;
}

*{
    padding: 0;
    margin: 0;
    box-sizing: border-box;
}

body{
    height: 100vh;
    display: flex;
} 
''')

# This will be written in JS File 

main_JS.write('''function function_Name() {
    console.log("Hello World");
}  ''')

# Once the file is opened in the write mode('w+') it should be definitely closed 
main_HTML.close()
style_CSS.close()
main_JS.close()